---
title: "Obsidian - Templates"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Templates

Templates is a core plugin that inserts pre-defined text from a template folder into the active note at the cursor, replacing variables such as the title, date and time.

## Facts

- Set the folder under Settings > Core plugins > Templates > Template folder location
- Variables: {{title}}, {{date}} (default format YYYY-MM-DD), {{time}} (default format HH:mm)
- Format strings use Moment.js tokens after a colon, for example {{date:YYYY-MM-DD}}
- Commands: Templates: Insert template, Templates: Insert current date, Templates: Insert current time; Insert template is also in the ribbon
- Template properties are merged into the note's existing properties on insert
- Edit templates in Source mode, because the Properties in document panel in Live Preview can overwrite unquoted template variables

## Syntax

```
---
topic: 
date: "{{date}}"
course: 
tags:
  - studies
---

# {{title}}

## Key Concepts
```

## Try in five minutes

Create a folder named Templates and set it as the Template folder location, add a note there with # {{title}} and a line Created {{date:YYYY-MM-DD}} {{time}}, then open a new note and run Templates: Insert template.

## In this vault

`_templates/obsidian/Feature note.md` is a template with {{title}}, {{date}} and {{time}}; point Settings, Templates at `_templates`.

## Source

- [Templates, Obsidian Help](https://help.obsidian.md/Plugins/Templates)

Back to [[Obsidian features]]. Kind: core plugin.
