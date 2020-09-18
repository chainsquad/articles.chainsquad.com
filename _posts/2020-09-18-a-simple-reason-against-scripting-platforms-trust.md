---
layout: post
title: A simple reason against Turing-complete scripting in Smart Contracting Platforms
tags: scriptable smart contracts
comments: true
---

In this short but concise article, I would like to give food for thought on
smart contracting platforms that come with a **Turing-complete scripting
language**.

It all breaks down to one thing: **trust**.

## The origin: Bitcoin

Let's begin at the origins of the blockchains space - Bitcoin. The core value
proposition of bitcoin - among others - is that it replaces the middleman and can
be easily verifiable.

So we got that covered. How about the **trust** thing? Isn't Bitcoin
*trust-less*? Of course it is **not**. The requirement for trust doesn't just
disappear, but in this case, it moves over from the middleman to a piece of
software, a contract written in code.

Why is this a thing? Bitcoin enables two parties to transact with each other
direct. They do **not need to trust a middleman**. This is important and
middlemen are technically capable of **changing their mind**, while a contract
on Bitcoin **cannot**.

So, in short, we trust a contract written in code and we know that it cannot
change it's mind. But how am I supposed to trust a piece of code? Obviously, I
can trust it if:

1. I can read the code, and
2. I can understand what it does.

To make things simple: There are people that can tick 1.) and there are plenty
of people (the rest) that cannot tick either of both. Technically, we cannot
easily reach 100% certainty about 2) - and I am not going into the technical
details here - as the *behavior* of code isn't trivially verified.

So, in case of Bitcoin, who do I trust then? In my opinion, the entire trust
lies into the foundation of the code basis and the understanding and
expectations of this code base being properly reviewed and tested. Apparently,
this is the case with bitcoin-core as there are hundreds of active developers and
thousands of people reviewing changes proposed to the code.

To conclude, we trust Bitcoin's code basis to do as we expect it to do and know
for sure that it doesn't change its behavior.

## Trust with Smart Contracting Platforms

So, from where we got - middlemen moving funds from left to right - we got to
experience improved trust by putting something in between that doesn't change
its mind and that *behaves*.

With Turing-complete Scripting and Smart contract platforms that allow anyone
to deploy code onto a blockchain, things look differently. Now, there is not
**one** major development community that supervises and reviews the code and
its behavior. Instead, we often see contracts being deployed by
*script-kiddies* that don't have the necessary skills or funds to have these
contracts properly reviewed by experts. And even then, the reviewing resources
are less than compared to a contract that is part of layer-1 (like in bitcoin).

What makes matter worse is that the behavior of the code might differ from the
expectations as we have seen from the great blow of "The DAO".

In short, we've been at a stage where we needed to **trust a huge community of
developers** and am moving slowly towards **trusting a smaller set of contract
developers**.

## Room for Innovations

If there was a way to bring both worlds together by combining the flexibility
of Turing-complete scripting with quality assurance due to hundreds of
developers reviewing your code, that would be wonderful.
