---
title: "Obsidian - File recovery"
date: 2026-09-17
tags: [tech, obsidian]
---
# Obsidian - File recovery

File recovery is a core plugin that saves complete snapshots of notes at regular intervals so you can restore or copy an earlier version after an accidental deletion or unwanted change. It is not a full backup solution.

## Facts

- By default snapshots are at least 5 minutes apart and kept for 7 days; both are set under Settings > Core plugins > File recovery
- Recover: Settings > File recovery > Snapshots > View, type the file name, pick a snapshot, then Copy or Restore; Show changes displays the diff
- Snapshots live in the global settings outside the vault and store the absolute path, so a moved vault may lose access to them
- Snapshots do not sync between devices, even with Obsidian Sync
- Only .md and .canvas files can be restored
- Clear history > Clear irreversibly deletes all snapshots

## Try in five minutes

Edit a note, wait a few minutes, edit it again, then open Settings > File recovery > Snapshots > View, type the note name, toggle Show changes to compare the two snapshots and use Copy to paste the older text into a new note.

## Source

- [File recovery, Obsidian Help](https://help.obsidian.md/Plugins/File+recovery)

Back to [[Obsidian features]]. Kind: core plugin.
