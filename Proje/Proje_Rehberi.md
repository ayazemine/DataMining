# Final Projesi - Veri Madenciliği Dersi

## 📋 Proje Açıklaması

Final projesi, dönem boyunca öğrenilen tüm veri madenciliği tekniklerinin gerçek bir veri seti üzerinde uygulanmasını içeren kapsamlı bir çalışmadır.

## 🎯 Proje Hedefleri

1. Gerçek dünya veri setiyle çalışma deneyimi kazanma
2. Veri madenciliği sürecinin tüm aşamalarını uygulama
3. Uygun algoritmaları seçme ve karşılaştırma
4. Sonuçları yorumlama ve raporlama
5. Takım çalışması ve proje yönetimi

## 👥 Grup Bilgileri

- **Grup Büyüklüğü:** 2-3 kişi
- **Grup Oluşturma:** Hafta 1-2

## 📅 Proje Takvimi

| Hafta | Milestone | Teslimat |
|-------|-----------|----------|
| 2 | Grup oluşturma | Grup listesi |
| 4 | Konu seçimi | Proje önerisi (1 sayfa) |
| 7 | Veri toplama ve EDA | Ara rapor |
| 10 | Model geliştirme | Kod + sonuçlar |
| 14 | Final sunumu | Rapor + kod + sunum |

## 📝 Proje Adımları

### 1. Problem Tanımlama (Hafta 2-4)

#### Konu Seçimi
Aşağıdaki kategorilerden birini seçin:
- **E-Ticaret:** Müşteri segmentasyonu, ürün önerisi, churn prediction
- **Sağlık:** Hastalık teşhisi, risk skorlaması
- **Finans:** Kredi risk analizi, dolandırıcılık tespiti
- **Sosyal Medya:** Duygu analizi, trend tahmini
- **Üretim:** Kalite kontrol, bakım tahmini
- **Serbest:** Kendi öneriniz (onay gerektirir)

#### Proje Önerisi İçeriği
```
1. Başlık
2. Problem tanımı (1 paragraf)
3. Veri kaynağı
4. Planlanan yöntemler
5. Beklenen sonuçlar
6. Grup üyeleri ve sorumluluklar
```

### 2. Veri Toplama (Hafta 4-5)

#### Veri Kaynakları
- Kaggle Datasets
- UCI ML Repository
- Açık veri portalleri
- Web scraping (etik kurallara uygun)
- Kamu verileri

#### Veri Gereksinimleri
- Minimum 1000 kayıt
- En az 5 öznitelik
- Anlamlı bir hedef değişken
- Yasal ve etik olarak uygun

### 3. Keşifsel Veri Analizi (Hafta 5-7)

#### Yapılacaklar
- Veri kalitesi değerlendirme
- Betimsel istatistikler
- Görselleştirmeler
- Korelasyon analizi
- Eksik değer analizi
- Aykırı değer tespiti

#### Ara Rapor İçeriği
```
1. Veri seti tanıtımı
2. Veri kalitesi raporu
3. EDA bulguları (grafiklerle)
4. Ön işleme planı
5. Sonraki adımlar
```

### 4. Veri Ön İşleme (Hafta 7-8)

- Eksik değer yönetimi
- Aykırı değer işleme
- Öznitelik mühendisliği
- Normalizasyon/Standardizasyon
- Encoding (label, one-hot)
- Train-test split

### 5. Model Geliştirme (Hafta 8-12)

#### Algoritma Seçimi
En az 3 farklı algoritma deneyin:
- Karar Ağaçları
- Random Forest
- k-NN
- Naïve Bayes
- SVM
- Lojistik Regresyon (binary için)

#### Model Eğitimi
```python
# Örnek yapı
from sklearn.model_selection import train_test_split, cross_val_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

models = {
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name}: {score:.3f}")
```

#### Hiperparametre Optimizasyonu
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

### 6. Model Değerlendirme (Hafta 12-13)

#### Metrikler
- Accuracy
- Precision, Recall, F1-Score
- ROC-AUC curve
- Confusion Matrix
- Cross-validation scores

#### Karşılaştırma
- Model performanslarını karşılaştırın
- En iyi modeli seçin
- Sonuçları yorumlayın

### 7. Raporlama ve Sunum (Hafta 13-14)

## 📊 Final Raporu Yapısı

### Rapor İçeriği (15-20 sayfa)

1. **Özet (Abstract)** - 1 paragraf
2. **Giriş** - 2 sayfa
   - Problem tanımı
   - Motivasyon
   - Amaç ve katkılar
3. **İlgili Çalışmalar** - 2 sayfa
   - Literatür taraması
   - Benzer çalışmalar
4. **Veri Seti** - 2 sayfa
   - Veri kaynağı
   - Veri tanıtımı
   - İstatistikler
