---
layout: post
title: What are Smart Contracts and why they have nothing to do with Turing Completeness and Scriptability
tags: core smart contracts
comments: true
---

Recently, I had a great conversation with Nathan Hourt, a brilliant backend
developer that I love working with. We are on the same wave length. So it
shouldn't surprise you that we came to similar conclusions on an item that is
often presented misleadingly in the public: The different aspects of *smart
contracts*, *Turing completeness* and *scriptability*.

<!--more-->

Before I start, let's setup a glossary 📖 and clarify these terms.

## Turing Completeness

This is a term used in computer-science and is called after Alan Turing - the
guy that broke Enigma encryption in WW2. From
[wikipedia](https://en.wikipedia.org/wiki/Turing_completeness) we get this

<blockquote>
In computability theory, a system of data-manipulation rules [...] is
said to be <strong>Turing-complete</strong> [..] if it can be used to
simulate any Turing machine. This means that this system is able to recognize
or decide other data-manipulation rule sets. Turing completeness is used as a
way to express the power of such a data-manipulation rule set.
</blockquote>

To break this down, it means that Turing-Complete languages can be used to do
**anything** that is in the reach of a computer. Not surprising, pretty much any
programming language is Turing-complete, including
[LaTex](https://stackoverflow.com/questions/2968411/ive-heard-that-latex-is-turing-complete-are-there-any-programs-written-in-late),
[Minecraft](https://gaming.stackexchange.com/questions/20219/is-minecraft-turing-complete), [Magic: The Gathering](https://arxiv.org/abs/1904.09828),
[CSS3](https://github.com/elitheeli/stupid-machines/tree/master/rule110), and
even Super Mario World
([more](https://beza1e1.tuxen.de/articles/accidentally_turing_complete.html)).

Interestingly, Bitcoin's [Script](https://en.bitcoin.it/wiki/Script) language
is capable of building a [dual stack push down
automata](https://en.wikipedia.org/wiki/Pushdown_automaton) and is thus capable
of computing values in a system compatible with that of Godel’s logic system.
While it is not a Turing machine, it is as powerful.

## Scriptability

Scriptability - I am not sure this is a real English word - describes the
ability to get a script installed on the blockchain easily. In essence, all
major Smart-Contract platforms these days allow any user to deploy any contract
onto their blockchain. 

Ethereum contracts are written in Solidity, EOS contracts in Webassambly, and
other blockchains use NodeJS or even Python to allow users to get *their own
scripts* installed on the blockchain.

In fact, even Bitcoin allows scripting - in fact, their stack-based language
for this is called [Script](https://en.bitcoin.it/wiki/Script).

Other blockchain systems do not provide Scripting capabilities, such as
[Hive](https://hive.io) yet they provide features that add just enough
flexibility to have a growing smart-contract community there as well. In a
sense, scripts would run off-chain and are fed with information that is stored
(and ordered) by the blockchain.

## Smart Contracts

Personally, I don't like this term. It's difficult to grasp what it really
means and no concise definition exists. In short, everyone thinks about
something else when they hear smart contracts.

To try to bring some meaning to this term that many would agree on, a smart
contract provides means to take some sort of action on participants according
to the terms set forth on deployment of said contract.

Usually, smart contracts are written in software language (Solidity, C++, ...)
and quite technical but they all have in common that the terms (**what is
executed under which conditions**) is provided to the parties prior to them
**approving** them.

What makes smart contracts (in particular in combination with Scriptablity)
particularly dangerous are *bugs* and *misunderstandings*. For that reason,
millions have been *hacked* or where lost as contracts apparently didn't
*behave* as *expected*. In fact, there are dozens of arguments about whether
*code is law* or not. Just a primer on the scope of this issue:

* [The DAO Hack](https://medium.com/@ogucluturk/the-dao-hack-explained-unfortunate-take-off-of-smart-contracts-2bd8c8db3562)
* [Incident with non-standard ERC20 deflationary tokens](https://medium.com/balancer-protocol/incident-with-non-standard-erc20-deflationary-tokens-95a0f6d46dea)
* [Uniswap/Lendf.Me Hacks: Root Cause and Loss Analysis](https://medium.com/@peckshield/uniswap-lendf-me-hacks-root-cause-and-loss-analysis-50f3263dcc09)
* [Ether Collateral Bug Disclosure](https://blog.synthetix.io/bug-disclosure/)
* [Parity Multi-Sig Library Self-Destruct](https://www.parity.io/a-postmortem-on-the-parity-multi-sig-library-self-destruct/)
* [The biggest smart contract hacks in history or how to endanger up to US $2.2 billion](https://medium.com/solidified/the-biggest-smart-contract-hacks-in-history-or-how-to-endanger-up-to-us-2-2-billion-d5a72961d15d)
* ...

To make matters worse, most smart contracts are not meant of ordinary people.
That's because they are written in a non-natural language that obfuscates or at
least disconnects the intend from the written.

## Ricardian Contracts

In order to make smart contracts *easier* to understand, Ian Grigg developed
[Ricardian Contracts](https://en.wikipedia.org/wiki/Ricardian_contract).
Basically, these are standard smart contracts, written in computer slang, but
extended by a legal document crafted by a lawyer. Unfortunately, not much is
known about the applicability as they are only rarely used.

I am not a lawyer, but I can think of a practical problem with these: Source of
Truth. In case of a disagreement of code and legal word, how would one tell
this to the blockchain?  A curt may rule that the software is wrong and needs
fixing, but the software may already have executed and the funds are gone. Go
after people in the real world? what was the advantage of using a blockchain
then?

## Room for innovation

As with all things in tech, there is some room left for innovations. In this
case, I would be interested to see why people consider it a given that smart
contracts are executed by the blockchain and not the user.

If you think of a smart contract like a *state-machine* that eats data and
poops some outcome while going to some other state, why do we need the state
and the outcome to be on the blockchain? A **deterministic** state-machine
would always return identical outcome and undergo the same state transitions
when provided the same input data again.
