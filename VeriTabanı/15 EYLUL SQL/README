# 15 Eylül — İleri Seviye SQL

Bu klasör, ilişkisel veri tabanı tasarımı, tablolar arası ilişkiler ve ileri seviye sorgulama tekniklerinin işlendiği çalışmaları içerir. İki ayrı case üzerinden (kütüphane üye/kitap sistemi ve öğrenci/ders/not sistemi) aynı kavramlar uygulanmıştır.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `15EylulCase.sql` / `15EylulCase.db` | Kütüphane sistemi: üyeler, kitaplar, ödünç alma kayıtları |
| `15EylulSQLIlerıSeviye.sql` / `15EylulSQLIlerıSeviye.db` | Okul sistemi: öğrenciler, dersler, notlar |

## 🎯 Konu Başlıkları

### 1. Kısıtlar ve İlişkiler
- `PRAGMA foreign_keys = ON;` ile yabancı anahtar denetimini aktifleştirme
- `FOREIGN KEY (REFERENCES ...)` ile tablolar arası ilişki kurma
- `ON DELETE CASCADE` ile bağlı kayıtların otomatik silinmesi
- Bileşik birincil anahtar (`PRIMARY KEY (kolon1, kolon2)`)
- `UNIQUE` kısıtı ile tekil (unique) sütunlar

### 2. JOIN İşlemleri
- `INNER JOIN` ile birden fazla tabloyu birleştirme
- `LEFT JOIN` ile eşleşmeyen kayıtları da (örn. hiç kitap almamış üyeleri) listeleme

### 3. Gruplama ve Toplama Fonksiyonları
- `GROUP BY`, `HAVING`
- `AVG()`, `COUNT()`, `MAX()`
- `WHERE` ile `HAVING` arasındaki fark: `WHERE` gruplamadan önce satır bazlı filtreler, `HAVING` gruplama sonrası toplama sonuçlarını filtreler.

### 4. Alt Sorgular (Subquery)
- `WHERE id IN (SELECT ...)`
- `WHERE ... NOT IN (SELECT ...)`
- Alt sorgu ile hesaplanan ortalamaya göre filtreleme

### 5. Koşullu İfadeler
- `CASE WHEN ... THEN ... ELSE ... END` ile etiketleme (örn. gecikme durumu, yaş grubu)

### 6. Index
- `CREATE INDEX` ile sorgu performansını artırma
- `CREATE UNIQUE INDEX` ile tekillik garantisi

## 💡 Örnek

```sql
SELECT
    u.ad AS uye_adi,
    AVG(o.gun) AS ortalama_gun,
    COUNT(o.kitap_id) AS alinan_kitap_sayisi
FROM uyeler u
JOIN odunc o ON u.id = o.uye_id
GROUP BY u.id, u.ad
HAVING AVG(o.gun) > 20;
```

## ✅ Kazanımlar

- İlişkisel tablo tasarımını ve yabancı anahtar kısıtlarını uygulamalı olarak öğrendim.
- `JOIN` türleri arasındaki farkı (özellikle `LEFT JOIN`'in ne zaman gerektiğini) kavradım.
- `GROUP BY`/`HAVING` ile özet istatistikler üretmeyi öğrendim.
- Alt sorgularla daha karmaşık filtreleme senaryolarını çözdüm.
- `CASE WHEN` ile veriyi kategorilere ayırmayı, `INDEX` ile performans/tekillik sağlamayı öğrendim.
