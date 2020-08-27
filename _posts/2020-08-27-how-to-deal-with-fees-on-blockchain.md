---
layout: post
title: How to deal with fees on a blockchain
tags: blockchain fees
comments: true
percent-steem-dollars: 0
---

Apparently, everyone expects fees on the blockchain in order to prevent
spamming or even for sake of some *economical* aspect of the chain. If it
wasn't for the transaction fees, the blockchain could be cluttered with
worthless transactions making legit transfers impossible or expensive. But,
what would be the benefits of having free transactions, what the the drawbacks,
and can there be economics that make sense for a blockchain?

<!-- more //-->

Ok, well, **almost** everyone expects these fees. In fact, we've seen a few
(very few) blockchains that do not require a fee to be paid on every
transaction. Most prominently [Hive](https://hive.io) which requires to have
free transactions for posting and voting on social media content. Obviously, no
one would pay dime for that.

But let's start at the beginning: **Bitcoin** and why it needs those
transaction fees.

## Bitcoin Transaction Fees

As most of you know, Bitcoin transfers require a fee to be paid that goes to
the *miners* (also called block producers) as they are the ones that have
significant expenses to mine new blocks and include your transaction into the
ledger.

Couldn't there be no fees? Technically, there could and even from the
implementation, 0-fee transfers are possible, but - these days - quite rare and
that comes with a reason: **economics**.

### Bitcoin's Fee Market

Given that Bitcoin fees are **not fix** but can be picked arbitrarily (>0) by
the user, and given that the fees go to the miners that include your transaction
into a block, there is an incentive for miners to add those transactions into a
block that comes with the highest fees.

As you can see in the graphic below, these fees are quite significant and vary
wildly over time:

[![](/img/posts/20200827_141246.png#large bordered)](/img/posts/20200827_141246.png)
<small>
-- Credits: [Jochen Hönicke](https://jochen-hoenicke.de/queue/)
</small>

These is what is often referred to as **fee market**: The fee depends on the
free market - others that want to get their transaction into the block first.
Obviously, miners prefer those that pay a more fee so that it happens that you
may have to pay up to 50€ for a single transfer if a lot of competing
transactions are in the *fee pool*.

### Sustainability

The fee market in combination with the fact that blocks can only fit up to a
certain number of transactions (let's leave lightning and other L2 solutions
out of the equation for now) and because mining subsidy is reduced over time
(the *halvenings*), having people pay a fee is a sustainable (though maybe
expensive) solution to ensure Bitcoin's long-term existence.

### Conclusion

Bitcoin requires fees because its proof-of-work consensus scheme is expensive to
operate and requires an incentive to block producers to add your transaction.
This is fine for Bitcoin.

## "Free" Transactions

As mentioned above, Hive is an excellent example of when *free* transactions are
required and how to get them implemented. Essentially, the idea behind Hive is
to establish a social media platform where people can blog, comment, curate,
vote and build other stuff. All without paying for a transaction fee.

### Free as in "beer"?

In case of Hive, this comes with a catch: Users have to obtain a fraction of the
available *resource* in order to get a pro-rata share of the throughput on a
time-sharing basis, enforced by rate-limitation.

### Rate-Limitations

This idea was first envisioned by Daniel Larimer on his blog post [How to build
a Decentralized Application without
Fees](http://bytemaster.github.io/article/2016/02/10/How-to-build-a-decentralized-application-without-fees/)
where he made a comparison with renting:

<blockquote>
Renting vs Buying vs Timeshares

When someone owns a house they expect the right to use the house for free. If a
group of people buy a house together then each can expect the right to use the
house proportional to their percentage ownership in the house. A fee based
blockchain is like renting the house from its owners, whereas rate limiting is
like a timeshare among owners.
<small>-- Daniel Larimer</small>
</blockquote>

So, now we are at a point where users are rate-limited according to some metric.
In Steem, Hive and EOS, this metric is solely based on the *stake* that users
have in the system. Even more so, it has to be *locked* away where *unlocking*
consumes some real-world time (days).

The clear problem with this requirement is, that it comes as a barrier of
entry for businesses and power users who suddenly have to invest in the platform
they use for their business. Now, the supposedly *free* platform is not free
anymore - at least not to everyone equally. I intend to write a separate blog
post about the economics of this and why it cannot scale for EOS in the long
term.

### Scheduling

Another problem with rate-limitation (which Larimer solved in his blog post and
implementation) is the known issue in Computer Science known as [Job
Scheduling](https://en.wikipedia.org/wiki/Job_scheduler) where even those jobs
with little priority (think, little shares in the total resources) need to be
processed in a quick manner. As you can imagine, this becomes quite *complex*
very early. So, you get rid of one problem, but now have to fix another one.
In the early days of STEEM, the big problem was that the rate-limitation
and scheduler have been part of the *consensus* algorithm and couldn't be
tuned without doing a hard fork of the blockchain protocol.

Fortunately, the engineers figured out that removing it from the consensus and
**letting the block producers do the rate-limitation locally** is much more
efficient and easier to improve over time. Still, the rate-limitation is based
on the *locked* stake a users has in their wallet.

### Conclusion

As we've seen with this approach, it goes in the right direction. It offers free
interaction with the blockchain, enables micro-transactions, reduces friction
for users but, the way it is implemented so far, also adds a barrier of entry
for businesses that intend to bring in a huge user base, grow their smart
contracts quickly or for power-users who all require to obtain more and more
stake and lock it away. This comes at a cost which is contrary to the claim of
being *free*.

## Fixed Fees and an Economical Model for Sustainability

With the sections above, we've already introduced everything we need in order to
get to where we really want:

* tokenomics that allow to pay block producers,
* rate-limitation on the block producers side that allows to prevent spam
  and Sybil attacks and
* zero free transactions

What follows is purely imaginary - no blockchain exists (yet) that does it like
so. Consequently, this section could as well be called **this is where there is
room for innovation**.

What if I told you that the three items in the list above are **not** connected
to each other. Like, come on, why would rate-limitation be linked to the value
of a token that block producers get, or to the amount people have to pay for a
transaction?

You may think, there has to be a connection between having zero fees and the
tokenomics of the blockchain that pays the block producers, right? But, no, not
really. As described in an [earlier blog post]({% post_url
2020-08-21-blockchains-and-the-need-for-a-token %}), there only needs to be
*some* sort of compensation to block producers, but not necessarily a financial
reward. As we learned in this post, the reward has to depend on the efforts
required in order to become block producer, as proof-of-work requires plenty of
financial up-front investment. So, the innovation has to also improve on the
consensus scheme - luckily there are plenty to chose from.

Further, rate-limitation is available and it is pretty much known on how to deal
with this. Plus, with Hive, we've learned that rate-limitation can be
implemented on the block  producer side and need not be part of the consensus
scheme. This allows to be flexible long-term.

Depending on how you want your tokenomics to work, you may decide that fees have
to apply at some point - in particular if you want a financial reward for block
producers. But does this financial reward have to come from transaction fees? I
would say, no. Alternatively, one could think of a blockchain to provide
services, such as p2p-payments, trading, liquidity, reputation which could come
with a price tag. Or even easier.

There's an even easier example: Why not have a fixed rate-limitation that you
can overcome with you pay 10$ worth of token per month to some treasury in order
to unlock your flat rate?
