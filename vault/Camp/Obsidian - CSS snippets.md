---
title: "Obsidian - CSS snippets"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - CSS snippets

CSS snippets are small CSS files in the vault's configuration folder that change parts of the Obsidian interface without building a full theme, using Obsidian's CSS variables and the cssclasses property for per-note styling.

## Facts

- Settings > Appearance > CSS snippets > Open snippets folder, add a .css file, select Reload snippets, then enable the toggle
- On mobile, create a folder called snippets inside the configuration folder and add the file there
- Changes to an enabled snippet are applied when the file is saved; no restart needed
- CSS variables such as --h1-color to --h6-color recolour the six heading levels
- The cssclasses property assigns a class to a note, for example red-border styled by .red-border img
- Invalid CSS will not work; validate with the W3C CSS Validation Service

## Syntax

```
body {
  --h1-color: red;
  --h2-color: orange;
  --h3-color: yellow;
  --h4-color: green;
  --h5-color: blue;
  --h6-color: pink;
}
```

## Try in five minutes

Open Settings > Appearance > CSS snippets > Open snippets folder, save a headers.css that sets --h1-color: red on body, click Reload snippets and enable it; then give one note a cssclasses property with the value red-border and style .red-border img in the same file.

## In this vault

`.obsidian/snippets/feature-demo.css` colours the #feature tag yellow once enabled under Settings, Appearance, CSS snippets.

## Source

- [CSS snippets, Obsidian Help](https://help.obsidian.md/Extending+Obsidian/CSS+snippets)

Back to [[Obsidian features]]. Kind: extending.
