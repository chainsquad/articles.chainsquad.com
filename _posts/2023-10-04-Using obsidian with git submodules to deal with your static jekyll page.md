---
layout: post
title: Using obsidian with git submodules to deal with your static jekyll page
tags:
  - jekyll
  - chainsquad/articles
comments: true
---
I have recently started playing around with [obsidian](https://obsidian.md) for my personal knowledge-base and **love** it. Not only does it
* support markdown for note taking
* it also allows to build PDFs using pandoc
* let's you create charts using mermaid
* is highly customizable with plugins and CSS
Among other things.

# Obsidian git
One nice feature is that you can use *git* as a means to backup your data into your remote origin. The plugin also supports submodules, so I thought, let's see if I can bring my jekyll pages in and manage my articles via Obsidian.

To do so, you need to

1. install Obsidian-git
2. enable submodules in obsidian-git
3. have your vault in a git repo
4. `git submodule add github:username/jekyll-page External/jekyll-page
5. modify your articles
6. commit your changes and push
7. 🎉