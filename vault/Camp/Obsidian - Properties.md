---
title: "Obsidian - Properties"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Properties

Properties store structured data about a note, such as text, links, dates, checkboxes and numbers, as YAML at the top of the file. Each property name has one type across the vault, and Obsidian ships default properties like tags, aliases and cssclasses.

## Facts

- Add a property with the Add file property command, the Cmd/Ctrl+; hotkey, or by typing --- at the very beginning of a file
- Property types: Text, List, Number, Checkbox, Date, Date & time, Tags
- Default properties: tags, aliases, cssclasses; Obsidian Publish also uses publish, permalink, description, image, cover
- Internal links in properties must be surrounded with quotes, for example link: "`[[Episode IV]]`"
- Dates are stored as 2020-08-21 and date & time as 2020-08-21T10:30:00
- Settings > Editor > Properties in document: Visible (default), Hidden, or Source

## Syntax

```
---
title: A New Hope
link: "[[Episode IV]]"
url: https://www.example.com
---
```

## Try in five minutes

Open a note, press Cmd/Ctrl+; and add a property named status with the value draft, then add a date property and a checkbox property; switch Settings > Editor > Properties in document to Source to see the YAML that was written.

## Source

- [Properties, Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Properties)

Back to [[Obsidian features]]. Kind: editing.
