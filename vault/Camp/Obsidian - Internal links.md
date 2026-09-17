---
title: "Obsidian - Internal links"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Internal links

Internal links point from one note to another note, attachment or file in the vault, in Wikilink or Markdown format. You can also link to a heading or a block inside a note and change the display text. Obsidian updates links when you rename a file.

## Facts

- Wikilink format: `[[Three laws of motion]]`; Markdown format: [Three laws of motion](Three%20laws%20of%20motion), with spaces URL encoded as %20
- Type [[ in the editor to autocomplete a link, or run Add internal link from the Command palette; select text first to turn it into a link
- Link to a heading with `[[About Obsidian#Links are first-class citizens]]`; `[[## team]]` searches headings across the vault
- Link to a block with `[[2023-01-01#^37066d]]`; add a space and ^quote-of-the-day at the end of a paragraph for a readable identifier (Latin letters, numbers, dashes only)
- Change the display text with a vertical bar: `[[Example|Custom name]]`; use an alias instead for a reusable name
- Settings > Files and links > Automatically update internal links keeps links working on rename; disable Use `[[Wikilinks]]` to generate Markdown links

## Syntax

```
[[Three laws of motion]]
[[Projects/Three laws of motion]]
[[About Obsidian#Links are first-class citizens]]
[[2023-01-01#^quote-of-the-day]]
[[Example|Custom name]]
```

## Try in five minutes

Create a note, type `[[ and pick another note to link it, then add ^my-block at the end of a paragraph and link to it from a third note with [[Note#^my-block]]`. Rename the first note and check that the links updated.

## Source

- [Internal links, Obsidian Help](https://help.obsidian.md/Linking+notes+and+files/Internal+links)

Back to [[Obsidian features]]. Kind: linking.
