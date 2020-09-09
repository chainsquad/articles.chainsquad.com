---
layout: post
title: "Atomic Swaps vs. Sidechain - Don't get fooled"
tags: atomic swaps sidechain
comments: true
---

In recent months, we have witnesses some confusion in the crypto currency
community about what *atomic swaps* can offer and why they are not necessarily
in-line with common understandings of a *sidechain*. We here want to clarify
the terms and ensure the reader can distinguish these despite confusing
marketing in the public.

To do that, we first discuss what atomic swaps can do (not going into the
details of how they do it) and what the general understanding of "sidechain"
is. We will conclude by giving a simple thought experiment by discussion supply
movements.

<!--more-->

## What Atomic Swaps

Despite the technical details being quite complex due to the usage of
hash-time-locked contracts (HTLCs) with *hashing* and a *time-lock*, the
essence of what an atomic swap can do is quite simple: **Let two asset change
hands without a third party**.

Personally, i wouldn't call Atomic Swaps *atomic* as there are multiple
processes involved and the actually *swapping* of the assets is far from being
*atomic* in the sense that they take place that same time. Yet, the swap is
often considered atomic since the flow itself is mostly automated and has almost
no attack vectors from timing point of view.

If you think about an atomic swap another way, it really is two people meeting
each other, one person has one asset, the other has another asset. They swap
the assets by handing them over to each other at the same time.

Of course, atomic swaps are interesting because the assets don't necessarily
need to be on the same blockchain which makes this an **inter-blockchain
transaction**, really. In fact, there is an entire
[protocol](https://interledger.org) that builds on top of atomic swaps to
facilitate the exchange of large sums of value.

What becomes quite clear from the above description is that the blockchains
themselves do not talk to each other directly, but the swapping takes places
through human beings, trust-minimized due to the use of HTLCs.

## Sidechain

To be honest right away, we don't think a clear and concise definition of
sidechain really exists. The wikipedia uses this:

> A sidechain is a designation for a blockchain ledger that runs in parallel to
> a primary blockchain. Entries from the primary blockchain (where said entries
> typically represent digital assets) can be linked to and from the sidechain;
> this allows the sidechain to otherwise operate independently of the primary
> blockchain (e.g., by using an alternate means of record keeping, alternate
> consensus algorithm, etc.).

While this is true for any blockchain that allows to operate user-issued assets
(or coloured coins, ERC20 tokens, etc), it does not discuss the aspect of
trust. In short: What you argue about a blockchain being a "sidechain" just
because someone manages a BTC symbol on it and allows deposits and withdrawals?
Would you consider an exchange being a sidechain because it has an (mostly
internal) database (ledger) for managing user balances? We don't.

For us, a true sidechain can operate independently (like Wikipedia says), but
also autonomously and trustlessly. This is where the challenges, because no
sidechains exist, yet. All that the community has are centralized *gateways*
(where one operator controls the supply of a token, liked *wrapped* BTC on
Ethereum), or a *federated* gateway (where multiple parties *jointly* managed
the supply, like with [Liquid](https://blockstream.com/liquid/)). No fully
automated, autonomous, and trustless sidechain exists, yet and given the
limited functionalities of Bitcoin, we may never find one - at least not with
Bitcoin.

### What would a true sidechain look like?

Let's say we have two different blockchains that each have their own
functionality and features. Let's say, the target audience of one blockchain is
*music* and the other blockchain focuses on *social media*. Now, obviously,
some users want to use both. Instead of having to spend money to obtain tokens
on both blockchains, which is capital in-efficient, the ideal solution would be
to have a common digital asset that can move freely (and without counterparty
risk) from one chain to the other and vise versa. So, in a sense, the
blockchains may need to be aware of each other, or at least of the transfers
that affect both of them so they can independently verify and validate moving
funds.

# Supply Comparison

The different between sidechain and atomic swaps is quite simple to see if you
take a look at the supply side. In the case of regular atomic swaps, the supply
on both blockchains stay the same - only the hands change - and the blockchains
are not aware of each other. On the other hand, a sidechain allows to move
supply from one chain to another. Tokens that are transferred disappear from
one chain (i.e., reduce the supply) while they appear on the other chain (i.e.,
are newly minted).

Now that we understand the difference, we also see where the challenges are.
Obviously, developing a true sidechain is (still) considered the *holy grail*
in the space. But don't let yourself get fooled by marketing buzzword bing, at
this point, no team has managed to build a truly autonomous and
counterparty-risk free sidechain to Bitcoin.

We do envision that true sidechains will become available in the future, but
they may not interact with Bitcoin but with other (more sophisticated)
blockchains.
