"""Twenty steps downhill on (w - 3) ** 2, learning from the error."""

w = 0.0
STEP = 0.1

for i in range(20):
    gradient = 2 * (w - 3)
    w -= STEP * gradient
    print(f"step {i + 1}: loss {(w - 3) ** 2:.4f}")

print(f"w = {round(w, 1)}")
