--BOILUM 1
CREATE TABLE Oyuncaklar(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	isim TEXT NOT NULL, 
	cesit TEXT,
	fiyat INTEGER CHECK (fiyat > 0),
	renk TEXT DEFAULT 'kırmızı'
)

-- eklemek ıslemlerı ınsert ınto ıleydı BOLUM 2
INSERT INTO Oyuncaklar(isim,cesit,fiyat) VALUES ('Şimşek','araba',50);

INSERT INTO Oyuncaklar (isim,cesit,fiyat,renk) VALUES 
('Ayıcık','peluş',80,'kahverengi'),
('Kale Seti','lego',150,'gri'),
('Zıpzıp','top',20,'sarı'),
('Barbi','bebek',90,'pembe');

--bolum 3 bulmak 
SELECT * FROM Oyuncaklar

SELECT isim,fiyat FROM Oyuncaklar Where fiyat >= 80;

SELECT * FROM Oyuncaklar ORDER BY fiyat DESC LIMIT 2;

SELECT * FROM Oyuncaklar Where isim LIKE 'Z%';

SELECT * FROM Oyuncaklar Where cesit = 'araba' or cesit= 'top'; -- veya in ıfadesını kullanarak ıcermek anlamı verebılırdık 

SELECT * FROM Oyuncaklar Where fiyat>20 AND fiyat<60;

--BOLUM 4 DEGISTIRME VE SILME ISLEMLERI 

UPDATE Oyuncaklar SET renk='mavi' WHERE isim='Şimşek';

DELETE FROM Oyuncaklar WHERE isim='Zıpzıp';

DELETE FROM Oyuncaklar;

--Bölüm5 tobloyu duzenleme

ALTER TABLE Oyuncaklar ADD COLUMN kimin TEXT;

UPDATE Oyuncaklar SET kimin ='Ali' WHERE isim='Kale Seti';

ALTER TABLE Oyuncaklar RENAME COLUMN cesit To tur;

