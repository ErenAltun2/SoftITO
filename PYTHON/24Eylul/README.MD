# 24 Eylül — Derin Öğrenmeye Giriş: ANN, RNN/LSTM/GRU

Bu klasörde yapay sinir ağları (Keras & PyTorch), zaman serisi tahmini (LSTM/GRU) ve metin sınıflandırma (duygu analizi) konularını kapsayan defterler bulunuyor.

## 📓 İçindekiler

### `24_Eylul.ipynb`
Tek defterde dört farklı derin öğrenme uygulaması:

**1) Keras ile İkili Sınıflandırma (ANN)**
- Veri: `load_breast_cancer` (scikit-learn)
- `StandardScaler` ile ölçeklendirme
- Dense + Dropout katmanlarından oluşan Sequential model (sigmoid çıkış)
- `EarlyStopping` callback'i ile eğitim

**2) PyTorch ile İkili Sınıflandırma (ANN)**
- Aynı breast cancer verisi, PyTorch `nn.Module` ile yeniden uygulama
- `TensorDataset` / `DataLoader` ile eğitim/doğrulama bölünmesi
- `BCEWithLogitsLoss` + Adam optimizer ile manuel eğitim döngüsü (20 epoch)

**3) Zaman Serisi Tahmini — LSTM vs GRU**
- Sentetik sinüs tabanlı zaman serisi verisi üretimi
- Kayan pencere (windowing) yöntemiyle girdi/çıktı oluşturma (window=30)
- **LSTM** ve **GRU** katmanlarıyla karşılaştırmalı model eğitimi, MSE/MAE metrikleri

**4) Duygu Analizi (Sentiment Analysis) — IMDB**
- Veri: `keras.datasets.imdb` (film yorumları)
- `Embedding` + `LSTM` + `Dropout` + `Dense(sigmoid)` mimarisi
- Metin ön işleme: padding/truncating (maxlen=200)
- Kendi yazılan `encode_text()` fonksiyonu ile serbest metin (yeni yorum) üzerinde canlı tahmin örnekleri

### `24EylulCase_1.ipynb`
Wine veri seti ile çok sınıflı sınıflandırma (Keras ANN) uygulaması.

- Veri: `load_wine` (178 örnek, 13 özellik, 3 sınıf)
- `StandardScaler` ile ölçeklendirme (yalnızca train üzerinde fit)
- Dense(32) → Dropout(0.3) → Dense(16) → Dropout(0.3) → Dense(3, softmax) mimarisi
- `SparseCategoricalCrossentropy` kaybı, `EarlyStopping` callback'i
- Test doğruluğu ve `classification_report` ile sınıf bazlı değerlendirme

### `lstm.ipynb`
Hisse senedi fiyat tahmini (MSFT) için çok adımlı LSTM denemesi.

- `yfinance` ile Microsoft (MSFT) hissesinin 5 yıllık geçmiş verisi çekiliyor
- `MinMaxScaler` ile normalizasyon, çoklu-adım girdi/çıktı pencereleri (n_steps_in=60, n_steps_out=30) hedefleniyor
- İki katmanlı **LSTM** (50+50 nöron) + Dense(30) mimarisi tanımlanıyor
- ⚠️ **Not:** Bu defter eksik/kırık durumda — `data_for_lstm` ve `split_sequences` gibi bazı değişken/fonksiyonlar defterde tanımlanmadan kullanılıyor, bu yüzden baştan sona çalıştırılabilir değil. Kod, referans/taslak amaçlı saklanmış görünüyor.

## 🛠️ Kullanılan Kütüphaneler
`tensorflow` / `keras`, `torch`, `scikit-learn`, `numpy`, `pandas`, `yfinance`

## 📊 Konu Başlıkları
Yapay Sinir Ağları (ANN) · Dropout & EarlyStopping · PyTorch ile Manuel Eğitim Döngüsü · LSTM · GRU · Zaman Serisi Tahmini · Metin Ön İşleme & Embedding · Duygu Analizi

> ℹ️ `lstm.ipynb` dosyası tarih etiketi taşımıyordu; içeriği (LSTM tabanlı zaman serisi tahmini) bu klasördeki diğer LSTM/GRU çalışmasıyla örtüştüğü için buraya eklendi. Farklı bir klasöre ait olması gerekiyorsa haber verebilirsin.
