---
title: "Obsidian - Introduction to Bases"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Introduction to Bases

Bases is a core plugin that builds database-like views (table, list, cards, kanban, map) over the notes in a vault, reading data from their properties. A base is a YAML .base file with filters, formulas and views, and can be embedded in a note.

## Facts

- A base is saved as a .base file or embedded in a code block; the Bases syntax must be valid YAML (also read: Bases/Bases syntax.md and Bases/Views.md)
- View types: Table, List, Cards, Kanban, Map (Map requires the Maps plugin); community plugins can add layouts
- Without filters a base includes every file in the vault; filters combine and, or, not with statements like file.hasTag("book") or file.inFolder("Required Reading")
- Properties: note.price (or just price), file.name, file.mtime, file.tags, formula.ppu; a formula looks like ppu: "(price / age).toFixed(2)"
- Bases: Add view adds a view; the toolbar has View menu, Results, Sort, Filter, Properties, Search and New, plus Copy to clipboard and Export CSV
- Embed with `![[File.base]]` or `![[File.base#View]]`; the first view loads by default

## Syntax

```yaml
filters:
  and:
    - file.hasTag("tag")
views:
  - type: table
    name: "My table"
    limit: 10
    order:
      - file.name
      - file.ext
```

## Try in five minutes

Create a base, open the Filter menu and add the condition file.hasTag("book") in the advanced filter editor, show file.name and file.mtime as properties in the table view, then add a Cards view with Bases: Add view and embed it in a note with `![[Books.base#Cards]]`.

## In this vault

`Tech notes.base` next to this note is a base: a table of every note tagged #tech, with its date and tags.

## Source

- [Introduction to Bases, Obsidian Help](https://help.obsidian.md/Bases/Introduction+to+Bases)

Back to [[Obsidian features]]. Kind: core plugin.
