---
layout: post
title: Accepting Recurring Solana Payments in React Without Losing Your Mind
tags: tributary solana react payments sdk
comments: true
---

You're building a dApp. The UI is shaping up. Then someone says "we need
subscriptions." Suddenly you're deep in token account delegation, PDA derivation,
transaction construction, and error handling that makes your React components look
like a graveyard of `useEffect` chains.

We built `@tributary-so/sdk-react` so you don't have to hand-roll any of that. A
collection of React hooks that wrap the Tributary payment protocol on Solana.
Drop recurring payments into your app. Move on.

Here's how it works, using our example payments app as the guide.

<!--more-->

![alt](/img/posts/integrate-checkout.webp)

## The Problem

Solana payments at the protocol level involve several moving parts. Payment
policies, delegate approvals, gateway accounts, fee distribution. If you've ever
wired up `@solana/web3.js` manually for a subscription flow, you know the drill.
Dozens of lines just to build, sign, and confirm a single transaction.

We wanted to get from "I need a subscribe button" to "the subscription is live
on-chain" in under 20 lines of component code.

## Two Paths: Checkout or Hooks

Tributary gives you two integration paths:

- **Checkout Sessions** -- redirect to a hosted payment page. Zero wallet
  connection needed in your app. You just want to collect money.
- **Direct Hooks** -- full control. Build your own UI, manage the wallet
  connection yourself. For when checkout pages aren't enough.

Both live in the same `@tributary-so/sdk-react` package. Let's start with the
simpler one.

## The Checkout Flow (No Wallet Required)

Fastest path from zero to payments. You don't even need
`@solana/wallet-adapter` in your app. The checkout page handles wallet
connection for you.

The entire payment initiation from our example app:

```javascript
import { useCheckoutSession } from "@tributary-so/sdk-react";

export default function Home() {
  const { initiate } = useCheckoutSession(CHECKOUT_BASE_URL);

  const handlePaymentRequest = () => {
    initiate({
      mode: "subscription",
      tokenMint: USDC_MINT,
      recipient,
      gateway: GATEWAY,
      amount: parseFloat(amount),
      trackingId,
      paymentFrequency: "monthly",
      autoRenew: true,
    });
  };

  return <button onClick={handlePaymentRequest}>Proceed to Payment</button>;
}
```

That's it. `useCheckoutSession` takes your checkout base URL and returns two
functions:

- `generateUrl(opts)` -- returns a checkout URL string. Use this for sharing
  payment links or rendering QR codes.
- `initiate(opts)` -- redirects the browser straight to the checkout page.

Under the hood, `useCheckoutSession` creates a `CheckoutSessionManager`,
encodes your payment parameters (amount, token, recipient, frequency), and
builds the full URL with callback routes. The `successUrl` and `cancelUrl` are
automatically derived from your current origin. The user lands back on your site
after paying.

One-time payments? Just set `mode: "payment"` and drop the frequency options.

```javascript
initiate({
  mode: "payment",
  tokenMint: USDC_MINT,
  recipient,
  amount: 9.99,
  memo: "One-time purchase",
});
```

## Verifying the Payment on Return

After a successful checkout, the user gets redirected back with a JWT token in
the URL query string. The `useTributaryToken` hook handles verification:

```javascript
import { useTributaryToken } from "@tributary-so/sdk-react";

export default function Success() {
  const { token, payload, loading } = useTributaryToken();

  if (loading) return <p>Verifying token...</p>;
  if (!token || !payload) {
    return <p>No valid payment token found.</p>;
  }

  return (
    <div>
      <h1>Payment Successful</h1>
      <p>Status: {payload.status}</p>
      <p>Tracking ID: {payload.trackingId}</p>
    </div>
  );
}
```

The hook reads `?token=` from the URL by default, sends it to the Tributary
verifier API, and decodes the JWT payload. You get `loading`, `error`, and the
decoded payload. Standard React hook pattern. No surprises.

You can also pass a token explicitly if you're getting it from somewhere other
than the URL:

```javascript
const { payload } = useTributaryToken(myJwtToken);
```

## The Full Example App

Our `example-payments` app is a Vite + React project that demonstrates the
complete checkout flow:

- **Home page** -- collects recipient address, amount, and payment mode
  (one-time vs. monthly). Uses `useCheckoutSession` to redirect to the checkout
  page.
- **Success page** -- reads the JWT from the URL and verifies it with
  `useTributaryToken`.
- **Cancel page** -- "payment cancelled" state.

## Getting Started

```bash
npm install @tributary-so/sdk-react @tributary-so/payments
```

For direct hooks, you'll also need the wallet adapter:

```bash
npm install @solana/wallet-adapter-react @solana/wallet-adapter-react-ui
```

Wrap your app with `ConnectionProvider` and `WalletProvider`. The hooks pick up
wallet and connection from context automatically.

The example app runs on devnet out of the box. Clone it, `pnpm install`,
`pnpm dev`, and you're accepting payments in minutes.

- [Tributary](https://tributary.so)
- [Example app on GitHub](https://github.com/tributary-so/example-payments)
- [Full docs](https://docs.tributary.so)

Accepting recurring payments on Solana shouldn't require a deep dive into CPI
calls and PDA derivation. The hooks handle the protocol complexity. You focus on
the product.
