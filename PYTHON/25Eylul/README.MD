# 25 Eylül — CNN ile Görüntü Sınıflandırma

Bu klasörde evrişimli sinir ağları (CNN) kullanarak görüntü sınıflandırma yapılan bir defter bulunuyor.

## 📓 İçindekiler

### `25_Eylul.ipynb`
CIFAR-10 veri seti üzerinde uçtan uca CNN eğitim hattı.

- Veri: `keras.datasets` üzerinden `mnist`, `fashion_mnist`, `cifar10`, `cifar100` desteklenecek şekilde parametrik (`DATASET = "cifar10"`) yazılmış
- Türkçe sınıf isimleri (`CLASS_NAMES`) ile etiketleme (ör. cifar10 için: uçak, otomobil, kuş, kedi, geyik, köpek, kurbağa, at, gemi, kamyon)
- `tf.data.Dataset` pipeline'ı ile eğitim/doğrulama/test setlerinin oluşturulması (batch + prefetch), %20 validation split
- **Model mimarisi:**
  - Veri artırma (data augmentation): `RandomFlip`, `RandomRotation`, `RandomZoom`
  - `Rescaling(1/255)`
  - 3 adet evrişim bloğu (`Conv2D` x2 + `BatchNormalization` + `ReLU` + `MaxPooling2D` + `Dropout`), filtre sayıları 32 → 64 → 128
  - `GlobalAveragePooling2D` → `Dense(256)` → `Dropout(0.5)` → `Dense(128)` → `Dense(num_classes, softmax)`
- `Adam` optimizer, `SparseCategoricalCrossentropy` kaybı, 50 epoch, batch size 64
- Eğitim/doğrulama kayıp ve doğruluk eğrilerinin çizdirilip kaydedilmesi (`egitim_egrileri.png`)
- Test seti üzerinde tahmin ve **confusion matrix** görselleştirmesi (`confusion_matrix.png`)
- Eğitim çıktısına göre model, ~13. epoch civarında %70 dolayında doğrulama doğruluğuna ulaşıyor (eğitim log'u kesilmiş, tam sonuç görünmüyor)

## 🛠️ Kullanılan Kütüphaneler
`tensorflow` / `keras`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## 📊 Konu Başlıkları
Convolutional Neural Network (CNN) · Data Augmentation · Batch Normalization · Dropout · Global Average Pooling · `tf.data` Pipeline · Confusion Matrix
