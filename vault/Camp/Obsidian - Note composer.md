---
title: "Obsidian - Note composer"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Note composer

Note composer is a core plugin that merges two notes or extracts a selection into another or a new note, updating links as it goes, with an optional template for the new content.

## Facts

- Commands: Note composer: Merge current file with another file... and Note composer: Extract current selection...
- Merging adds a note to another, removes the first, and updates all links to the merged note
- Enter adds at the end, Shift+Enter at the start, Ctrl+Enter (Cmd+Enter on macOS) creates a new note
- In Editing view, right-click selected text and choose Extract current selection...
- By default the extracted text is replaced with a link; settings can embed the destination note or leave nothing behind
- Template file location supports {{content}}, {{fromTitle}}, {{newTitle}} and {{date:FORMAT}}

## Try in five minutes

Select a paragraph in a note, right-click and choose Extract current selection..., type a new note name and press Ctrl/Cmd+Enter; check that the paragraph moved and a link to the new note was left behind.

## Source

- [Note composer, Obsidian Help](https://help.obsidian.md/Plugins/Note+composer)

Back to [[Obsidian features]]. Kind: core plugin.
