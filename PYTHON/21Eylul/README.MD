# 21 Eylül — Makine Öğrenmesine Giriş: Regresyon

Bu gün, **scikit-learn** kullanılarak regresyon problemlerine giriş yapıldı. Hem gerçekçi bir mühendislik senaryosu (nükleer reaktör simülasyon verisi) hem de klasik bir örnek veri seti (diyabet) üzerinde çalışıldı.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `21EylulCase.ipynb` | **Case:** NuScale US600 küçük modüler nükleer reaktör (SMR) yakıt çubukları simülasyon verisi (MCNP6 ile üretilmiş) üzerinde regresyon uygulaması |
| `21EylulDers.ipynb` | **Ders:** scikit-learn'ün hazır `load_diabetes` veri seti üzerinde regresyon örneği |

## 🎯 Konu Başlıkları

- **Kullanılan kütüphaneler:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`
- **Tekrarlanabilirlik:** `random.seed()`, `np.random.seed()` ile sabit `SEED` kullanımı
- **Veri setini okuma ve inceleme:**
  - Boşluk ayraçlı (`sep=r"\s+"`) dosya okuma
  - `.shape`, `.columns`, `.info()`
- **Hazır veri setleri:** `sklearn.datasets.load_diabetes`, `load_breast_cancer`
- **Girdi (X) / Hedef (y) ayrımı:** özellik sütunlarını ve tahmin edilecek hedef değişkeni belirleme
- **Görselleştirme:**
  - `sns.histplot()` ile hedef değişkenin dağılımı
  - `sns.heatmap()` ile korelasyon matrisi
- **Train/Test ayrımı:** `train_test_split()`

## 💡 Örnek

```python
from sklearn.model_selection import train_test_split

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=SEED
)
```

## ✅ Kazanımlar

- Bir regresyon probleminde girdi (X) ve hedef (y) değişkenlerini nasıl ayıracağımı öğrendim.
- Hem hazır (diyabet) hem de gerçekçi bir mühendislik veri setiyle (nükleer reaktör) çalışma deneyimi kazandım.
- Korelasyon haritası ile değişkenler arası ilişkileri görselleştirmeyi öğrendim.
- Model eğitimi öncesi `train_test_split` ile veriyi eğitim/test olarak ayırmayı uyguladım.
