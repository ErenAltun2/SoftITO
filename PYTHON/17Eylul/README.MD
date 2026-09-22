# 17 Eylül — Pandas'a Giriş

Veri analizinin temel kütüphanesi olan **pandas**'a giriş yapıldı: `Series`, `DataFrame` yapıları ve CSV dosyalarıyla çalışma öğrenildi.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `17EylulPython_CASELERI.ipynb` | Pandas alıştırmalarının çözüldüğü case notebook'u |
| `python_17_09_2026_DERS.ipynb` | Ders anlatımı sırasında işlenen örnekler (gerçek veri setleriyle: `grocery_chain_data.csv`, `Superlig_Proje.xlsx`) |

## 🎯 Konu Başlıkları

- **Pandas kurulumu ve içe aktarma:** `import pandas as pd`, `pd.__version__`
- **`Series` — tek boyutlu veri yapısı:**
  - Liste ve index'li (etiketli) Series oluşturma
  - Index adıyla eleman seçme
  - `.sum()` ile toplam alma
- **`DataFrame` — tablo yapısı:**
  - Sözlük (`dict`) veya kayıt listesi ile DataFrame oluşturma
  - `.shape` ile satır/sütun sayısını öğrenme
- **CSV dosyası okuma/yazma:**
  - `.to_csv()` ile dışa aktarma
  - `pd.read_csv()` ile içe aktarma
  - `index=False` parametresinin etkisi
- **Excel dosyası okuma:** `pd.read_excel()`
- **Veriye ilk bakış:** `.head()`, `.tail()`, `.info()`, `.describe()`, `.columns`

## 💡 Örnek

```python
urun_verisi = {
    "urun": ["Laptop", "Mouse", "Klavye"],
    "fiyat": [28500, 450, 1850],
    "stok": [15, 80, 35]
}
df_urunler = pd.DataFrame(urun_verisi)
print(df_urunler)
```

## ✅ Kazanımlar

- Pandas'ın iki temel veri yapısı olan `Series` ve `DataFrame`'i oluşturup kullanmayı öğrendim.
- CSV/Excel dosyalarını okuma ve dışa aktarma işlemlerini uyguladım.
- `index=False` gibi parametrelerin çıktı dosyasını nasıl etkilediğini gözlemledim.
