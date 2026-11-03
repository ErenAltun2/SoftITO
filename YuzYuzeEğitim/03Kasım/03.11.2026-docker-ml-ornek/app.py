"""Eğitilmiş Iris modelini HTTP API olarak sunar."""
import json

import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)
model = joblib.load("model.joblib")
with open("model_bilgi.json", encoding="utf-8") as f:
    BILGI = json.load(f)

ALANLAR = ["canak_uzunluk", "canak_genislik", "tac_uzunluk", "tac_genislik"]

FORM = """<!doctype html><meta charset="utf-8"><title>Iris Tahmini</title>
<body style="font-family:sans-serif;max-width:420px;margin:40px auto">
<h2>Iris çiçeği tahmini</h2>
<form method="post" action="/tahmin-form">
  <label>Çanak yaprak uzunluğu (cm) <input name="canak_uzunluk" value="5.1"></label><br><br>
  <label>Çanak yaprak genişliği (cm) <input name="canak_genislik" value="3.5"></label><br><br>
  <label>Taç yaprak uzunluğu (cm) <input name="tac_uzunluk" value="1.4"></label><br><br>
  <label>Taç yaprak genişliği (cm) <input name="tac_genislik" value="0.2"></label><br><br>
  <button>Tahmin et</button>
</form>
{sonuc}
</body>"""


def tahmin_et(degerler):
    olcum = [[float(degerler[a]) for a in ALANLAR]]
    sinif = int(model.predict(olcum)[0])
    olasiliklar = model.predict_proba(olcum)[0]
    return {
        "tur": BILGI["siniflar"][sinif],
        "olasiliklar": {
            ad: round(float(p), 3) for ad, p in zip(BILGI["siniflar"], olasiliklar)
        },
    }


@app.get("/")
def anasayfa():
    return FORM.format(sonuc="")


@app.post("/tahmin-form")
def tahmin_form():
    try:
        s = tahmin_et(request.form)
        sonuc = f"<h3>Tahmin: {s['tur']}</h3><pre>{json.dumps(s['olasiliklar'], indent=2)}</pre>"
    except (KeyError, ValueError):
        sonuc = "<p style='color:red'>Dört alanı da sayı olarak girin.</p>"
    return FORM.format(sonuc=sonuc)


@app.post("/tahmin")
def tahmin():
    veri = request.get_json(silent=True) or {}
    try:
        return jsonify(tahmin_et(veri))
    except (KeyError, ValueError, TypeError):
        return jsonify({"hata": f"JSON şu alanları sayı olarak içermeli: {ALANLAR}"}), 400


@app.get("/model")
def model_bilgisi():
    return jsonify(BILGI)


@app.get("/health")
def health():
    return {"durum": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
