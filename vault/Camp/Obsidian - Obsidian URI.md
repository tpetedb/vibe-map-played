---
title: "Obsidian - Obsidian URI"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Obsidian URI

Obsidian URI is a custom obsidian:// protocol that triggers actions from outside the app, such as opening or creating a note, opening the daily note, a unique note, a search or the vault manager, for automation and cross-app workflows.

## Facts

- Format: obsidian://action?param1=value&param2=value; actions are open, new, daily, unique, search, choose-vault
- obsidian://open?vault=my%20vault&file=my%20note opens my note.md in the vault my vault; vault can be the name or the 16-character vault ID
- obsidian://new?vault=my%20vault&name=my%20note creates a note; optional content, clipboard, silent, append, overwrite parameters
- paneType=tab, paneType=split or paneType=window controls where the note opens
- Values must be URI encoded: / becomes %2F and spaces %20; Note%23Heading opens a heading, Note%23%5EBlock a block
- Shorthand obsidian://vault/my vault/my note; x-success and x-error support x-callback-url

## Syntax

```
obsidian://action?param1=value&param2=value
obsidian://open?vault=my%20vault&file=my%20note
obsidian://new?vault=my%20vault&name=my%20note
obsidian://daily?vault=my%20vault
obsidian://search?vault=my%20vault&query=Obsidian
```

## Try in five minutes

Find your vault name, then paste obsidian://new?vault=YOUR%20VAULT&name=URI%20test&content=Hello%20World into your browser's address bar (encode spaces as %20) and confirm Obsidian opens a new note called URI test.

## Source

- [Obsidian URI, Obsidian Help](https://help.obsidian.md/Extending+Obsidian/Obsidian+URI)

Back to [[Obsidian features]]. Kind: extending.
