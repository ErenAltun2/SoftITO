from collections import Counter

import numpy as np


class KNN:
    """Sıfırdan yazılmış K-En Yakın Komşu (K-Nearest Neighbors) sınıflandırıcısı."""

    def __init__(self, k: int = 3):
        if k < 1:
            raise ValueError("k en az 1 olmalıdır")
        self.k = k
        self.X_train = None
        self.y_train = None
        self.classes_ = None

    def fit(self, X, y):
        # KNN "tembel" bir algoritmadır: eğitim = veriyi saklamak
        self.X_train = np.asarray(X, dtype=float)
        self.y_train = np.asarray(y)
        self.classes_ = sorted(set(self.y_train.tolist()))
        return self

    def _votes(self, x, k):
        # Öklid mesafesi: tüm eğitim noktalarına olan uzaklık
        distances = np.sqrt(((self.X_train - x) ** 2).sum(axis=1))
        # En yakın k komşunun indeksleri
        nearest = np.argsort(distances)[:k]
        return Counter(self.y_train[nearest].tolist())

    def _prepare(self, X, k):
        k = min(k or self.k, len(self.X_train))
        return np.atleast_2d(np.asarray(X, dtype=float)), k

    def predict(self, X, k=None):
        X, k = self._prepare(X, k)
        # Çoğunluk oylaması
        return np.array([self._votes(x, k).most_common(1)[0][0] for x in X])

    def predict_proba(self, X, k=None):
        """Her sınıf için komşular arasındaki oy oranını döndürür."""
        X, k = self._prepare(X, k)
        result = []
        for x in X:
            votes = self._votes(x, k)
            result.append({c: round(votes.get(c, 0) / k, 3) for c in self.classes_})
        return result

    def score(self, X, y):
        return float((self.predict(X) == np.asarray(y)).mean())