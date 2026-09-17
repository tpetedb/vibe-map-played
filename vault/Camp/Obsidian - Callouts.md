---
title: "Obsidian - Callouts"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Callouts

Callouts are blockquotes with a type identifier on the first line that render as coloured boxes with an icon, for extra content that does not break the flow of a note. They take custom titles, fold, nest, and can be styled with CSS.

## Facts

- Add [!info] to the first line of a blockquote, where info is the type identifier; the identifier is case-insensitive
- The Insert callout command inserts a default [!note] callout, or wraps the selected text in one
- Add + or - directly after the type identifier to make it foldable; - starts collapsed
- Supported types: note, abstract, info, todo, tip, success, question, warning, failure, danger, bug, example, quote; unsupported types fall back to note
- Aliases: summary and tldr (abstract), hint and important (tip), check and done (success), help and faq (question), caution and attention (warning), fail and missing (failure), error (danger), cite (quote)
- Custom callouts in a CSS snippet: .callout[data-callout="custom-question-type"] with --callout-color and --callout-icon

## Syntax

```
> [!info] Here's a callout title
> Here's a callout block.
> It supports **Markdown**, [[Internal link|Wikilinks]], and [[Embed files|embeds]]!
> ![[Engelbart.jpg]]
```

## Try in five minutes

In a note, run Insert callout from the Command palette, change it to [!tip] with a custom title, make it foldable by adding - after the identifier, then nest a [!example] callout inside it.

## Source

- [Callouts, Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Callouts)

Back to [[Obsidian features]]. Kind: editing.
