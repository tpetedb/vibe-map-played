---
title: "Obsidian - Tags"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Tags

Tags are keywords or topics that help you find notes quickly. You write them inline with a hash sign or in the tags property, nest them with slashes, and find them with the tag search operator or the Tags view.

## Facts

- Create a tag by typing # followed by a keyword, for example #meeting
- In YAML the tags property must always be formatted as a list
- Search with the tag operator, for example tag:#meeting; tag:inbox also matches nested tags such as #inbox/to-read
- Nested tags use forward slashes: #inbox/to-read and #inbox/processing
- Tags: Show tags in the Command palette opens the Tags view
- Tags can't contain spaces and need at least one non-numerical character (#1984 is invalid, #y1984 is valid); they are case-insensitive

## Syntax

```
---
tags:
  - recipe
  - cooking
---
```

## Try in five minutes

Add #inbox/to-read to one note and #inbox/processing to another, then open Search and enter tag:inbox to confirm both notes appear; run Tags: Show tags to see them nested under inbox.

## Source

- [Tags, Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Tags)

Back to [[Obsidian features]]. Kind: editing.
