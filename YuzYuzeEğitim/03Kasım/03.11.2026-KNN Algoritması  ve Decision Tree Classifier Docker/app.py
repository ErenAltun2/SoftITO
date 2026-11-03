from pathlib import Path

import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, field_validator
from sklearn.model_selection import train_test_split

from decision_tree import DecisionTree
from knn import KNN

# ---------------------------------------------------------------
# Ayarlar: hangi sütunu tahmin ediyoruz, hangi sütunları kullanıyoruz
# ---------------------------------------------------------------
CSV_PATH = Path(__file__).parent / "patients.csv"
TARGET = "socioeconomic_tier"                       # tahmin edilecek sütun
NUMERIC = ["age", "baseline_bmi", "baseline_charlson_comorbidity_index"]
CATEGORICAL = ["residential_zone", "primary_insurance_provider"]
DEFAULT_K = 51                                      # KNN için komşu sayısı
TREE_MAX_DEPTH = 5                                  # Decision Tree için en fazla derinlik
TREE_MIN_LEAF = 50                                  # Bir yaprakta en az kaç hasta olmalı


class Preprocessor:
    """Eksik değerleri doldurur, kategorileri 0/1 sütunlara çevirir, hepsini ölçekler."""

    def fit(self, df):
        self.medians = df[NUMERIC].astype(float).median()
        self.categories = {c: sorted(df[c].dropna().unique().tolist()) for c in CATEGORICAL}
        self.feature_names = NUMERIC + [
            f"{c}={cat}" for c in CATEGORICAL for cat in self.categories[c]
        ]
        raw = self._raw(df)
        self.mean = raw.mean(axis=0)
        self.std = raw.std(axis=0)
        self.std[self.std == 0] = 1.0
        return self

    def _raw(self, df):
        parts = [df[NUMERIC].astype(float).fillna(self.medians).to_numpy()]
        for c in CATEGORICAL:
            for cat in self.categories[c]:
                parts.append((df[c] == cat).to_numpy(dtype=float).reshape(-1, 1))
        return np.hstack(parts)

    def transform(self, df):
        return (self._raw(df) - self.mean) / self.std


# --- Veriyi yükle, böl, iki modeli de eğit (uygulama açılırken bir kez yapılır) ---
df = pd.read_csv(CSV_PATH).dropna(subset=[TARGET])
train_df, test_df = train_test_split(
    df, test_size=0.2, random_state=42, stratify=df[TARGET]
)
prep = Preprocessor().fit(train_df)

X_train = prep.transform(train_df)
X_test = prep.transform(test_df)
y_train = train_df[TARGET].to_numpy()
y_test = test_df[TARGET].to_numpy()

# Model 1: KNN (sıfırdan yazdığımız)
knn_model = KNN(k=DEFAULT_K).fit(X_train, y_train)
knn_accuracy = knn_model.score(X_test, y_test)

# Model 2: Decision Tree (decision_tree.py)
tree_model = DecisionTree(
    max_depth=TREE_MAX_DEPTH, min_samples_leaf=TREE_MIN_LEAF
).fit(X_train, y_train)
tree_accuracy = tree_model.score(X_test, y_test)

baseline = float(test_df[TARGET].value_counts(normalize=True).max())

app = FastAPI(title="Hasta Sosyoekonomik Seviye - KNN vs Decision Tree", version="2.0")

