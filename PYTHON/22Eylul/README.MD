# 22 Eylül — Doğrusal/Lojistik Regresyon, SVM, KNN

Bu klasörde regresyon ve sınıflandırma problemlerine giriş niteliğinde iki defter bulunuyor: ders çalışması (`22EylulDers.ipynb`) ve bir uygulama/case çalışması (`22EylulCase.ipynb`).

## 📓 İçindekiler

### `22EylulDers.ipynb`
İki ayrı veri seti üzerinden regresyon ve sınıflandırma konularının işlendiği ders defteri.

**1) Abalone (Deniz Salyangozu) — Yaş Tahmini (Regresyon)**
- Veri: `abalone.data` (Sex, Length, Diameter, Height, Weight vb. özellikler; hedef: `Rings` → yaş)
- Kategorik `Sex` değişkeni one-hot encoding ile sayısallaştırıldı
- Korelasyon matrisi ve dağılım grafikleriyle keşifsel veri analizi (EDA)
- **Çoklu Doğrusal Regresyon** (`LinearRegression`) ile yaş (Rings) tahmini
- `statsmodels` (OLS) ile katsayı anlamlılığı / model özeti
- Artık (residual) analizi ve normallik kontrolü
- **Polinomsal Regresyon**: tek değişken (Shell Weight) üzerinde derece 1–4 karşılaştırması, ardından tüm özelliklerle 2. derece polinom modeli
- Metrikler: R², MAE, MSE, RMSE

**2) German Credit — Kredi Riski Sınıflandırması**
- Veri: `german.data` (20 özellik: hesap durumu, kredi geçmişi, yaş, meslek vb.)
- Hedef değişken `Bad_risk` (iyi/kötü kredi riski) oluşturuldu
- Kategorik değişkenler one-hot encoding, sayısal değişkenler `StandardScaler` ile ölçeklendirildi
- **Lojistik Regresyon**: accuracy, precision, recall, F1, confusion matrix
- **SVM** (linear ve RBF çekirdek), `GridSearchCV` ile hiperparametre optimizasyonu (C, gamma)
- **KNN**: PCA ile 2/3 boyuta indirgenmiş görselleştirme, farklı k değerleri için CV skorları, `GridSearchCV` ile en iyi k/weights/p parametreleri
- Tüm modellerin (Lojistik Regresyon, SVM-RBF, KNN) karşılaştırma tablosu (Accuracy, Precision, Recall, F1, AUC)

### `22EylulCase.ipynb`
Wine Quality (kırmızı şarap kalitesi) veri seti üzerinde uygulama çalışması.

- Veri: `winequality-red.csv`
- EDA: kalite puanı dağılımı, korelasyon ısı haritası
- **1) Lineer Regresyon**: `quality` puanının (sayısal) doğrudan tahmini — MSE, RMSE, MAE, R², katsayı önem grafiği, gerçek vs tahmin scatter grafiği
- **2) Lojistik Regresyon**: `quality >= 7` eşiğiyle ikili sınıflandırmaya (iyi/kötü şarap) dönüştürülüp `class_weight="balanced"` ile model eğitimi — Accuracy, Precision, Recall, F1, ROC-AUC, confusion matrix, ROC eğrisi, katsayı önem grafiği

## 🛠️ Kullanılan Kütüphaneler
`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `statsmodels`

## 📊 Konu Başlıkları
Doğrusal Regresyon · Polinomsal Regresyon · Lojistik Regresyon · SVM (linear/RBF) · KNN · Ölçeklendirme · One-Hot Encoding · GridSearchCV · Model Karşılaştırma
