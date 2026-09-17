---
title: "Obsidian - Obsidian Flavored Markdown"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Obsidian Flavored Markdown

Obsidian Flavored Markdown combines CommonMark, GitHub Flavored Markdown and LaTeX with Obsidian's own extensions: wikilinks, embeds, block references, footnotes, comments, highlights, callouts and task lists. Markdown is not rendered inside HTML elements.

## Facts

- Supports CommonMark, GitHub Flavored Markdown and LaTeX
- Extensions: `[[Link]]` internal links, `![[Link]]` embeds, `![[Link#^id]]` block references, ^id block definitions, [^id] footnotes
- %%Text%% comments, ~~Text~~ strikethrough, ==Text== highlights, three backticks code blocks
- - [ ] incomplete task, - [x] completed task, > [!note] callouts, and tables
- Markdown such as **bold** or `code` is not processed inside <div>, <span>, <table> or any other HTML tag

## Syntax

```
[[Link]]
![[Link]]
![[Link#^id]]
^id
[^id]
%%Text%%
~~Text~~
==Text==
- [ ]
- [x]
> [!note]
```

## Try in five minutes

In one note write a line with ==highlight==, a %%hidden comment%%, a - [ ] task and a > [!note] callout, switch to Reading view to see which render, then wrap **bold** in a <div> and confirm it stays plain.

## Source

- [Obsidian Flavored Markdown, Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown)

Back to [[Obsidian features]]. Kind: format.
