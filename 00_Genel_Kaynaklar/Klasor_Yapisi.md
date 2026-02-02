# Veri Madenciliği Dersi - Klasör Yapısı

## 📁 Tüm Klasör ve Dosya Yapısı

```
Veri_Madenciliği_Ders_Dokümanı/
│
├── README.md                           # Genel tanıtım ve başlangıç rehberi
├── context.md                          # Ders bağlamı ve genel bilgiler
│
├── 00_Genel_Kaynaklar/                # Tüm ders boyunca kullanılacak kaynaklar
│   ├── Ders_Programi.md               # Detaylı haftalık program
│   ├── Kurulum_Rehberi.md             # Python/R kurulum talimatları
│   ├── Kaynakca.md                    # Kitaplar, makaleler, linkler
│   ├── Sozluk.md                      # Terimler sözlüğü
│   ├── SSS.md                         # Sıkça sorulan sorular
│   ├── Python_Cheat_Sheet.md          # Hızlı referans kodu
│   └── Jupyter_Notebook_Sablonu.py    # Standart notebook şablonu
│
├── Veri_Setleri_Genel/                # Genel veri setleri koleksiyonu
│   ├── README.md                      # Veri setleri hakkında bilgi
│   ├── iris.csv
│   ├── titanic.csv
│   ├── wine_quality.csv
│   └── [diğer veri setleri]
│
├── Proje/                             # Final projesi materyalleri
│   ├── Proje_Rehberi.md              # Detaylı proje talimatları
│   ├── Proje_Sablonu/                # Proje şablonu
│   └── Ornek_Projeler/               # Geçmiş başarılı projeler
│
├── Hafta_01_Giris/                    # Hafta 1: Veri Madenciliğine Giriş
│   ├── Ders_Notlari/
│   │   └── 01_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_python_temelleri.py
│   │   └── lab1_notebook.ipynb
│   ├── Odevler/
│   │   ├── Odev1_Arastirma.md
│   │   └── Odev2_Python_Alistirmalari.md
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│       └── ek_okuma.md
│
├── Hafta_02_Veri_On_Isleme/          # Hafta 2: Veri Ön İşleme
│   ├── Ders_Notlari/
│   │   └── 02_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_pandas_temizleme.py
│   │   ├── lab2_normalizasyon.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   │   ├── Odev1_Veri_Temizleme.md
│   │   └── Odev2_Pandas_Alistirmalari.md
│   ├── Veri_Setleri/
│   │   └── dirty_data.csv
│   └── Kaynaklar/
│
├── Hafta_03_EDA/                      # Hafta 3: Keşifsel Veri Analizi
│   ├── Ders_Notlari/
│   │   └── 03_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_matplotlib.py
│   │   ├── lab2_seaborn.py
│   │   └── lab3_eda_project.ipynb
│   ├── Odevler/
│   │   ├── Odev1_EDA_Raporu.md
│   │   └── Odev2_Gorsellestirme.md
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│
├── Hafta_04_Karar_Agaclari/          # Hafta 4: Karar Ağaçları
│   ├── Ders_Notlari/
│   │   └── 04_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_decision_tree.py
│   │   ├── lab2_pruning.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   │   ├── Odev1_Manuel_Hesaplama.md
│   │   └── Odev2_Sklearn_Uygulama.md
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│
├── Hafta_05_Kural_ve_KNN/            # Hafta 5: Kural Çıkarımı ve k-NN
│   ├── Ders_Notlari/
│   │   └── 05_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_apriori.py
│   │   ├── lab2_knn.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│
├── Hafta_06_NB_SVM_YSA/              # Hafta 6: Naïve Bayes, SVM, YSA
│   ├── Ders_Notlari/
│   │   └── 06_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_naive_bayes.py
│   │   ├── lab2_svm.py
│   │   └── lab3_neural_network.py
│   ├── Odevler/
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│
├── Hafta_07_Ensemble/                # Hafta 7: Ensemble ve Değerlendirme
│   ├── Ders_Notlari/
│   │   └── 07_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_random_forest.py
│   │   ├── lab2_xgboost.py
│   │   └── lab3_model_comparison.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│
├── Hafta_08_Birliktelik/             # Hafta 8: Birliktelik Kuralları
│   ├── Ders_Notlari/
│   │   └── 08_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_market_basket.py
│   │   ├── lab2_fp_growth.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   │   └── online_retail.csv
│   └── Kaynaklar/
│
├── Hafta_09_Kumeleme/                # Hafta 9: Kümeleme Algoritmaları
│   ├── Ders_Notlari/
│   │   └── 09_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_kmeans.py
│   │   ├── lab2_hierarchical.py
│   │   ├── lab3_dbscan.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   │   └── customer_segmentation.csv
│   └── Kaynaklar/
│
├── Hafta_10_Anomali/                 # Hafta 10: Aykırı Değer Tespiti
│   ├── Ders_Notlari/
│   │   └── 10_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_lof.py
│   │   ├── lab2_isolation_forest.py
│   │   └── lab3_fraud_detection.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   │   └── credit_card_fraud.csv
│   └── Kaynaklar/
│
├── Hafta_11_Metin_Madenciligi/       # Hafta 11: Metin Madenciliği
│   ├── Ders_Notlari/
│   │   └── 11_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_text_preprocessing.py
│   │   ├── lab2_sentiment_analysis.py
│   │   ├── lab3_topic_modeling.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   │   ├── twitter_data.csv
│   │   └── imdb_reviews.csv
│   └── Kaynaklar/
│
├── Hafta_12_Web_Madenciligi/         # Hafta 12: Web Madenciliği
│   ├── Ders_Notlari/
│   │   └── 12_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_web_scraping.py
│   │   ├── lab2_beautifulsoup.py
│   │   ├── lab3_selenium.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│       └── etik_kurallar.md
│
├── Hafta_13_Buyuk_Veri/              # Hafta 13: Büyük Veri Teknolojileri
│   ├── Ders_Notlari/
│   │   └── 13_Ders_Notu.md
│   ├── Uygulama/
│   │   ├── lab1_pyspark_intro.py
│   │   ├── lab2_mapreduce.py
│   │   ├── lab3_spark_ml.py
│   │   └── lab_notebook.ipynb
│   ├── Odevler/
│   ├── Veri_Setleri/
│   └── Kaynaklar/
│       └── spark_kurulum.md
│
├── Hafta_14_Proje_Sunumlari/        # Hafta 14: Proje Sunumları
│   ├── Sunum_Takvimi.md
│   ├── Degerlendirme_Formu.pdf
│   └── Ornek_Sunumlar/
│
└── Hafta_05-14_Ozet/                 # Hafta 5-14 özet içerikler
    └── Haftalik_Icerik_Ozeti.md
```

