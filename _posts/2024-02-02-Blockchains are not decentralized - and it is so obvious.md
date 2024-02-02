---
layout: post
title: Blockchains are not decentralized - and it is so obvious
tags:
  - blockchain
comments: false
---
In recent discussions about blockchain technology, there's been a growing emphasis on its decentralized nature, often hailed as a panacea for various problems. However, a critical examination reveals a fundamental oversight in this perception, particularly concerning popular blockchains like Bitcoin and Ethereum. The central issue stems from the fact that these blockchains are, paradoxically, centralized in a crucial aspect: **they operate as singular entities**.

# Bitcoin, Ethereum, Solana, Ripple, ...

The core of this argument revolves around the idea that despite being decentralized in operation – with no single entity controlling the network – Bitcoin and Ethereum maintain a centralization of structure. This singular nature of the blockchain becomes evident when we compare it to global financial technology (FinTech) applications, where decentralization takes a different form.

Consider major financial processors such as PayPal, Strike, and international banks. These entities are distributed globally, providing a robust system that ensures continuous service availability. For instance, if servers in the United States encounter issues, the European market remains largely unaffected because the system's distribution allows for regional autonomy. This resilience in the face of localized disruptions is a critical advantage for global commerce, ensuring minimal impact on international transactions.

In contrast, blockchains like Ethereum or Bitcoin present a different scenario. These platforms, while decentralized in terms of nodes and miners, centralize all users onto a single ledger. This arrangement inherently creates a 'one-size-fits-all' playing field, where every participant is bound to the same blockchain. While this uniformity offers unique value propositions, such as transparency and security, it also introduces a significant vulnerability: the risk of a single point of failure.

This vulnerability is not just theoretical but a practical concern. If the blockchain encounters a systemic problem, such as a technical flaw or a massive cyberattack, the repercussions are global and instantaneous. Every user, transaction, and application relying on that specific blockchain would be affected simultaneously, leading to potential disruptions in global financial operations. In essence, what is designed to be a strength of these blockchains – their unified structure – can also be their Achilles' heel.
# Options

Other ecosystems are smarter than that, they leverage the technology to allow application-specific blockchains, in short *app-chains*. If they break, the app is broken, all other apps, however, run their own blockchain and are independent. The [Cosmos Network](https://cosmos.network) with the [Cosmos SDK](https://v1.cosmos.network/sdk) are a prime example of how to deal with it. Congratulations.