--TABLO OLUSTURMA

CREATE TABLE ogrenciler(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	ad TEXT NOT NULL,
	yas INTEGER CHECK (yas > 14 ),
	sehir TEXT DEFAULT 'Erzincan',
	kayit TEXT DEFAULT CURRENT_TIMESTAMP
);

--VERİ EKLEME İŞLEMLERİ

INSERT INTO ogrenciler(ad,yas) VALUES ('Zıpırcan',28);
INSERT INTO ogrenciler(ad,yas) VALUES('Tripcan',24);
INSERT INTO ogrenciler(ad,yas,sehir) VALUES('Yurdagül',23,'Gümüşhane'),('Zeynep',18,'Tokat');

--VERİ OKUMA 
SELECT * FROM ogrenciler;

SELECT ad,yas FROM ogrenciler WHERE yas > 20 ORDER BY yas DESC LIMIT 3;

SELECT * FROM ogrenciler WHERE ad LIKE 'z%';

-- Guncelleme ve Silme
UPDATE ogrenciler SET yas = 21 Where ad='Zeynep';

DELETE FROM ogrenciler Where id=2;

ALTER TABLE ogrenciler ADD COLUMN eposta TEXT;

ALTER TABLE ogrenciler RENAME COLUMN sehir to il;
