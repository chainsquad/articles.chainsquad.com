---
layout: post
title: Tributary Development Update - Referral Program, Custom Fees, and x402 v2
tags: tributary solana payments x402
comments: true
---

86 commits. 21,000+ lines of code. Three features that change what Tributary can
do on Solana. We've been heads-down shipping since launch, and this is what came
out.

<!--more-->

## The Referral Program

This was the biggest piece of work since we went live. A three-tier referral
chain with a 60/30/10 reward split. The original referrer (L3) gets the largest
cut. Their referrer (L2) gets half that. The immediate referrer (L1) gets the
smallest slice.

### Account Storage

Early implementations used simple mappings. That didn't scale. We pivoted to
Anchor's `AccountLoader` pattern for PDA derivation and validation. The referral
account seed now includes the referral code itself, so a single user can have
multiple referral codes across different gateways.

This constraint surfaced late. It was critical for flexibility.

### Chain Ordering

The trickiest part wasn't the smart contract logic. It was the chain ordering.

The SDK's `getReferralChain()` returns accounts bottom-up: `[L1, L2, L3]`. But
Rust's assignment logic reverses this for fee distribution. We spent a full day
debugging why rewards weren't landing where expected. After that, we documented
the contract-SDK interface explicitly in `specs/referral-program.md`.

The fix:

```
level1_referrer = L3
level2_referrer = L2
level3_referrer = L1
```

Counter-intuitive? Yes. Documented now? Also yes.

## Custom Protocol Fees

Protocol fees are now configurable per gateway. Not just globally.

We added a feature flag (`use_custom_protocol_fee`, bit 2) to the
`PaymentGateway` struct and an admin-only instruction
`update_gateway_protocol_fee` that lets protocol administrators set
gateway-specific rates.

### The Security Model

Gateways cannot toggle their own custom fee flag. That's reserved for protocol
admin. We added masking in `update_gateway_referral_settings` to prevent gateway
authority from modifying bit 2. Gateways can optimize their fee structure, but
they can't bypass protocol oversight.

```rust
if ctx.accounts.gateway_authority.is_signer() && use_custom_protocol_fee.is_some() {
    return err!(ErrorCode::UnauthorizedFeatureFlagModification);
}
```

Tests cover three scenarios: custom fee at 0 bps (no protocol fee charged),
disabled custom fee (reverts to global 100 bps default), and unauthorized
gateway attempts. All rejected where they should be.

## x402 v2

The x402 middleware got a complete overhaul. We migrated from `X-Payment`
headers to the new `Payment` header format, added subscription support, and
wrote 55 passing unit tests across metering utilities and middleware components.

The metering module tracks usage across time windows with proper reset logic.
The middleware validates payment headers before allowing request processing.
Coverage reports land in `x402/coverage/` with full lcov output for CI.

Documentation followed implementation: three new docs files covering overview,
getting started, and API reference. We also created a dedicated x402 server
implementation in `x402/server.ts` that handles the full payment flow.

## Milestone Payments

Milestone-based payments are now usable. We replaced Unix timestamp inputs with
native HTML5 `datetime-local` pickers in the payment policy form. The form
validates chronologically — each milestone must be later than the previous one,
and all must be in the future.

The scheduler was extended to handle time-based milestones, not just
subscriptions. This required threading `next_payment_due` through the execution
path and adding proper timestamp comparisons in `execute_payment.rs`.

## Semantic Versioning for Monorepo

Unsexy but essential. We implemented independent semantic versioning across all
packages. SDK, SDK-React, and other packages now version independently based on
commit message scopes:

- `feat(sdk):` triggers minor bumps
- `fix(sdk):` triggers patches

Five GitHub workflows handle testing, SDK publishing, and release management.
The release workflow creates GitHub releases based on semantic release analysis.
npm publishing gets proper version tags for downstream consumers.

## What We Learned

- Referral chain ordering is counter-intuitive — document the contract-SDK
  interface explicitly
- Feature flags need strict ownership — gateways can't control their own fee
  flags
- Datetime pickers beat Unix timestamps — UX improvements pay dividends
- Independent versioning works for monorepos — commit-based automation scales

## What's Next

The referral program is almost merged and will be live soon with full test
coverage. Custom protocol fees give gateway operators flexibility. x402 v2
provides a production-ready payment middleware.

Next up: scaling the scheduler and deeper x402 integrations.

Ship it.
