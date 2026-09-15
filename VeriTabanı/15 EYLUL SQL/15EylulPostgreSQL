CREATE TABLE bolum(
	id SERIAL PRIMARY KEY ,
	ad VARCHAR(50) NOT NULL
);

CREATE TABLE ogrenci(
	identify SERIAL PRIMARY KEY,
	ad VARCHAR(50),
	not_ort NUMERIC (4,2)
);

CREATE TABLE ders(

	id SERIAL PRIMARY KEY,
	ad VARCHAR(100) NOT NULL,
	kredi INT,
	bolum_id INT REFERENCES bolum(id)
);

CREATE TABLE kayit(
	ogrenci_id INT REFERENCES ogrenci(identify) ON DELETE CASCADE,
	ders_id INT REFERENCES ders(id) ON DELETE CASCADE,
	notu INT,
	donem VARCHAR(25),
	PRIMARY KEY (ogrenci_id,ders_id)
);


---eskı---------------------

ALTER TABLE ogrenci ADD COLUMN bolum VARCHAR(50);

--veri işlemlerinde 

INSERT INTO ogrenci(ad,not_ort) VALUES ('Zıpırcan',68.3);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Cırcırböceği Cemal', 42.1);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Makyajlı Muhtar', 88.9);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Çorapsız Çetin', 50.0);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Gözlüklü Gönül', 95.4);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Tostçu Tayfun', 31.8);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Biberli Bedriye', 74.2);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Hapşıran Hikmet', 61.7);
INSERT INTO ogrenci (ad, not_ort) VALUES ('Lastik Lütfü', 22.3);

SELECT * FROM ogrenci WHERE not_ort> 60 ORDER BY ad;

UPDATE ogrenci SET  not_ort=60 WHERE identify =2;

select * FROM ogrenci;

DELETE FROM ogrenci WHERE identify = 1 ;

SELECT * FROM ogrenci ORDER BY identify;

----------------------------------------------------------------------------


-- 1. BÖLÜM VERİLERİ
INSERT INTO bolum (id, ad) VALUES
(1, 'Şanssızlık Mühendisliği'),
(2, 'Dedikodu Bilimleri ve Stratejik Fısıltı'),
(3, 'Uykusuzluk ve Gece 3 Mesajları Anabilim Dalı'),
(4, 'Fast Food Felsefesi ve Ketçap Yönetimi');

-- 2. ÖĞRENCİ VERİLERİ
INSERT INTO ogrenci (ad, not_ort) VALUES
('Zıpırcan', 68.30),
('Cırcırböceği Cemal', 42.10),
('Pırtlayan Pınar', 12.50),
('Makyajlı Muhtar', 88.90),
('Çorapsız Çetin', 50.00),
('Tostçu Tayfun', 31.80),
('Biberli Bedriye', 74.20),
('Hapşıran Hikmet', 61.70);

-- 3. DERS VERİLERİ
INSERT INTO ders (ad, kredi, bolum_id) VALUES
('Kopya Çekme Teknikleri 101', 4, 1),
('Açık Unutulan Muslukları Kapatma Sanatı', 3, 1),
('Yan Masadakinin Konuşmasını Dinleme ve Raporlama', 5, 2),
('Sabah 8.00 Dersine Gidiyormuş Gibi Görünme', 2, 3),
('Ketçap ve Mayonez Dökülme Risk Analizi', 4, 4),
('Sosyal Medyada Eski Sevgilinin Profilini İnceleme', 3, 2);

-- 4. KAYIT (NOT VE DÖNEM) VERİLERİ
INSERT INTO kayit (ogrenci_id, ders_id, notu, donem) VALUES
(1, 1, 45, '2025-Güz'),
(1, 2, 70, '2025-Güz'),
(2, 3, 90, '2025-Güz'),
(3, 4, 15, '2026-Bahar'),
(4, 5, 88, '2026-Bahar'),
(5, 1, 50, '2025-Güz'),
(6, 5, 30, '2026-Bahar'),
(7, 6, 95, '2026-Bahar'),
(8, 2, 62, '2025-Güz');