## 📊 İstatistikler

- **Toplam Hafta:** 14
- **Teorik Ders Saati:** 28 saat (14 × 2)
- **Lab Uygulaması:** 28 saat (14 × 2)
- **Toplam Saat:** 56 saat
- **Ödev Sayısı:** ~20-25
- **Lab Çalışması:** 40+
- **Proje:** 1 (grup)

## 🎯 Her Hafta Klasörün İçeriği

### Standart Yapı
Her hafta klasörü aşağıdaki alt klasörleri içerir:

1. **Ders_Notlari/**
   - Markdown formatında teorik ders notları
   - Kavramlar, algoritmalar, formüller
   - Örnekler ve açıklamalar

2. **Uygulama/**
   - Python script dosyaları (.py)
   - Jupyter Notebook dosyaları (.ipynb)
   - Hands-on kod örnekleri

3. **Odevler/**
   - Haftalık ödev talimatları
   - Alıştırma soruları
   - Proje şablonları

4. **Veri_Setleri/**
   - İlgili haftaya özel veri setleri
   - CSV, Excel veya diğer formatlar

5. **Kaynaklar/**
   - Ek okuma materyalleri
   - Makale linkleri
   - Video kaynakları
   - Faydalı web siteleri

## 🔍 Dosya Adlandırma Kuralları

- **Markdown dosyaları:** `lowercase_with_underscores.md`
- **Python scripts:** `lab1_descriptive_name.py`
- **Notebooks:** `lab_notebook.ipynb` veya `topic_name.ipynb`
- **Veri setleri:** `dataset_name.csv`
- **Ödevler:** `Odev1_Konu.md`

## 📱 Navigasyon İpuçları

### Hızlı Erişim
- Her hafta README.md'den başlayın
- Önce ders notlarını okuyun
- Sonra uygulamalara geçin
- Ödevleri son bırakmayın

### Arama
- VS Code: `Ctrl+P` ile dosya ara
- Terminal: `find . -name "*.py"` (Linux/Mac)
- Windows: `dir /s *.ipynb` (dosya ara)

### Git İle Takip
```bash
# Tüm dosyaları track et
git add .
git commit -m "Hafta X tamamlandı"
git push
```

## 💡 Öneriler

1. **Sıralı İlerleyin:** Haftaları sırayla takip edin
2. **Kod Çalıştırın:** Her kodu mutlaka çalıştırın
3. **Notlar Alın:** Kendi notlarınızı ekleyin
4. **Projeler Yapın:** Kendi mini projelerinizi oluşturun
5. **Yedekleyin:** Düzenli olarak yedek alın

## 🔄 Güncelleme Politikası

Bu klasör yapısı:
- Dönem başında tamamlanır
- Haftalık güncellemeler yapılır
- Öğrenci geri bildirimine göre iyileştirilir
- Her dönem revize edilir

## 📞 Yardım

Klasör yapısı veya dosyalar hakkında sorularınız için:
- **E-posta:** [ders_hocasi@universite.edu.tr]
- **Ofis Saatleri:** Pazartesi-Çarşamba 14:00-16:00

---

**Son Güncelleme:** Şubat 2026
**Versiyon:** 1.0
