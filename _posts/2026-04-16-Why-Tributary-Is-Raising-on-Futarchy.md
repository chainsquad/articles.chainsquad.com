---
layout: post
title: Why Tributary Is Raising on Futarchy
tags: tributary solana futarchy payments metaDAO
comments: true
---

Most on-chain payments are optimized for the first transaction. The second one
-- and the 200th -- is where products either become reliable infrastructure or
quietly break.

Crypto is pretty good at one-off transfers. It is still weirdly bad at recurring
payments. Subscriptions, repayments, usage-based billing, scheduled payouts,
milestone-based compensation, agent-controlled spending. These are the flows
that decide whether a product becomes an operation or stays an experiment.

That gap is why we built Tributary. Recurring payment infrastructure for Solana.

<!--more-->

![alt](/img/posts/futardio-raise.webp)

## What Tributary Is

Tributary is a live protocol on Solana mainnet. It handles recurring payment
logic: subscriptions, milestone payments, pay-as-you-go billing, and (soon)
controlled top-ups. Developers integrate a reusable payment layer instead of
building custom rails from scratch every time.

The approach is non-custodial. Users authorize payment policies with explicit
constraints: who gets paid, how much, when, and when it stops. Payments execute
according to those rules. Users can pause, resume, or cancel anytime.

The protocol charges a 1% fee on payment volume. That fee flows into a treasury
soon to be owned by token holders. More payment volume, more fees, more
treasury value. Simple.

## What's Already Live

Tributary has been live on Solana mainnet since October 2025. This isn't a
whitepaper or a roadmap promise.

- The app: [app.tributary.so](https://app.tributary.so)
- The docs: [docs.tributary.so](https://docs.tributary.so)
- The SDK: `@tributary-so/sdk` on npm
- The checkout: [checkout.tributary.so](https://checkout.tributary.so)

Yumi Finance is already using Tributary in production for cash loans with
automatic repayments. That's a serious use case. Repayments aren't a marketing
moment. They're a reliability test. They're the part of a product that has to
work even when nobody is watching.

Allowly runs recurring subscription flows on Tributary. Contribute.so runs
recurring crypto donations for GitHub developers. Each hits a different surface
area of the same underlying problem: money that needs to move repeatedly,
predictably, and with clean UX.

## Why the Category Matters

When most people hear "recurring payments," they think "subscriptions." That's
part of it. The category is broader.

- **SaaS billing** -- monthly software licenses, API access
- **Lending** -- automated repayments on fixed schedules
- **Commerce** -- repeat merchant flows, checkout integrations
- **Creator economy** -- memberships, recurring support, patronage
- **Professional services** -- retainers, milestone-based project payments
- **AI and agents** -- usage-based billing, controlled top-ups, spending limits

Money that needs to move repeatedly, according to rules, without rebuilding the
whole system every time.

If Solana is going to support real software businesses, real commerce, and real
on-chain organizations, recurring payments can't remain a bespoke workaround
that every team reinvents alone.

## Why Raise on Futarchy

We're raising via MetaDAO's [Futard.io](https://futard.io). The choice is
intentional, not convenient.

In a traditional raise, valuation is negotiated in a small room. Narrative does
a lot of work. Everyone's incentives are to sound confident, simplify risk, and
move fast.

Futarchy flips the posture.

It's harder to hide behind a deck. It's next to impossible to outsource
diligence to "smart money." It rewards clarity, not charisma. It makes it
obvious whether the market thinks the product is real enough to underwrite
today.

For payments infrastructure specifically, this alignment matters. Payments isn't
a meme category. It's the part of the stack where people care about reliability,
edge cases, and whether integrations will keep working next month.

The MetaDAO community has seen what happens with hype-first raises. Ranger
raised $8M on trading infrastructure promises and was liquidated by governance
vote.

The community has also seen what succeeds. Omnipair raised $1.1M with working
code and is up 100% from ICO. Umbra raised $3M with a working privacy protocol
and is up 39% from ICO.

Real product, specific use case, conservative target. That's the pattern
Tributary fits.

The question the market needs to answer isn't "will this product work?" It
already works. The question is "will it grow?" Futarchy lets participants
answer that question with real capital and real consequences. If the market says
yes, the raise proceeds fund growth. If it says no, everyone gets their capital
back.

The primary reasons we chose Futard.io, in order of priority:

1. It lets you raise from a wide audience without backdoor deals.
2. It lets you hand over the contract to the DAO.
3. It gets you attention about the product you build.

## What the Raise Funds

The product is built. This isn't about proving Tributary can exist. It already
does.

The capital funds the next stage:

- **Audit** -- security and trust matter for infrastructure people build on
- **Runway** -- roughly six months to execute without distraction
- **Integrations** -- more live products running on Tributary
- **Growth** -- developer onboarding, ecosystem awareness, clearer use-case
  packaging

The risk investors are underwriting isn't execution risk. It's growth risk.
That's a fundamentally different bet. Arguably a smaller one.

## Who's Building This

Dr.-Ing. Fabian Schuh. 10+ years in web3. Work across multiple top-10 L1
ecosystems. Full-time on Solana for two years. Superteam Germany member. PhD in
engineering.

Fabian has built on BitShares, Steemit, and Hive. In the last two years he has
worked on multiple projects (most of them stealth) on Solana. He also built
web2 products that integrated with payment providers such as Adyen and Stripe --
for instance [relay.md](https://relay.md). This gives him direct experience with
the kind of product and crypto payment problems Tributary solves.

He also built [repo.trade](https://repo.trade), which clarified the need for
simpler recurring support flows. repo.trade became contribute.so.

This isn't a team chasing a narrative. It's a protocol founder with real
shipping history building infrastructure for an important category.

## AMA

Fabian will attend ownershipfm radio on Sunday 19th April 2026 to answer all
your questions.

## The Honest Framing

Tributary is early in adoption. PMF is not proven. We haven't done a serious
growth push yet.

But early is different from imaginary. The product is live. The SDK exists. The
docs exist. Multiple payment models exist. And there's already live usage.

Important category. Live product. Real integrations. Clear room to scale.
Raising through a mechanism that holds us accountable from day one.

If that's the kind of bet you want to evaluate:

- App: [app.tributary.so](https://app.tributary.so)
- Docs: [docs.tributary.so](https://docs.tributary.so)
- SDK: `npm install @tributary-so/sdk`
- Checkout: [checkout.tributary.so](https://checkout.tributary.so)
- Telegram: [t.me/tributaryso](https://t.me/tributaryso)

Read the docs. Touch the app. Look at the integrations. Ask hard questions.

That's the standard we're building to.

## Room for Innovations

Recurring payments on-chain are still early. What's left to build:

- Trustless fee distribution where token holders vote on treasury allocation
- Cross-chain recurring payments using the same policy model
- Agent-native payment policies where AI models manage their own spending
  limits without human intervention

Tributary is live. The raise is live on Futard.io. If the market thinks this
category matters, the capital arrives. If not, we keep shipping anyway.
