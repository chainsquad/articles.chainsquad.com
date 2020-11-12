---
layout: post
title: If I was asked to do a "fair launch"
tags: genesis fair blockchain launch
comments: true
---

Let's assume for a moment one of my clients approached me and asked for a "fair
blockchain launch", how would I do that? What needs to be considered? Where are
the technical, legal, social challanges? What does it even mean?

<!-- more -->

## Blockchain Launch

As many of you know, *launching* a blockchain is quite a delicate aspect of
blockchain technologies. Not only do you have to have your technology stack as
far together as you can produce blocks and not break your own consensus rules
by some bugs, you also need to set in stone various aspects of your entire
setup:

* initial distribution of monetary value (i.e., coins)
* initial distribution of voting rights (i.e., governance tokens)
* consensus scheme
* initial block producers
* *and many other things*

In particular the distribution of coins/tokens is set in stone in the so called
*genesis block*, the *first block* of your blockchain that will live on in your
system for eternity. Hence, delicate.

## Considerations for "fairness"

IMHO

> A fair launch can only exist in so far as you ignore information asymmetry.

This means that no matter how you launch, there will always be people (the
insiders) that worked on the blockchain and have an advantage over everyone
else as they built it. This advantage can often be used to gain some additional
benefit out of the system.

What might look unfair at first is often on purpose in order to avoid legal
trouble. Here's an example:

### Proof of Work

Ok, let's get back one step. The term "fair launch" is quite opaque and can
mean many things especially when your blockchain comes with a governance token.

Initially, a *good* launch was associated with:

* Proof-of-work
* Absence of a pre-mine

thus, everyone has had the same chances to join right after launch. Soon, it
turned out, smart engineers would automate launches of new coins and throw a
ton of compute power onto a chain right after launch (much like a
*ninja-mine*). Hence, soon after the launch of a POW chain, the it was
attrition warfare, whoever had most resources, got more our of it.

Hardly a fair launch.

Arguable, Bitcoin is special with that regard, as back in the time when Bitcoin
launched, too few people took it serious and the one that did, wouldn't throw
thousands of dollars worth of compute power onto it. Bitcoin grew gradually.
Still, Satoshi, the creator, is estimated to hold roughly a Million Bitcoin.

### STEEM

The Steem blockchain was developed in Stealth. No one outside Steemit Inc. knew
about what is being built. Not even the launch it self was associated with
Steemit Inc. or the individuals involved. There was an anonymous, new account
on bitcointalk, called `thereverseflash` that would make the announcement that
a new project has come to life and where the source code was. Nothing more.

Initially, STEEM was in fact a POW chain where blocks could be mined through
hash-power.

This was the single-most-important information asymmetry between Steemit Inc.
(the insiders) and the rest (the outsiders).

Why would they do their launch in such a way? To avoid trouble with the SEC
while still securing funding for future development without getting into the
corner of *selling unregistered securities to US-citizens*. As STEEM went live
and people started to understand its implications, a market established that
would give STEEM tokens value and voila, funding for the future secured as
Steemit Inc. controlled a massive percentage of the stake. This is what is
often referred to as a *ninja mine*.

Hardly a fair launch.

### YFI

The developer of the YFI/yearn.finance tools has made the decision of not
securing any stake in the YFI token when launching and instead give it all out
to *the community*.

> With this, $YFI has had the most favorable supply distribution for a DeFi
> Community that’s ever been seen with everyone that earned tokens having
> undertaken the same risks with all the information freely available to them.
> This fair launch is reminiscent of early Bitcoin mining, as nobody had a head
> start–not even Andre, and the only way to acquire it was to earn (mine) it.
> Much like early bitcoin miners, early YFI yield farmers have self-selected as
> those most in tune with DeFi, ensuring a passionate and involved community.
(from [insights.deribit.com](https://insights.deribit.com/market-research/yfi-a-tale-of-fair-launch-governance-and-value/))

The idea was (and still is) that the newly minted supply has to be **earned**,
e.g.  through

* staking yCRV and receiving some sort of *dividend*
* providing liquidity
* participating in governance

As the crypto community understood the concept, YFI rose significantly, as well
as its trading volume.

However, was this a *fair launch*? The creators of YFI have worked hard and put
their sweat into building these pieces of software, yet they have not received
any benefit from it. On the other hand, *yield harversting* became a thing
dozends of heavy *investors* entered the game of earning YFI for their staked
token. The rich get richer and those that made it all possible are left behind.

> It's completely lopsided. No cryptocurrency is going to succeed where
> investors outnumber developers so heavily.

Hardly a fair launch. However, one might argue that the supply has been *well
distributed* (by some metric).

## Conclusions

Even today, we have not seen a "fair launch" by very strict definition.
However, we have seen setups that resulted in quite a good distribution of
stake (even including Bitcoin).

Ultimately, in our view, every launch of a new blockchain needs to particularly
investigate who to best benefit from the technology in combination with the
distribution of stake and thus control over the system. The most important question
will undoubtably be **who will get to control the blockchain**: Will it be the
developers, some investors, or those that use the platform?

## Room for Innovations

Obviously, the entire question opens up a huge playing field where parameters
like, total stake, initial distribution, airdrops, but also dilution/inflation
and "earning stake" as well as how the stake can be used for receiving
benefits, or profits, or rather grant access to governance. All these questions
need to be individually balanced for each particular blockchain application.

> Let the games begin.
