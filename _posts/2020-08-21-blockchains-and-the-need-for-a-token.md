---
layout: post
title: Blockchains and the need for a token
tags: core token
comments: true
---

Whenever people start talking about *blockchain* they often imply *crypto
currencies*. However, a blockchain itself doesn't require *any* token and still
be a blockchain. The mere requirement for being public and permission-less,
however makes a token (of some value) a requirement.

<!--more-->

## A simple and stupid blockchain

On a technical basis, a blockchain is a simple **hash-linked list**. That means
arbitrary data is stored in a block and these blocks are linked through the hash
of the previous block's data. By linking many blocks, we end up in a
blockchain. Quite easy to understand.

## The *protocol*

Now, what makes blockchain technologies interesting is that they come with a
*protocol*. To us, this protocol describes the **rules of the game** in the sense
that you have to play by the rules or you **cannot play**. The protocol is what
gives a blockchain some meaning. For instance, if we break down Bitcoin's protocol,
it could be simplified by these two rules:

1. You can transfer bitcoins to another bitcoin address
2. You cannot make your own balance go below zero

Obviously, Bitcoin can do way more than that (for the interested reader look up
[Bitcoin Script](https://en.bitcoin.it/wiki/Script))

Either way, you can only get transactions into the blockchain that follow these
rules. And there are other blockchain systems that have other rules, some of which
offer a lot of features and flexibility - but that's outside the scope of this
article.

## The need for a token

As with a stupid blockchain, the protocol itself doesn't require a 'token'
per-se. One could build a chess-game using computer slang and make those the
protocol of your chess-game blockchain.

However, there is one aspect that may require your blockchain to have a *core*
token of value and that is the **consensus scheme**. Think of the consensus
scheme as the part of the technology that makes all participants *agree* on
what's going on and for that someone has to operate servers in the network that
connects your participants. These servers come at an expense to the operates so
that they seek for an incentive to continue providing a consensus node. That is
why *block producers* are almost always paid for their service of producing
blocks.

In case of Bitcoin, the consensus mechanism requires additional work for block
producers in that some additional (hard) metric (find a certain hash that
fulfills some dynamic target difficulty) is met. This *proof of work* comes
with additional expenses for computational hardware and makes for a huge
upfront investment of block producers.

Obviously, there are other consensus schemes achieve the same production of
blocks at far less expenses at the potential cost of centralization,
permissiveness, security or even scalability. It is outside the scope of this
article to go into further detail of alternatives to POW.

Either way, to overcome the need for a token, one can either keep the block
production in-house which makes the system centralized and probably private.
The alternative is to have block producers selected (and incentivised)
off-chain which makes it a permissive blockchain as it comes with a much higher
barrier-of-entry.

## Potential innovations

What's open for further experimentation is the incentive-structure provided to
block producers. While a *financial* compensation by means of token is an easy
route other rewards could come into play, such as

* participation in governance
* prestige
* discounts on fees
* no compensation at all (voluntarism)
* ...

## Conclusion

To conclude this article, a argument was made that public and permission-less
blockchains are open for anyone to participate in block production. Due to the
expenses required to take for operating a block producers, the blockchain has
to provide an incentive (often financially) to the operate to continue with
block production.
