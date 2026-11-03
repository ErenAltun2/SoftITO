"""Iris veri setiyle Random Forest sınıflandırıcısı eğitir ve modeli diske kaydeder."""
import json

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# 1. Veriyi yükle: 150 çiçek, 4 özellik, 3 tür
iris = load_iris()
X, y = iris.data, iris.target

# 2. Eğitim (%80) ve test (%20) olarak ayır
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Modeli eğit
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Test verisiyle değerlendir
y_pred = model.predict(X_test)
dogruluk = accuracy_score(y_test, y_pred)
print(f"Test doğruluğu: {dogruluk:.3f}")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 5. Modeli ve bilgilerini kaydet
joblib.dump(model, "model.joblib")
with open("model_bilgi.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "algoritma": "RandomForestClassifier",
            "agac_sayisi": 100,
            "test_dogrulugu": round(dogruluk, 4),
            "ozellikler": iris.feature_names,
            "siniflar": iris.target_names.tolist(),
        },
        f,
        ensure_ascii=False,
        indent=2,
    )
print("Model kaydedildi: model.joblib")
