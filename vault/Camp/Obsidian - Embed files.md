---
title: "Obsidian - Embed files"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Embed files

Embedding shows a file's content inline in a note and keeps it up to date with the source. An exclamation mark before an internal link embeds notes, headings, blocks, images, audio, PDFs, canvases, lists and search results.

## Facts

- Add ! in front of an internal link: `![[Internal links]]`; any accepted file format can be embedded
- Embed a heading or block: `![[Internal links#^b15695]]`
- Resize images with |640x480, or width only to scale proportionally: `![[Engelbart.jpg|100]]`
- PDFs: `![[Document.pdf#page=3]]` opens a page, `![[Document.pdf#height=400]]` sets the viewer height
- Embed a canvas with `![[My canvas.canvas]]`; embedded canvases show shapes but not card text
- On desktop, drag and drop a supported file into a note to embed it

## Syntax

```
![[Internal links]]
![[Internal links#^b15695]]
![[Engelbart.jpg|100x145]]
![[Document.pdf#page=3]]
![[My canvas.canvas]]
```

## Try in five minutes

Add ^my-list-id on its own line after a bullet list in one note, then in another note write `![[My note#^my-list-id]]` and watch the list appear; edit the source list and confirm the embed updates.

## Source

- [Embed files, Obsidian Help](https://help.obsidian.md/Linking+notes+and+files/Embed+files)

Back to [[Obsidian features]]. Kind: linking.
