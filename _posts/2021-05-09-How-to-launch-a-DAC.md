---
layout: post
title: How to launch a DAC
tags: DAC blockchain genesis launch
comments: true
---

# Introduction

A decentralized autonomous company, as the name implies, should mimic the
behavior of a *company* in most (if not all) regards. This implies that a
blockchain that implements a DAC comes with a few components among which
are:

* **shareholders** that own and control the DAC
* **corporate governance** to allow decision making
* **services** that generate revenue for the company
* **employees** that work for the company and earn a salary

**Remark**: It's worth emphasizing that the terminologies used on an actual
blockchain should be reconsidered and reviewed by a legal term. The reason is
that "shareholder" as well as "employee" comes with legal implications that may
not necessarily fit the setup of the blockchain. For sake of simplicity, this
article will stick with the traditional notion, even though an actual
implementation might use terms like *token holders* and *workers* instead.

# Purpose

The purpose of this article is to present a way to launch a DAC while trying to
comply with securities as much as possible, or at least minimize liabilities for
all parties involved (legal review required!).

# Mimicking traditional startups

Here, we try to mimic how regular startups bootstrap a business. In particular,
we consider the blockchain/DAC to be the actual startup.

# The business idea

It all begins with a "business idea" that fills a need and can earn revenue. In
case of a DAC, this business idea most probably involves some digital
automation or *smart contract* that offers some service to people at a fee. What
particular service that might be is left open and is irrelevant for the rest of
the article, however, for sake of simplicity, we assume that the DAC will operated
an *exchange* for digital tokens (e.g. crypto currencies).

# The launch

In contrast to a regular company where a team gets together to work on the
project and share the stake among the founders, our case is different mostly,
due to legal reasons but also due to desires to establish a decentralized
ecosystem where *pre-mines* (e.g., founders setting aside some token at launch
time) is often considered harmful.

Instead, when launching a DAC, the team building the software will have to
commit their resources without the promises of a return of investment as they
compete for stake in the DAC in the very same way as everyone else. It's worth
mentioning a certain information asymmetry that might benefit the founders.

# Separation of Profits and Control

Similar to silent partnerships, the DAC should have a way to distinguish tokens
that grant voting control from tokens that offer a claim on the profit payouts.
It's also worth discussing the possibility to *vest* shares for certain periods
of time and/or have tokens expire.

# Assets and Tokens

Additionally to the profit-sharing and governance tokens, some
"cash-equivalent" token is required for people to pay the fee; a token that
ends has value outside the DAC and that ends up as profits in the DAC's
treasury.

A good candidate (depending on technical feasibility) would be Bitcoin, Ether
and others.

The technical implementation details around custody through gateway or
non-custodian "side-chains" are left open for another article intentionally.
What counts is that the DAC has a cash-equivalent token with value outside the
DAC itself.

# What's needed at launch

Already at the launch, the DAC need to have an operational governance setup. It
does not need a working product but decision making is required to ensure the
DAC develops towards a common goal, a *profitable* exchange.

To achieve this at the start, the DAC either needs to start with governing
bodies pre-filled (e.g. by the founding team), or some initial tokens have to
be distributed so that people can be voted into the governing bodies,
accordingly.

Now, with a working governance setup, the DAC can start hiring 3rd parties.

# The first hires

Obviously, there is no cash or cash equivalent available to the DAC as it, so
far, operates outside of the existing financial realm and outside the existing
crypto currency community.

Hence, the first hires can only be paid in "company stock" or "tokens" that
allow the first "employees" to claim profits generated from the DAC further
down the road.

This is quite similar to startups that often reduce their burn-rate by
replacing parts of the cash-salary by stock or stock options, with or without
vesting. Obviously, a DAC can do the same and after all, no money is involved
so this is all just moving numbers around at this point in time.

Obviously, the first hires are taking a huge risk as they essentially work for
(still worthless) tokens and only have expectations of future profits.
Considering tax laws in some countries, this setup might be discouraged
entirely as the worker might still owe tax on delivered work despite being paid
worthless tokens!

# Earning Money

At some point, the DAC will offer a service that goes life and will be used by
customers that pay a fee. This fee ends up in the treasury of the DAC as
revenue. At this point, governance can share the profits with token holders,
including the first hires.

# Raising Capital

At some point, the DAC might need to raise capital, e.g. for further
development, new business opportunities, additional hires or marketing.

Instead of asking hires to take on the financial risk, the DAC could decide to
instead "raise money" by selling profit-sharing token to investors, or the
public. An investor would pay cash-equivalent token (e.g. Bitcoin) into the
treasury and would get profit-reward token in return. This could take place
as an OTC deal, or using the internal exchange.

# Spending Cash and Cash-Equivalents

At this point, the DAC has cash at hand and can hire people without letting
them take the financial risk that the first hires had to take.

Additionally, the DAC does not need to dilute it's own shareholders for its
new hires but can instead spend the cash instead.

# Reaching Profitability

Obviously, the fun begins when the generated revenue outperforms the expenses
for hires (and block producers) as then, the funds in the treasury grow. This
allows for the DAC to buy back it's own shares, or to pay "dividends" to hits
shareholders.

# Going "public"

Additionally to *earning* revenue and sharing profits with token holders, the
other option would be to allow trading of those profit-sharing tokens for the
cash-equivalent token.

However, it is worth mentioning that those profit-earning tokens might tick all
the prongs of the Howey-Test and thus be declared a security token. Selling
them to non-accredited investors could involve risks. This particular aspect
needs a thorough investigation by a securities lawyer.

However, a few aspects work in the DAC's favour such as:

* there is no *common enterprise* that works to earn the profits - there are
  independent *hires* that work for the blockchain directly.
* there is no centralized issuance of the token, rather a set of governing
  bodies whose seats are filled by independent people and businesses

Additionally, further options to reduce legal risks in this regard are:

* requiring KYC for participants of the trade involving the profit-earning token
* registering the profit-earning token with the SEC
* as well as potential other means ..

# Conclusion

The above setup brings corporate setups to the blockchain. Even though there
are some unresolved questions about the legal implications and risks associated
with the sale of profit-generating tokens, the general setup itself appears
sound and worth pursuing.

## Room for Innovations

Required innovations for setup to work flawlessly are

* legal clarity (Wyoming, anyone?)
* bringing cash-equivalents into the DAC in a trust-less manner (the holy cosmos?)