5. **Yöntem** - 4-5 sayfa
   - Veri ön işleme
   - Öznitelik mühendisliği
   - Kullanılan algoritmalar
   - Hiperparametre ayarları
6. **Deneyler ve Sonuçlar** - 4-5 sayfa
   - Deney kurgusu
   - Sonuçlar (tablolar, grafikler)
   - Model karşılaştırmaları
7. **Tartışma** - 1-2 sayfa
   - Bulguların yorumu
   - Kısıtlamalar
   - İyileştirme önerileri
8. **Sonuç** - 1 sayfa
9. **Kaynaklar**
10. **Ekler** (Kod, ek tablolar)

### Rapor Formatı
- PDF formatı
- Times New Roman, 12pt
- 1.5 satır aralığı
- IEEE veya ACM format (şablon verilecek)

## 🎤 Sunum Gereksinimleri

- **Süre:** 15 dakika + 5 dakika soru-cevap
- **Format:** PowerPoint/PDF
- **İçerik:**
  - Problem ve motivasyon
  - Veri seti
  - Yöntem (özet)
  - Sonuçlar (grafiklerle)
  - Demo (varsa)
  - Sonuçlar ve gelecek çalışmalar

## 💻 Kod Teslimi

### Gereksinimler
- Jupyter Notebook veya Python script
- README.md (nasıl çalıştırılır)
- requirements.txt (bağımlılıklar)
- Temiz ve yorumlu kod
- GitHub repository (önerilen)

### Kod Yapısı
```
proje/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── preprocessing.py
│   └── models.py
├── results/
│   ├── figures/
│   └── models/
├── README.md
└── requirements.txt
```

## ✅ Değerlendirme Kriterleri

| Kriter | Puan | Açıklama |
|--------|------|----------|
| **Rapor** | **40** | |
| - Problem tanımı | 5 | Netlik ve uygunluk |
| - Veri analizi | 10 | EDA kalitesi |
| - Yöntem | 10 | Teknik detay |
| - Sonuçlar | 10 | Doğruluk ve yorumlama |
| - Yazım | 5 | Akademik yazım |
| **Kod** | **30** | |
| - Kod kalitesi | 15 | Temiz, yorumlu |
| - Çalışırlık | 10 | Hatasız çalışma |
| - Organizasyon | 5 | Dosya yapısı |
| **Sunum** | **20** | |
| - İçerik | 10 | Anlaşılırlık |
| - Sunum becerisi | 10 | Profesyonellik |
| **Yenilik** | **10** | |
| - Özgünlük | 5 | Farklı yaklaşım |
| - Derinlik | 5 | İleri analiz |
| **Toplam** | **100** | |

## 📚 Kaynaklar ve Şablonlar

### Rapor Şablonları
- IEEE Conference Template
- ACM Article Template
- [Overleaf](https://www.overleaf.com/) (LaTeX)

### Kod Örnekleri
- [Kaggle Kernels](https://www.kaggle.com/code)
- GitHub örnek projeler

### Sunum Şablonları
- [Slides Carnival](https://www.slidescarnival.com/)
- [Canva](https://www.canva.com/)

## 💡 İpuçları

1. **Erken başlayın:** Veri toplama ve temizleme zaman alır
2. **Düzenli toplantılar:** Haftalık grup toplantıları yapın
3. **Versiyon kontrolü:** Git kullanın
4. **Dokümantasyon:** Her adımı belgeleyin
5. **Danışman iletişimi:** Sorunlarda asistanınıza danışın
6. **Gerçekçi olun:** Çok karmaşık hedeflerden kaçının
7. **Sonuçları yorumlayın:** Sayılarla yetinmeyin, açıklayın

## ❓ SSS

**S: Veri setini nereden bulabilirim?**
C: Kaggle, UCI Repository, data.gov gibi sitelerden

**S: Grup üyelerinden biri çalışmıyorsa ne yapmalıyım?**
C: Asistanınızı bilgilendirin

**S: Rapor kaç sayfa olmalı?**
C: 15-20 sayfa (ekler hariç)

**S: Kodu hangi dilde yazmalıyım?**
C: Python tercih edilir, R de kabul edilir

**S: Demo zorunlu mu?**
C: Hayır ama ekstra puan kazandırabilir

## 📧 İletişim

- **Koordinatör:** ecengil@beu.edu.tr
- **Asistanlar:** [Liste]
- **E-posta:** ecengil@beu.edu.tr]
- **Ofis Saatleri:** Her hafta belirlenen saatler

## 🏆 Örnek Başarılı Projeler

1. **Netflix Film Öneri Sistemi** (2024)
2. **Kredi Kartı Dolandırıcılık Tespiti** (2024)
3. **Twitter Duygu Analizi - Seçim Tahmini** (2023)
4. **E-Ticaret Müşteri Segmentasyonu** (2023)

---

**Başarılar Dileriz!** 🎓🚀
