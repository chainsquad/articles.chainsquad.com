---
layout: post
title: Proving Payments Without a Backend - How Tributary Uses JWT
tags: tributary solana payments jwt x402
comments: true
---

Everyone accepting crypto subscriptions runs into the same wall. How do you
verify a user has paid without running your own backend?

Stripe gives you webhooks and server-side sessions. In Web3, the standard
approach is to run an RPC node, poll the blockchain, and maintain your own
payment state. That's infrastructure tax for something that should be simple.

We built [Tributary](https://tributary.so) to solve this.

<!--more-->

![alt](/img/posts/proving-payments.webp)

## Signed JWTs from On-Chain State

Tributary issues cryptographically signed JWTs that carry payment proofs. No
backend required on the merchant side.

The flow:

1. User clicks "Subscribe" on `checkout.tributary.so`
2. Wallet signs the transaction. On-chain: `UserPayment`, `PaymentPolicy`,
   delegate approval created.
3. Tributary API reads on-chain policies, signs a JWT (ES256) with a JWKS key,
   redirects to `successUrl?token=<jwt>`
4. Merchant frontend validates the JWT via public JWKS endpoint. No backend.
   Subscription claims are verified. Access is granted.

The merchant never talks to Solana directly. The JWT is the proof.

## What's Inside the JWT

Every JWT contains the user's active subscription claims, signed by
Tributary's ES256 key:

```json
{
  "sub": "7xKpV2BZQ3HfeRZFMfWVBpDCmCN8eYwGmCjL7m3mVqR",
  "iss": "https://api.tributary.so",
  "aud": "tributary-checkout",
  "subscriptions": [
    {
      "recipient": "BxKp...9mVq",
      "amount": "10.00",
      "tokenMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
      "paymentFrequency": "monthly",
      "status": "paid",
      "totalPayments": 3,
      "nextPaymentDue": 1746057600
    }
  ]
}
```

Validation is three lines:

```javascript
import { jwtVerify, createRemoteJWKSet } from "jose";
const { payload } = await jwtVerify(
  token,
  createRemoteJWKSet(new URL("https://api.tributary.so/.well-known/jwks.json")),
  { issuer: "https://api.tributary.so", audience: "tributary-checkout" },
);
```

No database. No RPC polling. No webhook endpoints.

## Why This Works

### Stateless

Tributary's API reads on-chain state at issuance time, signs it, hands it off.
No server-side session storage. No token database.

### Expiration tied to payment cycles

Token TTL is `nextPaymentDue + 10min`, capped at 30 days. The token expires
when the next payment is due. That forces a refresh, which re-reads the
blockchain.

```
exp = min(
  earliest nextPaymentDue + 10 minutes,
  now + 30 days
)
```

Monthly subscription? JWT lives ~30 days minus 10 minutes. Weekly? ~7 days.
Yearly? Capped at 30 days regardless.

The 10 minute overlap exists so the facilitator can catch an overdue
subscription and trigger its payment on-chain before the merchant notices.

### Refresh is a fresh read

When the token expires, the merchant calls `POST /v1/tokens/refresh` with the
expired JWT. Tributary verifies the signature (expired is fine, forged is not),
re-queries on-chain state, and issues a new JWT. No sessions. No stored tokens.

This is stateless re-issuance.

### JWKS is publicly verifiable

The `/.well-known/jwks.json` endpoint serves public keys. Anyone can cache and
use them. Key rotation happens every 30 days with a 24-hour grace period.
In-flight tokens never break.

### The data is public anyway

The JWT contains only on-chain subscription data. Amounts, recipients, payment
status, next due dates. No secrets. No balances. No private keys. Bearer-token
semantics are acceptable here. The worst case is someone reads public payment
info.

All backend services, indexer, database, and API of Tributary are MIT license.
Anyone can operate them.

## When You Need a Backend

JWTs handle the "prove you paid" case. Granting access, checking status,
displaying subscription info. Pure frontend. Event-driven by users visiting
your site.

But some businesses need background tasks that react to payment events:

- Revoke access when a payment fails
- Send "payment overdue" emails
- Trigger provisioning on new subscription
- Maintain audit logs of payment state changes

For these, the business runs their own Facilitator (Gateway).

## The Facilitator Model

Facilitators are the entities that trigger `execute_payment` on-chain. They're
the crank that makes recurring payments happen. Any business can operate their
own.

The key insight: the Facilitator already knows whether a payment succeeded or
failed. It's the one executing it.

The flow:

1. Facilitator's cron fires
2. Is this policy's `nextPaymentDue` passed?
3. Yes? Call `execute_payment()` on-chain.
4. TX confirmed? Payment made. Update local DB. Send confirmation email.
   Extend access for another period.
5. TX failed? Payment failed. Update local DB. Send overdue notification.
   Schedule retry.
6. No? Skip, check next policy.

The Facilitator doesn't poll the blockchain to check if a payment happened. It
already knows. It submitted the transaction. Success or failure is immediate,
local, and deterministic.

No indexing lag. The Facilitator knows payment state at transaction submission
time, not whenever an indexer catches up.

No webhook dependency. The Facilitator is the source of truth for its own
payment executions.

## The Decision Tree

Do you need to react to payment events in the background?

No? JWT-only. Pure frontend. User visits your site, you validate the JWT, you
grant or deny access. JWT expired? Refresh via API, get a new one. No backend.
No database. No Facilitator needed.

Yes? Run a Facilitator plus optional backend. The Facilitator executes payments
on schedule. It knows success or failure immediately. Your backend stores local
payment state for business logic. You can still use JWTs for frontend access
checks. Full control: email triggers, provisioning, analytics.

Both can coexist. A business might use JWTs for frontend access checks while
running a Facilitator for background tasks.

## Mental Model

Think of the JWT as a digitally signed receipt the customer carries with them.

For access control (gated content, SaaS features, premium tiers): check the
receipt at the door. JWT validation on the frontend. No backend.

For operational automation (billing emails, access revocation, provisioning): be
the cashier. Run a Facilitator. You see every transaction because you're the one
processing it.

## JWKS Infrastructure

- Algorithm: ES256 (ECDSA P-256). Smaller tokens, faster verification than
  RS256.
- Key storage: Postgres + Drizzle ORM, encrypted at rest with AES-256-GCM.
- Rotation: automatic every 30 days, admin override available.
- Grace period: 24 hours after rotation. Old key still validates in-flight
  tokens.
- Endpoint: `GET /.well-known/jwks.json`. Publicly cacheable for 1 hour.

## Rate Limits

- `/v1/tokens/issue`: 10 req/min per wallet
- `/v1/tokens/refresh`: 30 req/min per wallet

Refresh mechanics:

1. Accept expired JWT. Must have valid signature (prevents forgery).
2. Must be within 7-day grace window past expiration.
3. Extract wallet pubkey from `sub` claim.
4. Re-query all subscription policies from blockchain.
5. Build fresh JWT with current on-chain state.
6. Return new token.

## Room for Innovations

The JWT bridges Solana's trustless on-chain state and Web2-style application
logic. Signed by Tributary, verified by anyone, expired by design.

What's left to build:

- Trustless JWT issuance without Tributary as intermediary. A smart contract
  that signs tokens directly.
- Cross-chain verification. The same JWT pattern on other chains.
- Zero-knowledge proofs instead of bearer tokens. The merchant learns "user has
  paid" without learning which user or how much.

The current system works. The next iteration should remove the need to trust
us at all.
