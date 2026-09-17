# Nicknames for players

## Why
Two players share a first name and the leaderboard is confusing.

## What
A player may set a nickname; the leaderboard shows it instead of the name.

## Not this
No profiles, no avatars, no login.
No migration of the rows already in scores.csv.

## Files
workspace/python/scores.py reads it; workspace/sql/top_runs.sql groups on it.

## Done when
The nickname appears in scores.csv and the tests cover an empty one.
A run with no nickname still shows the name, and the test says so.
