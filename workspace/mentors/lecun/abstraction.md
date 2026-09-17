# Renaming the score column

## What mattered
- The column is called `score` in workspace/data/scores.csv.
- Two files read it: workspace/python/scores.py and workspace/sql/top_runs.sql.
- The rename had to keep the old header readable for one release.

## What I could throw away
- The whole history of the file, which I pasted in for no reason.
- The game code, which never touches the CSV.
- My long explanation of why the name was bad. The agent only needed the name.
