# 18 Eylül — İstatistik & Keşifçi Veri Analizi (EDA)

Bu gün, veri analizinde istatistiksel temeller ve **Keşifçi Veri Analizi (Exploratory Data Analysis)** süreci işlendi. Sentetik müşteri verisi ve gerçek bir Netflix veri seti üzerinde uygulama yapıldı.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `18_09_2026_İstatistik.ipynb` | Sentetik müşteri veri seti üzerinde istatistik ve EDA uygulaması |
| `Keşifci_Veri_Analizi.ipynb` | Kasıtlı olarak bozulmuş (eksik/aykırı değerli) sentetik veri üzerinde EDA alıştırması |
| `NetflixDataSet.ipynb` | Gerçek Netflix veri seti (`netflix_titles.csv`) üzerinde uçtan uca EDA uygulaması |

## 🎯 Konu Başlıkları

- **Kullanılan kütüphaneler:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy.stats`, `statsmodels`, `scikit-learn` (`StandardScaler`, `PCA`)
- **Veri setine ilk bakış:** `.shape`, `.info()`, `.head()`, `.tail()`, `.sample()`
- **Sütun özeti çıkarma:** veri tipi, benzersiz değer sayısı, eksik değer sayısı ve yüzdesi
- **Veri temizleme:**
  - Tekrar eden satırları tespit etme (`.duplicated()`)
  - Tutarsız kategorik verileri düzeltme (`.str.strip()`, `.str.title()`, `.replace()`)
  - Eksik (`NaN`) ve aykırı (outlier) değerlerin tespiti
- **Betimsel istatistik ve güven aralığı:**
  - Ortalama, standart hata (`stats.sem`)
  - `%95 güven aralığı` hesaplama (`stats.t.ppf` ile t-kritik değeri)
- **İleri istatistik araçları:** `VIF` (Variance Inflation Factor - çoklu doğrusal bağlantı kontrolü), `pairwise_tukeyhsd` (grup karşılaştırma testi)

## 💡 Örnek

```python
def ortalama_guven_araligi(seri, guven=0.95):
    veri = seri.dropna()
    n = len(veri)
    ortalama = veri.mean()
    sem = stats.sem(veri)
    t_kritik = stats.t.ppf((1 + guven) / 2, df=n - 1)
    hata_payi = t_kritik * sem
    return ortalama, ortalama - hata_payi, ortalama + hata_payi
```

## ✅ Kazanımlar

- Ham bir veri setini analiz etmeden önce nasıl "tanınması" gerektiğini (şekil, tip, eksik değer) öğrendim.
- Eksik ve aykırı değerleri tespit etme ve bunlarla başa çıkma yöntemlerini gördüm.
- Örneklem istatistiklerinden güven aralığı hesaplamayı uyguladım.
- Gerçek bir veri seti (Netflix) üzerinde uçtan uca bir EDA sürecini deneyimledim.
