# 23 Eylül — Kümeleme, Karar Ağaçları, Random Forest ve Ensemble Yöntemler

Bu klasörde gözetimsiz öğrenme (kümeleme) ile ağaç tabanlı/topluluk (ensemble) sınıflandırma yöntemlerini kapsayan üç defter bulunuyor.

## 📓 İçindekiler

### `23EylulPart1.ipynb`
**Bölüm 1 — Kümeleme (Unsupervised Learning)**
- Veri: `Data.csv` (kredi kartı müşteri verisi, `CUST_ID` index)
- Eksik veriler `SimpleImputer` (mean) ile dolduruldu, `StandardScaler` ile ölçeklendirildi
- **K-Means**: Elbow yöntemi ve Silhouette skoru ile optimum k belirleme, PCA (2 bileşen) ile kümelerin görselleştirilmesi
- **Hiyerarşik (Agglomerative) Kümeleme**: Ward bağlantısı, dendrogram, PCA ile görselleştirme
- **DBSCAN**: k-mesafe grafiği ile eps belirleme, gürültü (noise) oranı analizi
- Değerlendirme metrikleri: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Score

**Bölüm 2 — Karar Ağacı & Random Forest**
- Veri: `load_breast_cancer` (scikit-learn)
- `GridSearchCV` ile **Decision Tree** hiperparametre optimizasyonu, ağaç görselleştirmesi (`plot_tree`)
- `GridSearchCV` ile **Random Forest** hiperparametre optimizasyonu
- Test doğruluğu ve 5 katlı çapraz doğrulama (cross-validation) karşılaştırması
- Özellik önem (feature importance) grafiği

### `23EylulCase.ipynb`
Titanic hayatta kalma tahmini — Karar Ağacı ve Random Forest uygulaması.

- Veri: `titanic.csv`
- Ön işleme: `Cabin` → `HasCabin` (0/1), `Age` medyan ile doldurma, `Embarked` mode ile doldurma, `Sex` binary encoding, `Embarked` one-hot encoding
- `GridSearchCV` ile **Decision Tree** (criterion, max_depth, min_samples_leaf/split) optimizasyonu ve ağaç görselleştirmesi
- `GridSearchCV` ile **Random Forest** optimizasyonu
- Decision Tree vs Random Forest: test doğruluğu, 5 katlı CV doğruluğu, classification report karşılaştırması
- Random Forest özellik önem grafiği (Titanic'te hayatta kalmayı en çok etkileyen değişkenler)

### `23EylulPart2.ipynb`
Ensemble (topluluk) sınıflandırıcıların karşılaştırılması.

- Veri: `load_breast_cancer` (scikit-learn)
- Karşılaştırılan modeller: **Random Forest, AdaBoost, Gradient Boosting, HistGradientBoosting, XGBoost**
- 5 katlı Stratified K-Fold çapraz doğrulama (Accuracy, ROC-AUC) + test seti sonuçları + eğitim süresi
- Sonuçlar CV AUC'ye göre sıralanmış özet tablo halinde sunuluyor
- Not: Bu defterde ayrıca `catboost` kütüphanesi kuruluyor ancak sonuç tablosunda kullanılmıyor (sadece 5 model karşılaştırılıyor)

## 🛠️ Kullanılan Kütüphaneler
`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `lightgbm`, `catboost`, `scipy`

## 📊 Konu Başlıkları
K-Means · Hiyerarşik Kümeleme · DBSCAN · PCA · Decision Tree · Random Forest · AdaBoost · Gradient Boosting · HistGradientBoosting · XGBoost · GridSearchCV · Cross-Validation
