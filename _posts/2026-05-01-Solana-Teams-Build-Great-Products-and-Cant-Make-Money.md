---
layout: post
title: Solana Teams Build Great Products and Can't Make Money
tags: tributary solana payments subscriptions
comments: true
---

Solana teams are building great products. Many can't make money. Not because the
market isn't there or users wouldn't pay. Because collecting recurring revenue
on-chain was hard.

Until now.

<!--more-->

## What a Subscription Actually Requires

A user says "charge me $X every month." That charge happens automatically. The
user stays in control.

In Web2, Stripe does this in five lines of code. In Web3, every single
transaction needs a user signature. That's the fundamental mismatch.

## What Teams Do Instead

They pick from a menu of bad options:

- Gate the product behind a one-time payment. Bad for retention.
- Ask users to manually renew every period. They don't.
- Build a custodial workaround. Terrible for trust.
- Create a token on pumpfun. I have no comment on this one.
- Give up and offer the product for free.

The same problem hits web-based apps that want to touch Solana. You build a
great SaaS. You want to charge users. You look at your options. No smart
contract means no transaction fees. No automated billing means manual invoices
or Stripe. And Stripe means off-chain, no crypto, no composability.

## How We Fixed This

Solana's SPL token standard lets users delegate spending authority without
locking up funds. We built a protocol on top of this.

1. User approves once.
2. Protocol charges automatically according to the rules the user set.
3. User can pause, resume, or cancel anytime.

No middleman holding your funds. No trust assumptions. No smart wallet required.

Because it's a protocol, not a product, any team can build on top of it. One
contract, unlimited businesses.

## Three Business Models

We built for how real businesses actually charge:

- **Subscriptions** -- fixed amount, recurring schedule
- **Milestones** -- release funds when conditions are met
- **Pay-as-you-go** -- charge per usage, within user-set limits

One SDK. Three business models. Five lines of TypeScript.

## What This Unlocks

A DePIN project that bills by usage. An AI API that charges per token. A SaaS
tool that runs monthly renewals without Stripe. Any web app that wants to
monetize without building payment infrastructure from scratch.

The business model layer for Solana.

## Where We Are

We started building this for Cyphrypunk. We continued through Frontier. Always
building in public.

Live on mainnet. Full SDK. React components and hooks.

The infra is done. We are onboarding teams that use it.

If you've ever said "we'll figure out payments later" -- later is now.

- Docs: [docs.tributary.so](https://docs.tributary.so)
- SDK: `npm install @tributary-so/sdk`
- DM us if you want to be a design partner
- [tributary.so](https://tributary.so)

Subscriptions on Solana. Built right. Ready today.

## Room for Innovations

What's still missing:

- Agent-controlled spending where AI models manage their own budgets
- Cross-chain recurring payments using the same policy model
- Governance-integrated billing where DAOs vote on fee structures

The protocol handles the plumbing. The use cases are yours to build.
