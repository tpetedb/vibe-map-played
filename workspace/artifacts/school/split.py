import random

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

rng = random.Random(0)
X = [[rng.random(), rng.random()] for _ in range(400)]
y = [1 if a + b > 1 else 0 for a, b in X]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)
tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print(f"train accuracy: {tree.score(X_train, y_train):.3f}")
print(f"test accuracy: {tree.score(X_test, y_test):.3f}")