--------- hangı ogrencı hangı dersı almıs notu kaç 
SELECT o.ad AS ogrenci , d.ad AS Ders , k.notu
FROM kayit k
JOIN ogrenci o on k.ogrenci_id = o.identify
JOIN ders d ON k.ders_id = d.id
ORDER BY o.ad , k.notu DESC

---------- bölüm bazında ders ortalaması 
SELECT b.ad as bolum , d.ad as ders, AVG (k.notu) as ort
from kayit k
join ders d on k.ders_id = d.id
join bolum b on k.bolum_id = b.id


-----her ogrencının aldıgı kredı
SELECT 
    o.ad AS ogrenci, 
    SUM(d.kredi) AS toplam_kredi
FROM kayit k
JOIN ogrenci o ON k.ogrenci_id = o.identify
JOIN ders d ON k.ders_id = d.id
GROUP BY o.identify, o.ad
ORDER BY toplam_kredi DESC;




--------subquery not ortalama genel ortalamaların ustunde olan ogrencıler
select ad , not_ort
from ogrenci
where not_ort>(select avg(not_ort)from ogrenci)
order by not_ort desc


-----en cok ders alan ogrencı
SELECT 
    o.ad AS ogrenci, 
    COUNT(k.ders_id) AS alinan_ders_sayisi
FROM kayit k
JOIN ogrenci o ON k.ogrenci_id = o.identify
GROUP BY o.identify, o.ad
ORDER BY alinan_ders_sayisi DESC
LIMIT 1;

------------harf notu ogrenelım ıf else case end 
select o.ad,
	case 
		when avg(k.notu)>=90 then 'aa'
		when avg(k.notu)>= 80 then 'bb'
		when avg (k.notu)>=70 then 'cc'
		else 'f'
	end as harf_notu
from ogrenci o 
join kayit k on o.identify = k.ogrenci_id
group by o.identify, o.ad;

----- her ogrencının derslere kacıncı geldıgını gosterır 
select o.ad, d.ad as ders, k.notu,
	row_number() over (PARTITION by k.ders_id order by k.notu desc) as siralama
from ogrenci o 
join kayit k on o.identify= k.ogrenci_id
join ders d on k.ders_id = d.id;

---ogrenci başına toplam kredi ve sınıfın kredi ortalaması
WITH ogrenci_kredileri AS (
    SELECT 
        o.identify,
        o.ad AS ogrenci,
        SUM(d.kredi) AS ogrenci_toplam_kredi
    FROM kayit k
    JOIN ogrenci o ON k.ogrenci_id = o.identify
    JOIN ders d ON k.ders_id = d.id
    GROUP BY o.identify, o.ad
)
SELECT 
    ogrenci,
    ogrenci_toplam_kredi,
    ROUND(AVG(ogrenci_toplam_kredi) OVER(), 2) AS sinif_kredi_ortalamasi
FROM ogrenci_kredileri
ORDER BY ogrenci_toplam_kredi DESC;


SELECT
o.ad AS ogrenci_adi,
SUM(d.kredi) AS ogrenci_toplam_kredisi,
ROUND(AVG(SUM(d.kredi)) OVER(), 2) AS sinif_kredi_ortalamasi
FROM ogrenci o
JOIN kayit k ON o.identify = k.ogrenci_id
JOIN ders d ON k.ders_id = d.id
GROUP BY o.identify, o.ad
ORDER BY ogrenci_toplam_kredisi DESC;

--- cte with common table expression 
-- önce ogrencı ortalamasını hesapla sonra kullan 

with ogrenci_ort as (
	select o.identify, o.ad , AVG(k.notu) as ort 
	from ogrenci o 
	join kayit k on o.identify=k.ogrenci_id
	group by o.identify, o.ad 
)
SELECT * FROM ogrenci_ort where ort>80 order by ort desc;


-- kaç farklı derse not verılmıstır 
SELECT DISTINCT ders_id FROM kayit;



---- ders başına istatiklre 
SELECT d.ad,
	COUNT (k.ogrenci_id) as ogrenci_sayisi,
	AVG	(k.notu) as ort_not,
	MIN (k.notu) as en_dusuk,
	MAX (k.notu) as en_yuksek,
	STDDEV (k.notu) as standart_sapma
	from ders d 
	left join kayit k on d.id = k.ders_id 
	group by d.id, d.ad
	order by ort_not desc
	
