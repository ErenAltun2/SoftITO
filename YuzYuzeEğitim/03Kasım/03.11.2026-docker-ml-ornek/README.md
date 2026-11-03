# Docker ile ML Modeli: Iris Sınıflandırıcı

Bu örnekte scikit-learn ile bir **Random Forest** modeli eğitiliyor ve Flask API'si üzerinden sunuluyor. Model, çiçeğin 4 ölçüsüne bakarak türünü tahmin ediyor: *setosa*, *versicolor* veya *virginica*.

## Nasıl çalışır?

1. `docker build` sırasında `train.py` çalışır. Iris verisini %80 eğitim ve %20 test olarak böler, modeli eğitir, doğruluğu yazdırır ve modeli `model.joblib` dosyasına kaydeder.
2. Kaydedilen model imajın içine girer. Konteyner her başladığında yeniden eğitim yapılmaz.
3. `app.py` modeli yükler ve tahminleri HTTP üzerinden sunar. Gunicorn ile 2 işçi süreç çalışır.

## Çalıştırma

```bash
docker compose up -d --build
```

Build çıktısında modelin test doğruluğunu görürsünüz. Örneğin `Test doğruluğu: 0.900`.

Tarayıcıda http://localhost:8000 adresinde basit bir form açılır.

## API

```bash
# Tahmin
curl -X POST http://localhost:8000/tahmin \
  -H "Content-Type: application/json" \
  -d '{"canak_uzunluk":6.7,"canak_genislik":3.0,"tac_uzunluk":5.2,"tac_genislik":2.3}'

# Model bilgisi
curl http://localhost:8000/model

# Sağlık kontrolü
curl http://localhost:8000/health
```

Örnek yanıt:

```json
{"olasiliklar":{"setosa":0.0,"versicolor":0.0,"virginica":1.0},"tur":"virginica"}
```

## Compose olmadan

```bash
docker build -t iris-ml:1.0 .
docker run -d --name iris -p 8000:8000 iris-ml:1.0
docker logs iris
docker rm -f iris
```

## Geliştirme fikirleri

- Algoritmayı `train.py` içinde değiştirin. Örneğin `LogisticRegression` veya `SVC` kullanıp doğruluğu karşılaştırın.
- Modeli imaja gömmek yerine bir volume'den yükleyin. Böylece imajı yeniden build etmeden modeli güncelleyebilirsiniz.
- Eğitimi ayrı bir aşamada yapın (multi-stage build). Böylece son imajda yalnızca model ve API kalır.
