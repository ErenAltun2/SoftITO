import numpy as np
from sklearn.tree import DecisionTreeClassifier


class DecisionTree:
    """scikit-learn DecisionTreeClassifier'ı, knn.py'deki KNN ile aynı arayüzle saran sınıf."""

    def __init__(self, max_depth: int = 5, min_samples_leaf: int = 50, random_state: int = 42):
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.model = DecisionTreeClassifier(
            max_depth=max_depth,
            min_samples_leaf=min_samples_leaf,
            random_state=random_state,
        )
        self.classes_ = None

    def fit(self, X, y):
        self.model.fit(np.asarray(X, dtype=float), np.asarray(y))
        self.classes_ = self.model.classes_.tolist()
        return self

    def predict(self, X):
        return self.model.predict(np.atleast_2d(np.asarray(X, dtype=float)))

    def predict_proba(self, X):
        """Her sınıf için yaprak düğümündeki oran (KNN'deki oy oranına karşılık gelir)."""
        probs = self.model.predict_proba(np.atleast_2d(np.asarray(X, dtype=float)))
        return [
            {str(c): round(float(p), 3) for c, p in zip(self.classes_, row)}
            for row in probs
        ]

    def score(self, X, y):
        return float((self.predict(X) == np.asarray(y)).mean())

    @property
    def feature_importances_(self):
        return self.model.feature_importances_