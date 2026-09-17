"""My clever rule first, then plain search over every pair."""

NUMS = [2, 17, 30, 41, 55, 70, 88]

# The rule I invented: the smallest and the largest should be the pair.
guess = (min(NUMS), max(NUMS))
print(f"my rule says: {guess[0]} {guess[1]} (sum {sum(guess)})")

for i, a in enumerate(NUMS):
    for b in NUMS[i + 1 :]:
        if a + b == 100:
            print(f"search found: {a} {b}")
