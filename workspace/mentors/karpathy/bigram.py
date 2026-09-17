"""Count every pair of neighbours and ask what follows an a."""

TEXT = "the cat sat on the mat"

counts: dict[str, dict[str, int]] = {}
for first, second in zip(TEXT, TEXT[1:]):
    counts.setdefault(first, {})
    counts[first][second] = counts[first].get(second, 0) + 1

after_a = counts["a"]
best = max(after_a, key=lambda c: after_a[c])
print(f"after a: {best}")
