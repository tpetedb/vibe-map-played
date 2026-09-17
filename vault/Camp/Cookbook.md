---
title: "Cookbook"
date: 2026-09-17
tags: [recipe]
---
# Cookbook

Recipes for a Data engineer. Each one is a prompt you paste into your provider, a definition of done, and the workstream it belongs to. Every persona has its own set; switch with `vibe persona <id>`.

## Two-file task pattern
Workstream 3. A pipeline task as a .py plus a .yaml sidecar with tests.

```text
Create tasks/orders_silver.py and tasks/orders_silver.yaml (source, target, schedule, owner). The task reads bronze from DuckDB, dedupes, writes silver. pytest with a fixture CSV.
```

**Done when:** uv run pytest is green and the yaml validates.

## Schema drift guard
Workstream 4. A hook that refuses a commit when a CSV header changes.

```text
Write a pre-commit style Claude Code hook (PostToolUse on Edit and Write) that compares data/*.csv headers to schema.json and prints the diff. Show me the settings.json block.
```

**Done when:** Renaming a column produces a loud message.

## Nightly run report
Workstream 8. Headless agent summarises last night's runs into the vault.

```text
Write a script that runs the provider in print mode over workspace/data/pipeline_runs.csv and writes vault/Camp/Runs.md with a table and one paragraph. Schedule it at 07:00.
```

**Done when:** Runs.md is updated by the schedule, not by you.

Back to [[Your field]] · [[Tonight]]

#recipe
