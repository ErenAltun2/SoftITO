# SOFTİTO Eğitimi — Çalışma Deposu

Bu repository, **SOFTİTO** eğitimi kapsamında öğrendiğim konuların günlük olarak düzenlenmiş uygulama dosyalarını içerir. Her klasör, o gün işlenen konuyu ve yaptığım alıştırma/case çözümlerini barındırır.

SOFTİTO çalışmalarına ek olarak, yüz yüze eğitim sürecindeki not defterleri ve uygulamalar da tarih sırasına göre aşağıda yer almaktadır.

## 📚 İçindekiler

### 🗄️ SQL

| Klasör | Konu | İçerik |
|---|---|---|
| [`VeriTabanı/14 Eylul SQL`](./VeriTaban%C4%B1/14%20Eylul%20SQL) | SQL'e Giriş | Tablo oluşturma, CRUD işlemleri (INSERT/SELECT/UPDATE/DELETE), `ALTER TABLE`, `LIKE`, `BETWEEN`, sıralama ve limitleme |
| [`VeriTabanı/15 Eylul SQL`](./VeriTaban%C4%B1/15%20EYLUL%20SQL) | İleri Seviye SQL | Kısıtlar (`CHECK`, `UNIQUE`, `FOREIGN KEY`), `JOIN` türleri, `GROUP BY`/`HAVING`, alt sorgular, `CASE WHEN`, `INDEX` |

### 🐍 Python

| Klasör | Konu | Özet |
|---|---|---|
| [`Python/16Eylul`](./PYTHON/16Eylul) | Python'a Giriş | `print`, yorum satırları, değişkenler, veri tipleri, operatörler, `if-else`, string işlemleri |
| [`Python/17Eylul`](./PYTHON/17Eylul) | Pandas'a Giriş | `Series`, `DataFrame`, CSV okuma/yazma |
| [`Python/18Eylul`](./PYTHON/18Eylul) | İstatistik & Keşifçi Veri Analizi (EDA) | Betimsel istatistik, güven aralığı, eksik/aykırı değer analizi, veri temizleme |
| [`Python/21Eylul`](./PYTHON/21Eylul) | Makine Öğrenmesi — Regresyon | `scikit-learn` ile regresyon problemleri, korelasyon analizi, train/test ayrımı |
| [`Python/22Eylul`](./PYTHON/22Eylul) | Doğrusal/Lojistik Regresyon, SVM, KNN | Abalone & German Credit & Wine Quality veri setleri; regresyon, ikili sınıflandırma, ölçeklendirme, `GridSearchCV`, model karşılaştırma |
| [`Python/23Eylul`](./PYTHON/23Eylul) | Kümeleme & Ağaç Tabanlı Yöntemler | K-Means, Hiyerarşik Kümeleme, DBSCAN; Decision Tree & Random Forest (Titanic); Ensemble karşılaştırması (AdaBoost, Gradient Boosting, XGBoost) |
| [`Python/24Eylul`](./PYTHON/24Eylul) | Derin Öğrenmeye Giriş — ANN & LSTM/GRU | Keras/PyTorch ile yapay sinir ağları, zaman serisi tahmini (LSTM/GRU), IMDB duygu analizi |
| [`Python/25Eylul`](./PYTHON/25Eylul) | CNN ile Görüntü Sınıflandırma | CIFAR-10 üzerinde evrişimli sinir ağı (CNN), veri artırma, confusion matrix |

### 🧑‍🏫 Yüz Yüze Eğitim