# --- Küçük test sayfası (/ui adresinde açılır) ---
HTML_PAGE = r"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KNN vs Decision Tree</title>
<style>
  body { font-family: system-ui, sans-serif; max-width: 460px; margin: 40px auto; padding: 0 16px; }
  h2 { margin-bottom: 4px; }
  .sub { color: #777; font-size: 14px; margin-bottom: 16px; line-height: 1.5; }
  label { display: block; font-size: 13px; margin: 10px 0 3px; }
  input, select { width: 100%; padding: 8px; font-size: 15px; box-sizing: border-box; }
  #go { width: 100%; margin-top: 16px; padding: 10px; font-size: 15px; cursor: pointer; }
  .cols { display: flex; gap: 12px; margin-top: 16px; }
  .box { flex: 1; border: 1px solid #ccc; border-radius: 8px; padding: 10px; }
  .box h4 { margin: 0 0 6px; font-size: 13px; color: #777; font-weight: 600; }
  .pred { font-size: 20px; font-weight: 600; }
  .detail { margin-top: 6px; font-size: 13px; color: #777; }
  #error { margin-top: 12px; color: #c00; }
</style>
</head>
<body>
  <h2>KNN vs Decision Tree</h2>
  <div class="sub" id="info">Model bilgisi yükleniyor…</div>

  <label>Yaş</label><input id="age" type="number" min="0" max="120" value="45">
  <label>BMI (boş bırakılabilir)</label><input id="bmi" type="number" step="0.1" value="28">
  <label>Charlson hastalık indeksi (0-8)</label><input id="cci" type="number" min="0" max="20" value="2">
  <label>Yerleşim bölgesi</label><select id="zone"></select>
  <label>Sigorta sağlayıcı</label><select id="ins"></select>
  <label>k (KNN için komşu sayısı)</label><input id="k" type="number" min="1" max="200" value="51">

  <button id="go" onclick="predict()">Tahmin et</button>
  <div id="error"></div>
  <div class="cols">
    <div class="box"><h4>KNN</h4><div class="pred" id="knn-pred">-</div><div class="detail" id="knn-detail"></div></div>
    <div class="box"><h4>Decision Tree</h4><div class="pred" id="tree-pred">-</div><div class="detail" id="tree-detail"></div></div>
  </div>

<script>
  const $ = id => document.getElementById(id);
  const TR = { Low: 'Düşük', Middle: 'Orta', High: 'Yüksek' };
  const pct = x => '%' + (x * 100).toFixed(1);

  fetch('/').then(r => r.json()).then(d => {
    $('info').innerHTML = 'Test doğruluğu:<br>KNN ' + pct(d.models.knn.test_accuracy) +
      ' · Decision Tree ' + pct(d.models.decision_tree.test_accuracy) +
      '<br>Hep en sık sınıfı söylesek: ' + pct(d.majority_baseline);
    $('k').value = d.models.knn.k;
    const fill = (id, opts) => $(id).innerHTML = opts.map(o => `<option>${o}</option>`).join('');
    fill('zone', d.options.residential_zone);
    fill('ins', d.options.primary_insurance_provider);
  });

  const show = (prefix, res) => {
    $(prefix + '-pred').textContent = TR[res.prediction] || res.prediction;
    $(prefix + '-detail').innerHTML = Object.entries(res.probabilities)
      .map(([c, p]) => (TR[c] || c) + ' ' + (p * 100).toFixed(0) + '%').join('<br>');
  };

  async function predict() {
    $('error').textContent = '';
    const bmi = $('bmi').value;
    const body = {
      age: parseInt($('age').value, 10),
      baseline_bmi: bmi === '' ? null : parseFloat(bmi),
      baseline_charlson_comorbidity_index: parseInt($('cci').value, 10),
      residential_zone: $('zone').value,
      primary_insurance_provider: $('ins').value,
      k: parseInt($('k').value, 10)
    };
    const r = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!r.ok) { $('error').textContent = 'Hata: alanları kontrol edin'; return; }
    const d = await r.json();
    show('knn', d.knn);
    show('tree', d.decision_tree);
  }
</script>
</body>
</html>"""


class PredictRequest(BaseModel):
    age: int = Field(..., ge=0, le=120)
    baseline_bmi: float | None = Field(None, ge=10, le=80)
    baseline_charlson_comorbidity_index: int = Field(..., ge=0, le=20)
    residential_zone: str
    primary_insurance_provider: str
    k: int = Field(DEFAULT_K, ge=1, le=200)

    @field_validator("residential_zone", "primary_insurance_provider")
    @classmethod
    def check_category(cls, v, info):
        options = prep.categories[info.field_name]
        if v not in options:
            raise ValueError(f"Geçersiz değer. Seçenekler: {options}")
        return v


@app.get("/")
def root():
    importance = dict(zip(prep.feature_names, tree_model.feature_importances_.round(3).tolist()))
    importance = dict(sorted(importance.items(), key=lambda kv: kv[1], reverse=True))
    return {
        "dataset": "patients.csv",
        "target": TARGET,
        "features": NUMERIC + CATEGORICAL,
        "options": prep.categories,
        "train_size": len(train_df),
        "test_size": len(test_df),
        "majority_baseline": round(baseline, 4),
        "models": {
            "knn": {"k": DEFAULT_K, "test_accuracy": round(knn_accuracy, 4)},
            "decision_tree": {
                "max_depth": TREE_MAX_DEPTH,
                "min_samples_leaf": TREE_MIN_LEAF,
                "test_accuracy": round(tree_accuracy, 4),
                "feature_importance": importance,
            },
        },
    }


@app.get("/ui", response_class=HTMLResponse, include_in_schema=False)
def ui():
    return HTML_PAGE


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: PredictRequest):
    row = pd.DataFrame([req.model_dump(exclude={"k"})])
    x = prep.transform(row)

    knn_proba = knn_model.predict_proba(x, k=req.k)[0]
    knn_label = max(knn_proba, key=knn_proba.get)

    tree_proba = tree_model.predict_proba(x)[0]
    tree_label = max(tree_proba, key=tree_proba.get)

    return {
        "knn": {"prediction": knn_label, "probabilities": knn_proba},
        "decision_tree": {"prediction": tree_label, "probabilities": tree_proba},
        "k": req.k,
    }