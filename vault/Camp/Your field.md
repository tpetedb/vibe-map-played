---
title: "Your field"
date: 2026-09-17
tags: [persona]
---
# Your field

Data engineer: pipelines, warehouses, orchestration and tests.

**Your game (workstream 1).** Pipeline defense: rows flow from left to right, schema drift attacks at night, and you place tests and quarantine tables to keep the gold layer clean until the CEO's dashboard loads.

**Your dataset (workstream 3).** `data/examples/pipeline_runs.csv` with columns run_at, pipeline, layer, rows, seconds, status. The question to answer: Which layer failed last night, and what did the row counts say before it did?

**Rolinda asks.** If the silver run says zero rows, what did the bronze run say, and why did nobody get paged?

## Recipes
- **Two-file task pattern** (workstream 3): A pipeline task as a .py plus a .yaml sidecar with tests. See [[Cookbook]].
- **Schema drift guard** (workstream 4): A hook that refuses a commit when a CSV header changes. See [[Cookbook]].
- **Nightly run report** (workstream 8): Headless agent summarises last night's runs into the vault. See [[Cookbook]].

Back to [[Tonight]]

#persona