| Klasör | Konu | İçerik |
|---|---|---|
| [`13Ekim`](./YuzYuzeE%C4%9Fitim/13Ekim) | Apache Hadoop | Google Colab üzerinde Hadoop lab çalışması; NameNode, DataNode, ResourceManager ve NodeManager bileşenleri |
| [`15Ekim`](./YuzYuzeE%C4%9Fitim/15Ekim) | Metin Vektörleştirme ve Gömme Yöntemleri | TF-IDF, Word2Vec, FastText ve GloVe; seyreklik, embedding karşılaştırması ve metin sınıflandırma örnekleri |
| [`16Ekim`](./YuzYuzeE%C4%9Fitim/16Ekim) | RNN, LSTM ve GRU | Sıralı veriler ve tekrarlayan sinir ağları; PyTorch ve Keras ile uygulamalar |
| [`20Ekim`](./YuzYuzeE%C4%9Fitim/20Ekim) | Transformer Mimarisi | Transformer mimarisi ve temel bileşenleri üzerine çalışma |
| [`21Ekim`](./YuzYuzeE%C4%9Fitim/21Ekim) | Mini GPT | Decoder-only Transformer mimarisi ve Mini GPT uygulamaları |
| [`22Ekim`](./YuzYuzeE%C4%9Fitim/22Ekim) | Hugging Face Transformers | Hazır Transformer modellerini ve büyük dil modellerini kullanmaya yönelik çalışmalar |
| [`23Ekim`](./YuzYuzeE%C4%9Fitim/23Ekim) | Transformer ve LLM Uygulamaları | Transformer/büyük dil modeli konularındaki uygulama ve alıştırmalar |
| [`26Ekim`](./YuzYuzeE%C4%9Fitim/26Ekim) | Model Yönlendirme ve Üretken Yapay Zekâ | Duygu ekleme/model steering denemeleri ve karakter tabanlı sohbet uygulaması |
| [`27Ekim`](./YuzYuzeE%C4%9Fitim/27Ekim) | Gelişmiş RAG Mimarisi | Retrieval-Augmented Generation (RAG) mimarisi ve uygulamaları |
| [`30Ekim`](./YuzYuzeE%C4%9Fitim/30Ekim) | Gelişmiş RAG Projesi | Belge yükleme, metadata ve gelişmiş RAG teknikleri üzerine kişisel proje çalışmaları |
| [`02Kasım`](./YuzYuzeE%C4%9Fitim/02Kas%C4%B1m) | LoRA ile Model Uyarlama | Qwen modeli üzerinde LoRA/PEFT yaklaşımıyla ince ayar çalışması |
| [`03Kasım`](./YuzYuzeE%C4%9Fitim/03Kas%C4%B1m) | Docker ile Makine Öğrenmesi | KNN ve Decision Tree sınıflandırıcıları; model/API uygulamaları ve Docker ile çalıştırma |
| [`04Kasım`](./YuzYuzeE%C4%9Fitim/04Kas%C4%B1m) | Büyük Dil Modellerinde Bilgi Damıtma | Qwen öğretmen ve öğrenci modelleriyle knowledge distillation çalışması |
| [`05Kasım`](./YuzYuzeE%C4%9Fitim/05Kas%C4%B1m) | Büyük Dil Modellerinde Bilgi Damıtma | Qwen modelleriyle bilgi damıtma uygulamasının devamı |
| [`06Kasım`](./YuzYuzeE%C4%9Fitim/06Kas%C4%B1m) | Görüntü İşleme ve Nesne Tespiti | Görüntü işleme, CNN, U-Net, Mask R-CNN, YOLO ve SSD çalışmaları |

## 🛠️ Kullanılan Teknolojiler

- **SQL:** SQLite
- **Python:** pandas, numpy, matplotlib, seaborn, scipy, statsmodels, scikit-learn, xgboost, lightgbm, catboost, tensorflow/keras, torch (PyTorch)
- **Ortam:** Google Colab / Jupyter Notebook
- **Yüz yüze eğitim çalışmaları:** Apache Hadoop, Hugging Face Transformers, LoRA/PEFT, RAG, Docker

## 📁 Genel Klasör Yapısı

```
.
├── SQL/
│   ├── SQL-Temelleri/
│   └── 15Eylul-Ileri-SQL/
└── Python/
    ├── 16Eylul/
    ├── 17Eylul/
    ├── 18Eylul/
    ├── 21Eylul/
    ├── 22Eylul/
    ├── 23Eylul/
    ├── 24Eylul/
    └── 25Eylul/
└── YuzYuzeEğitim/
    ├── 13Ekim/
    ├── 15Ekim/
    └── ...
```

Yüz yüze eğitim çalışmaları, kök dizindeki `YuzYuzeEğitim/` klasörü altında `13Ekim`–`30Ekim` ve `02Kasım`–`06Kasım` tarihli klasörlerde tutulur.

Her klasörün kendi `README.md` dosyası, o gün işlenen konunun detaylarını ve dosya açıklamalarını içerir.

---
*Bu depo, SOFTİTO ve yüz yüze eğitim süreçlerindeki kişisel çalışmaları ve ders notlarını içerir.*
