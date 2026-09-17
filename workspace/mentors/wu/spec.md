# A nickname on the leaderboard

## Spec
Done is: a player can set a nickname, the leaderboard shows it instead of the
name, and a player without one still shows their name.

## Plan
1. Add a nickname column to the CSV reader with an empty default.
2. Show nickname or name in the table.
3. Write two tests: one with a nickname, one without.

## To-do
- [ ] Read the CSV with the extra column.
- [ ] Render nickname or name.
- [ ] Two tests, both red first.
