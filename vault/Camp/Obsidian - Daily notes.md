---
title: "Obsidian - Daily notes"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Daily notes

Daily notes is a core plugin that opens today's note or creates it if it does not exist, for journals, to-do lists or daily logs. It can use a template and a custom folder, and date properties become links to daily notes.

## Facts

- Open with the Open today's daily note ribbon icon, the Command palette command, or a hotkey for that command
- By default the note is an empty note named after today's date in YYYY-MM-DD format
- New file location in the plugin options changes the folder; Template file location sets a template
- A Date format such as YYYY/MMMM/YYYY-MMM-DD creates automatic subfolders like 2023/January/2023-Jan-01
- With the plugin enabled, a date property in any note becomes a clickable link to that day's daily note in Live Preview

## Syntax

```
# {{date:YYYY-MM-DD}}

## Tasks

- [ ]
```

## Try in five minutes

Create a note called Daily template with the heading # {{date:YYYY-MM-DD}} and a Tasks list, set it as Template file location under Daily notes, then run Open today's daily note and add a task.

## In this vault

`_templates/obsidian/Daily.md` is a daily note template; set it as the Daily notes template and the folder to `Daily`.

## Source

- [Daily notes, Obsidian Help](https://help.obsidian.md/Plugins/Daily+notes)

Back to [[Obsidian features]]. Kind: core plugin.
