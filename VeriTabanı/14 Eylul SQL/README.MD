# SQL Temelleri

Bu klasör, SQL'e giriş kapsamında yapılan temel tablo tasarımı ve CRUD (Create-Read-Update-Delete) alıştırmalarını içerir. Üç ayrı senaryo üzerinden (hayvanat bahçesi, öğrenciler, oyuncaklar) aynı temel işlemler tekrar edilerek pekiştirilmiştir.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `HayvanatBahcesi.sql` / `hayvanatBahcesi.db` | Hayvanat bahçesindeki hayvanlar üzerinden CRUD alıştırması |
| `ogrenciler.sql` / `Deneme.db` | Öğrenci kayıtları üzerinden CRUD alıştırması |
| `Oyuncaklar-SQL.sql` / `Oyuncaklar.db` | Oyuncak stok/fiyat verisi üzerinden CRUD alıştırması |

## 🎯 Konu Başlıkları

- **Tablo oluşturma:** `CREATE TABLE`, `PRIMARY KEY AUTOINCREMENT`, `NOT NULL`, `DEFAULT`, `CHECK`
- **Veri ekleme:** `INSERT INTO` (tekli ve çoklu satır)
- **Veri okuma / filtreleme:**
  - `SELECT * FROM ...`
  - `WHERE`, `LIKE`, `BETWEEN`
  - `ORDER BY ... DESC/ASC`, `LIMIT`
- **Güncelleme ve silme:** `UPDATE ... SET ... WHERE`, `DELETE FROM ... WHERE`
- **Tablo yapısını değiştirme:** `ALTER TABLE ADD COLUMN`, `ALTER TABLE RENAME COLUMN`

## 💡 Örnek

```sql
CREATE TABLE hayvanlar(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT NOT NULL,
    tur TEXT,
    yas INTEGER CHECK (yas > 0),
    renk TEXT DEFAULT 'Kahverengi'
);

SELECT * FROM hayvanlar WHERE yas BETWEEN 5 AND 7;
```

## ✅ Kazanımlar

- Temel veri tabanı şeması tasarlamayı öğrendim.
- `CHECK` ve `DEFAULT` gibi kısıtlarla veri bütünlüğünü nasıl koruyacağımı gördüm.
- Filtreleme ve sıralama operatörlerini (`LIKE`, `BETWEEN`, `ORDER BY`, `LIMIT`) uyguladım.
- `ALTER TABLE` ile var olan bir tabloyu sonradan nasıl değiştireceğimi öğrendim.
