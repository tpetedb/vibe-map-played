import math
from collections import Counter

NOTES = {
    "Headless agents and scheduling": (
        "the monday job runs vibe vault build on a schedule while you sleep and "
        "it failed because uv was missing on the runner"
    ),
    "CI-CD and automation": "a workflow runs the tests on every push to main",
    "Git hooks": "a hook runs before a commit and can refuse it",
    "Obsidian and the graph": "notes link to each other and the graph shows it",
}
QUESTION = "why did the monday run fail?"


def vector(text):
    return Counter(text.lower().split())


def cosine(a, b):
    dot = sum(a[word] * b[word] for word in set(a) & set(b))
    size = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(
        sum(v * v for v in b.values())
    )
    return dot / size if size else 0.0


question = vector(QUESTION)
ranked = sorted(
    ((cosine(question, vector(text)), name) for name, text in NOTES.items()),
    reverse=True,
)
print("top 3 for:", QUESTION)
for score, name in ranked[:3]:
    print(f"  {score:.2f}  {name}")
print(f"It failed because uv was missing on the runner. source: {ranked[0][1]}")
