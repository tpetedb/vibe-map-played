---
title: "Obsidian - Search"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Search

Search is a core plugin that finds text across the vault using search terms, operators, property queries and regular expressions. Results can be sorted, copied, and embedded in a note with a query code block.

## Facts

- Open with Ctrl+Shift+F (Windows/Linux) or Command+Shift+F (macOS); selected text becomes the search term
- Quote exact phrases ("star wars"), combine with OR and parentheses, negate with a leading hyphen: meeting -work
- Operators: file:, path:, content:, match-case:, ignore-case:, tag:, line:, block:, section:, task:, task-todo:, task-done:
- Property search: [aliases], [aliases:Name], [aliases:null], [status:Draft OR Published]
- Regular expressions go between forward slashes, for example /\d{4}-\d{2}-\d{2}/ (JavaScript flavour)
- Embed results with a query code block; Search settings offer Explain search term, Collapse results and Show more context

## Syntax

~~~
```query
embed OR search
```
~~~

## Try in five minutes

Press Ctrl/Cmd+Shift+F, search meeting -work and click Explain search term to read the breakdown, then try task-todo:call, and paste a query code block with one of the terms into a note to embed the results.

## Source

- [Search, Obsidian Help](https://help.obsidian.md/Plugins/Search)

Back to [[Obsidian features]]. Kind: core plugin.
