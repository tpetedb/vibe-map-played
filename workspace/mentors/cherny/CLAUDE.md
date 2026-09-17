# Working with my agent

## Rules
- Never edit a generated file; change the generator and run it again.

## How it is verified
`uv run pytest tests/test_build.py` rebuilds and compares, so a hand edit to a
generated file shows up as a failing test before I can commit it.
