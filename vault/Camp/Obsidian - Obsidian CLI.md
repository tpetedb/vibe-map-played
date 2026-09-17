---
title: "Obsidian - Obsidian CLI"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - Obsidian CLI

Obsidian CLI controls a running Obsidian app from the terminal, for scripting, automation and agent tooling. It offers single commands and a TUI, covering files, daily notes, search, tasks, properties, plugins, bases, sync, publish and developer commands.

## Facts

- Requires the Obsidian 1.12.7+ installer; enable under Settings > General > Command line interface; the app must be running
- obsidian help runs a single command; obsidian alone opens the TUI with autocomplete, history and Ctrl+R reverse search
- Parameters are parameter=value (quote values with spaces), flags such as open and overwrite take no value, --copy copies the output
- Examples: obsidian daily, obsidian daily:append content="- [ ] Buy groceries", obsidian search query="meeting notes", obsidian create name="Trip to Paris" template=Travel
- vault=<name> must be the first parameter; file=<name> resolves like a wikilink, path=<path> needs the exact path from the vault root
- Developer commands: devtools, plugin:reload id=my-plugin, dev:screenshot path=screenshot.png, eval code="app.vault.getFiles().length"

## Syntax

```
# Open today's daily note
obsidian daily

# Add a task to your daily note
obsidian daily:append content="- [ ] Buy groceries"

# Search your vault
obsidian search query="meeting notes"

# List all tags in your vault with counts
obsidian tags counts
```

## Try in five minutes

Turn on Command line interface under Settings > General, restart your terminal, then run obsidian tags counts, obsidian daily:append content="- [ ] Try the CLI" and obsidian tasks daily to see the new task listed.

## Source

- [Obsidian CLI, Obsidian Help](https://help.obsidian.md/Extending+Obsidian/Obsidian+CLI)

Back to [[Obsidian features]]. Kind: extending.
