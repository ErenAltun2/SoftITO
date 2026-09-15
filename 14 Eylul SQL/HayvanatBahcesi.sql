CREATE TABLE hayvanlar(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	isim TEXT NOT NULL,
	tur TEXT,
	yas INTEGER CHECK (yas > 0),
	renk TEXT DEFAULT 'Kahverengi'
);

INSERT INTO hayvanlar (isim,tur,yas,renk) VALUES
('Pamuk', 'kedi', 3, 'beyaz'),
('Duman', 'kedi', 4, 'gri'),
('Zeytin', 'köpek', 2, 'siyah'),
('Boncuk', 'kuş', 2, 'mavi'),
('Fıstık', 'kuş', 1, 'yeşil'),
('Şanslı', 'köpek', 6, 'kahverengi'),
('Gölge', 'kedi', 5, 'siyah'),
('Mercan', 'balık', 1, 'kırmızı'),
('Bulut', 'köpek', 3, 'beyaz'),
('Ateş', 'kedi', 2, 'turuncu'),
('Çikolata', 'köpek', 4, 'kahverengi'),
('Limon', 'kuş', 1, 'sarı'),
('Kömür', 'kedi', 3, 'siyah'),
('Sakız', 'tavşan', 1, 'beyaz'),
('Gümüş', 'balık', 2, 'gri'),
('Çoşku', 'kuş', 3, 'yeşil'),
('Poyraz', 'köpek', 7, 'gri'),
('Findik', 'sincap', 2, 'kahverengi'),
('Ceviz', 'köpek', 4, 'kahverengi'),
('Gece', 'kedi', 1, 'siyah');

SELECT * FROM hayvanlar;
SELECT isim,yas FROM hayvanlar Where yas >= 5;
SELECT * FROM hayvanlar ORDER BY yas DESC LIMIT 2;
SELECT * FROM hayvanlar Where isim LIKE 'K%';
SELECT * FROM hayvanlar Where yas BETWEEN 5 AND 7;

UPDATE hayvanlar SET yas=9 WHERE isim = 'Poyraz';

DELETE FROM hayvanlar WHERE isim = 'Boncuk';

ALTER TABLE hayvanlar ADD COLUMN sevdigi_yemek TEXT;
UPDATE hayvanlar SET sevdigi_yemek = 'havuç' WHERE isim = 'Sakız';
