--Tablo Tasarımı ve Kısıtlar

-- FOREIGN key kapalı defaultta açmak için 
PRAGMA foreign_keys= ON;

CREATE TABLE uyeler(
	
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    yas INTEGER CHECK (yas > 13),
    sehir TEXT DEFAULT 'Erzincan',
    kayit TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE kitaplar(
	kitap_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kitap_adi TEXT UNIQUE NOT NULL
	
);

CREATE TABLE odunc(
	--on delete cascade ana sey sılındı mı hepsı 
	--bırden butun tablolardakı ona baglı bılgıler gıder
	
	uye_id INTEGER REFERENCES uyeler(id) ON DELETE CASCADE,
    kitap_id INTEGER REFERENCES kitaplar(kitap_id),
    PRIMARY KEY (uye_id, kitap_id)
	
);

-----Veri Ekleme

INSERT INTO kitaplar (kitap_adi) VALUES 
('Nutuk'),
('Suç ve Ceza'),
('Simyacı'),
('1984'),
('Kürk Mantolu Madonna');

INSERT INTO uyeler (ad, yas, sehir) VALUES 
('Ahmet Yılmaz', 24, 'İstanbul'),
('Ayşe Kaya', 19, 'Ankara'),
('Mehmet Demir', 32, 'İzmir'),
('Fatma Çelik', 15, 'Erzincan'),
('Ali Şahin', 28, 'Bursa'),
('Zeynep Aydın', 21, 'Antalya'),
('Emre Koç', 17, 'Trabzon'),
('Elif Doğan', 22, 'Eskişehir'),
('Can Özkan', 35, 'Adana'),
('Selin Arslan', 20, 'Samsun');

INSERT INTO uyeler (ad, yas) VALUES ('Eren Altun', 23);

INSERT INTO uyeler (ad, yas) VALUES ('Ali Osman', 10);
-- kurala uymama hatası basta check dıye tanımlama yaptık cunku. 


INSERT INTO odunc (uye_id, kitap_id) VALUES (99, 1);
--- PRAGMA foreign_keys= ON; bastakı bu komut sayesınde yabancı anahtar denetımını actık verıtabanlarını kontrol eder gecersız anahtarlar ıle olusturmaz 

ALTER TABLE odunc ADD COLUMN gun INTEGER;
INSERT INTO odunc (uye_id, kitap_id, gun) VALUES 
-- Üye 1
(1, 1, 14), (1, 2, 7),
-- Üye 2
(2, 2, 21), (2, 3, 5),
-- Üye 3
(3, 1, 30), (3, 4, 12),
-- Üye 4
(4, 3, 15), (4, 5, 40),
-- Üye 5
(5, 2, 10), (5, 4, 25),
-- Üye 6
(6, 1, 18), (6, 5, 8),
-- Üye 7
(7, 3, 35), (7, 4, 4),
-- Üye 8
(8, 2, 45), (8, 5, 16),
-- Üye 9
(9, 1, 9),  (9, 3, 27),
-- Üye 10
(10, 4, 6), (10, 5, 33);

SELECT 
    u.ad AS uye_adi,
    k.kitap_adi,
    o.gun AS gun_sayisi
FROM odunc o
JOIN uyeler u ON o.uye_id = u.id
JOIN kitaplar k ON o.kitap_id = k.kitap_id;


--- 30 gun kosulu eklenmıs halı 

SELECT 
    u.ad AS uye_adi,
    k.kitap_adi,
    o.gun AS gun_sayisi
FROM odunc o
JOIN uyeler u ON o.uye_id = u.id
JOIN kitaplar k ON o.kitap_id = k.kitap_id
WHERE o.gun > 30;

SELECT 
    u.ad AS uye_adi,
    u.sehir,
    k.kitap_adi,
    o.gun
FROM odunc o
JOIN uyeler u ON o.uye_id = u.id
JOIN kitaplar k ON o.kitap_id = k.kitap_id
WHERE u.sehir = 'Erzincan';

--- Hiç kitap almamış üyeleri de listede göstermek için hangi JOIN türü gerekir? 
--- left joın kullanmamız gerekıyor. 

SELECT 
    u.ad AS uye_adi,
    u.sehir,
    k.kitap_adi,
    o.gun
FROM uyeler u
LEFT JOIN odunc o ON u.id = o.uye_id
LEFT JOIN kitaplar k ON o.kitap_id = k.kitap_id;


---- Üyelerin Süre ve Kitap İstatistikleri (Ortalama > 20 Gün)
SELECT 
    u.ad AS uye_adi,
    AVG(o.gun) AS ortalama_gun,
    COUNT(o.kitap_id) AS alinan_kitap_sayisi,
    MAX(o.gun) AS en_uzun_gun
FROM uyeler u
JOIN odunc o ON u.id = o.uye_id
GROUP BY u.id, u.ad
HAVING AVG(o.gun) > 20;


---- SQL'in çalışma sırasında WHERE bloğu, gruplama (GROUP BY) yapılmadan önce satır bazında filtreleme yapar. AVG(), COUNT(), MAX() gibi toplama (aggregate) fonksiyonları ise gruplama yapıldıktan sonra hesaplanır. Gruplanmış verinin sonucuna (AVG(o.gun) > 20) dayalı bir filtreleme yapmak için gruplamadan sonra çalışan HAVING ifadesi kullanılmak zorundadır.


---- . Her Kitabın Kaç Kez Ödünç Alındığı
SELECT 
    k.kitap_adi,
    COUNT(o.uye_id) AS odunc_sayisi
FROM kitaplar k
LEFT JOIN odunc o ON k.kitap_id = o.kitap_id
GROUP BY k.kitap_id, k.kitap_adi;


----- Şehirlere Göre Üye Sayısı (Çoktan Aza)
SELECT 
    sehir,
    COUNT(*) AS uye_sayisi
FROM uyeler
GROUP BY sehir
ORDER BY uye_sayisi DESC;

---- En Az Bir Kitabı 30 Günden Uzun Tutmuş Üyeler (Alt Sorgu ile)
SELECT ad 
FROM uyeler 
WHERE id IN (
    SELECT uye_id 
    FROM odunc 
    WHERE gun > 30
);

---- Hiç Ödünç Alınmamış Kitaplar (NOT IN ile)
SELECT kitap_adi 
FROM kitaplar 
WHERE kitap_id NOT IN (
    SELECT DISTINCT kitap_id 
    FROM odunc 
    WHERE kitap_id IS NOT NULL
);

----Genel Ortalamanın Üzerinde Süre Tutulan Tüm Kayıtlar
SELECT 
    u.ad AS uye_adi,
    k.kitap_adi,
    o.gun
FROM odunc o
JOIN uyeler u ON o.uye_id = u.id
JOIN kitaplar k ON o.kitap_id = k.kitap_id
WHERE o.gun > (
    SELECT AVG(gun) 
    FROM odunc
);


-----Her Ödünç Kaydı İçin Durum Etiketi (CASE WHEN)
SELECT 
    uye_id,
    kitap_id,
    gun,
    CASE 
        WHEN gun > 30 THEN 'Gecikmiş'
        WHEN gun >= 15 THEN 'Uyarı'
        ELSE 'Normal'
    END AS durum
FROM odunc;
------Üyeleri Yaşına Göre Etiketleme (Genç / Yetişkin)
SELECT 
    id,
    ad,
    yas,
    CASE 
        WHEN yas <= 18 THEN 'Genç'
        ELSE 'Yetişkin'
    END AS yas_grubu
FROM uyeler;

-----(İleri) Her Durumdan Kaç Kayıt Olduğunu Sayma (CASE + GROUP BY)
SELECT 
    CASE 
        WHEN gun > 30 THEN 'Gecikmiş'
        WHEN gun >= 15 THEN 'Uyarı'
        ELSE 'Normal'
    END AS durum,
    COUNT(*) AS kayit_sayisi
FROM odunc
GROUP BY durum;


--------Index
--uyeler.ad Sütununda İndeks Oluşturma
CREATE INDEX idx_uyeler_ad ON uyeler(ad);
---eposta Sütunu Ekleme ve UNIQUE INDEX Tanımlama
-- Tabloya eposta sütununu ekleme
ALTER TABLE uyeler ADD COLUMN eposta TEXT;
-- Sütun üzerinde tekillik sağlayan UNIQUE indeks oluşturma
CREATE UNIQUE INDEX idx_uyeler_eposta_unique ON uyeler(eposta);

----İki Üyeye Aynı E-postayı Verme Denemesi ve Sonuç
-- Birinci üyeye e-posta atama (Başarılı)
UPDATE uyeler SET eposta = 'ornek@posta.com' WHERE id = 1;

-- İkinci üyeye aynı e-postayı atamayı deneme (Hata verir)
UPDATE uyeler SET eposta = 'ornek@posta.com' WHERE id = 2;