# Your fork of Vibe Map

Your fork is yours to break and repair; the course keeps living in the
product (https://github.com/tpetedb/vibe-map). Nothing here feeds back into
it, and nothing here is needed to play: this is the copy you experiment on.

Everything the build needs is here: `src/` (the game in load order, with
`src/vendor/` and your own `src/config/`), `tools/build.py` and the generated
inputs under `tools/generated/`.

    just build      # or: python3 tools/build.py
    open game/vibe-map.html

Your camp's `config/camp.toml` still decides who you are, how hard and which
theme; `src/config/00-config.js` is the game's own level: the world scale,
the island radius, the palette. `vibe check --fork` verifies that it builds
and that your configuration is no longer the product's.

## Challenges

Each one is checked; `vibe check --fork <challenge>` runs one of them, and
`vibe check --world prod 6` runs the stop they belong to.

1. `exists`: fork tpetedb/vibe-map on GitHub, then `vibe fork` here.
2. `config`: change one value in `src/config/00-config.js` (the world scale,
   or a palette colour) and rebuild. Look at the result.
3. `topic`: pick a topic from `vibe news` or an article you found, and have
   your agent add it to `tools/generated/campaign.json` (a stop of your own)
   or to `tools/generated/tree.js` (a node of your own), then rebuild.
4. `repair`: break the build on purpose, run `just record`, read the error,
   repair it, and run `just record` again. The two runs in `repair.json` are
   the evidence.
