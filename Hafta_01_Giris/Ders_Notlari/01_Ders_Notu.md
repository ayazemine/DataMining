# Hafta 1: Veri Madenciliğine Giriş

## 📋 Hafta Hedefleri
Bu hafta sonunda öğrenciler:
- Veri madenciliğinin tanımını, amacını ve kapsamını detaylıca öğrenecek
- Veri madenciliği sürecini (CRISP-DM ve KDD) adım adım anlayacak
- Temel veri madenciliği görevlerini ve algoritmalarını tanıyacak
- Veri madenciliğinin diğer disiplinlerle (İstatistik, ML, AI) ilişkisini kavrayacak
- Güncel uygulama alanları ve etik boyutlarını irdeleyecek

## 📚 Teorik İçerik (2 saat)

### 1. Veri Madenciliği Nedir?

**Tanım 1 (Akademik):** Veri madenciliği (Data Mining), büyük ölçekli veri setleri içerisinden gizli, önceden bilinmeyen, potansiyel olarak yararlı ve anlaşılabilir örüntülerin (patterns) otomatik veya yarı-otomatik yöntemlerle keşfedilmesi sürecidir. Bu süreç genellikle "Knowledge Discovery in Databases" (KDD) olarak da adlandırılır.

**Tanım 2 (İş Dünyası):** Veri madenciliği, ham veriyi iş kararlarını destekleyecek eyleme dönüştürülebilir "bilgiye" (actionable insight) çevirme sanatıdır.

**Anahtar Kavramlar:**
- **Büyük Veri (Huge Data):** Terabaytlarca veri üzerinde çalışabilme.
- **Gizli Örüntüler (Hidden Patterns):** Çıplak gözle veya basit sorgularla (SQL) görülemeyen ilişkiler.
- **Önceden Bilinmeyen (Non-trivial):** Sonuçlar aşikar olmamalıdır (Örn: "Hamile kadınlar hastaneye gider" bir veri madenciliği bulgusu değildir).
- **Yararlı (Useful):** Bulunan bilgi bir değer yaratmalı veya bir problemi çözmelidir.
- **Anlaşılabilir (Understandable):** Sonuçlar insan tarafından yorumlanabilir olmalıdır.

![datamining](https://www.netsuite.com/portal/assets/img/business-articles/data-warehouse/social-data-mining.jpg?v2)

#### Disiplinlerarası İlişkiler
- **İstatistik:** Veri madenciliğinin temelidir. Hipotez testleri, dağılımlar ve olasılık teorisini sağlar. İstatistik genellikle model odaklıdır (veriyi modele uydurur), veri madenciliği ise veri odaklıdır (modeli veriye uydurur) ve daha büyük veri setleriyle ilgilenir.
- **Makine Öğrenmesi (Machine Learning):** Veri madenciliğinin "motorudur". Algoritmaları (karar ağaçları, sinir ağları vb.) sağlar. Veri madenciliği bu algoritmaları kullanarak "bilgi keşfine" odaklanırken, makine öğrenmesi "tahmin ve öğrenme" performansına odaklanır.
- **Veritabanı Sistemleri:** Verinin saklanması, indekslenmesi ve hızlı erişimi için gereklidir.
- **Yapay Zeka (AI):** En geniş kümedir. İnsan zekasını taklit eden sistemlerdir. Veri madenciliği, AI'nın öğrenme ve çıkarım yapma yeteneklerini kullanır.

::: info
**Özet:** Veri Tabanları veriyi **saklar**, İstatistik veriyi **sayısal olarak özetler**, Makine Öğrenmesi veriden **öğrenir**, Veri Madenciliği ise tüm bunları kullanarak veriden **değerli bilgi keşfeder**.
:::

### 2. Veri Madenciliğinin Tarihçesi
- 1960-1970: İstatistiksel veri analizi
- 1980-1990: Veri tabanı sistemleri ve veri ambarları
- 1990-2000: Veri madenciliği kavramının ortaya çıkışı
- 2000-2010: Web madenciliği ve büyük veri
- 2010-Günümüz: Derin öğrenme ve yapay zeka çağı

### 3. Veri Madenciliği Süreç Modelleri

#### A. KDD (Knowledge Discovery in Databases) Süreci
![KDD](https://www.scaler.com/topics/images/kdd-in-data-mining-1.webp)

Veri madenciliği, KDD sürecinin sadece bir adımıdır. KDD süreci şu adımlardan oluşur:
1.  **Veri Temizleme (Data Cleaning):** Gürültü ve tutarsızlıkların giderilmesi.
2.  **Veri Bütünleştirme (Data Integration):** Farklı kaynakların birleştirilmesi.
3.  **Veri Seçimi (Data Selection):** Analizle ilgili verilerin seçilmesi.
4.  **Veri Dönüştürme (Data Transformation):** Verinin madencilik için uygun formata getirilmesi (normalizasyon vb.).
5.  **Veri Madenciliği (Data Mining):** Örüntüleri bulmak için akıllı algoritmaların uygulanması.
6.  **Örüntü Değerlendirme (Pattern Evaluation):** İlginçlik ölçütlerine göre örüntülerin değerlendirilmesi.
7.  **Bilgi Sunumu (Knowledge Presentation):** Görselleştirme ve raporlama.

#### B. CRISP-DM (Cross-Industry Standard Process for Data Mining)
Endüstride en yaygın kabul gören standarttır. Döngüsel bir süreçtir, yani bir proje bittiğinde elde edilen bilgiler yeni sorular doğurur.

![CRISP-DM](https://www.ist.fraunhofer.de/en/expertise/simulation-digital-services/data-acquisition-model-based-process-optimization/crisp-dm-surface-technology/jcr:content/contentPar/sectioncomponent/sectionParsys/wideimage/imageComponent/image.img.jpg/1713953737218/wi-crisp-en.jpg)

1.  **İş Anlayışı (Business Understanding):**
    - **Amaç:** Projenin ticari/bilimsel hedeflerini belirlemek.
    - **Sorular:** "Müşteri kaybını neden yaşıyoruz?", "Hangi ürünler birlikte satılıyor?"
    - **Çıktı:** Proje planı, başarı kriterleri.

2.  **Veri Anlayışı (Data Understanding):**
    - **Amaç:** Veriyi tanımak, kalitesini ölçmek.
    - **Eylemler:** Veri toplama, betimsel istatistik (ortalama, medyan), görselleştirme.
    - **Çıktı:** Veri kalitesi raporu.

3.  **Veri Hazırlama (Data Preparation) - *En çok zaman alan aşama (%60-80)*:**
    - **Amaç:** Model için temiz veri seti oluşturmak.
    - **Eylemler:** Eksik veri tamamlama, aykırı değer temizliği, öznitelik seçimi (feature selection), öznitelik mühendisliği (feature engineering).
    - **Çıktı:** Temizlenmiş eğitim ve test veri setleri.

4.  **Modelleme (Modeling):**
    - **Amaç:** Uygun algoritmaları uygulamak.
    - **Eylemler:** Algoritma seçimi (örn. Karar Ağacı vs. SVM), model eğitimi, parametre optimizasyonu.
    - **Çıktı:** Eğitilmiş modeller.

5.  **Değerlendirme (Evaluation):**
    - **Amaç:** Modelin iş hedeflerini karşılayıp karşılamadığını test etmek.
    - **Eylemler:** Accuracy, Precision, Recall gibi metriklerle ölçüm, A/B testleri.
    - **Çıktı:** Modelin başarısı hakkında karar (Deploy edelim mi?).

6.  **Dağıtım (Deployment):**
    - **Amaç:** Modeli canlı sisteme entegre etmek.
    - **Eylemler:** API oluşturma, rapor otomasyonu, model izleme (monitoring).
    - **Çıktı:** Canlı çalışan sistem.

### 4. Veri Madenciliği Görevleri ve Algoritmaları

Veri madenciliği görevleri genellikle iki ana kategoriye ayrılır:

#### A. Tanımlayıcı (Descriptive) Görevler
Mevcut veriyi özetleyerek ne olduğunu anlamaya çalışır. "Geçmişte ne oldu?" sorusuna odaklanır.

1.  **Kümeleme (Clustering):** Veri nesnelerini, grup içi benzerlik maksimum, gruplar arası benzerlik minimum olacak şekilde gruplara ayırma. Unsupervised (denetimsiz) bir yöntemdir.
    - *Örnek:* Müşteri segmentasyonu (VIP müşteriler, Fiyat odaklı müşteriler).
    - *Algoritmalar:* K-Means, DBSCAN, Hierarchical Clustering.
![clustering](https://miro.medium.com/1*JsfEdbXKwJw_Euprvx17KA.png)

2.  **Birliktelik Analizi (Association Analysis):** Veriler arasındaki sık tekrarlayan ilişkileri bulma. "Bunu alan şunu da aldı" mantığı.
    - *Örnek:* Market sepet analizi (Bebek bezi alan Bira da alıyor).
    - *Algoritmalar:* Apriori, FP-Growth.
![sepet-analizi](https://miro.medium.com/1*Jd_52SlGjmkqxXbIh_CLkg.png)

3.  **Sıralı Örüntü Madenciliği (Sequential Pattern Mining):** Zaman boyutunu içeren ilişkiler.
    - *Örnek:* Bilgisayar alan birinin 3 ay sonra yazıcı alması.

#### B. Tahmin Edici (Predictive) Görevler
Veriden bir model oluşturarak gelecekteki veya bilinmeyen verileri tahmin etmeye çalışır. Supervised (denetimli) yöntemlerdir.

1.  **Sınıflandırma (Classification):** Veriyi önceden tanımlanmış ayrık (kategorik) sınıflara atama.
    - *Örnek:* Bir e-postanın "Spam" veya "Normal" olarak etiketlenmesi.
    - *Algoritmalar:* Karar Ağaçları, Lojistik Regresyon, Naive Bayes, SVM, KNN, Random Forest.
![classification](https://makineogrenimi.wordpress.com/wp-content/uploads/2017/05/image_32.png?w=656)

2.  **Regresyon (Regression):** Sürekli sayısal bir değeri tahmin etme.
    - *Örnek:* Bir evin fiyatını tahmin etme, önümüzdeki ayki satış miktarını tahmin etme.
    - *Algoritmalar:* Lineer Regresyon, Random Forest Regresyon, SVR.

![reg](https://media.geeksforgeeks.org/wp-content/uploads/20231018110652/Regression-Line-copy.webp)

3.  **Anomali Tespiti (Anomaly/Outlier Detection):** Normal davranıştan sapan verileri bulma.
    - *Örnek:* Kredi kartı dolandırıcılığı, ağ saldırı tespiti, üretim bandındaki hatalı parça.
    - *Algoritmalar:* Isolation Forest, One-Class SVM.
![anomaly](https://linkurious.com/images/uploads/2024/01/Graph-and-anomaly-detection.png)

### 5. Uygulama Alanları ve Veri Tipleri

#### İş Dünyası
- **Pazarlama:** Müşteri segmentasyonu, sepet analizi
- **Bankacılık:** Kredi risk analizi, dolandırıcılık tespiti
- **Perakende:** Talep tahmini, fiyatlandırma optimizasyonu
- **E-Ticaret:** Ürün öneri sistemleri, churn prediction

#### Veri Tipleri Detaylı
- **Kategorik (Nitel) Veriler:**
    - **Nominal:** Sırasız (Renk: Kırmızı, Mavi).
    - **Ordinal:** Sıralı (Eğitim: Lise, Lisans).
- **Sayısal (Nicel) Veriler:**
    - **Interval (Aralık):** Mutlak sıfır yok (Sıcaklık).
    - **Ratio (Oran):** Mutlak sıfır var (Maaş, Boy).

### 6. Veri Madenciliğinde Zorluklar
- Veri kalitesi sorunları (Eksik, gürültülü veri)
- Büyük veri hacmi (Ölçeklenebilirlik)
- Yüksek boyutluluk (Curse of dimensionality)
- Karmaşık ve heterojen veri tipleri
- Gizlilik ve güvenlik
- Etik konular ve bias (yanlılık)

## 💻 Uygulama İçeriği (2 saat)

### Lab 1: Python Kurulumu ve Temel Veri Yapıları
### Lab 2: İlk Veri Analizi

## 📝 Ödevler

### Ödev 1: Araştırma Ödevi
Bir veri madenciliği uygulama örneği araştırın ve 2 sayfalık rapor hazırlayın.

### Ödev 2: Python Alıştırmaları
Temel Python veri yapıları ile pratik yapın.

## 📖 Okuma Listesi

### Zorunlu Okuma
- Han et al., Bölüm 1: Introduction
- Tan et al., Bölüm 1: Introduction

### Önerilen Okuma
- "Data Mining: What is Data Mining?" - Oracle White Paper
- "The CRISP-DM Model" - IBM SPSS Documentation

## 🎯 Değerlendirme Kriterleri
- Derse katılım: %20
- Lab çalışması: %40
- Ödevler: %40

## 📺 Video Kaynakları
- "What is Data Mining?" - StatQuest
- "CRISP-DM Process" - Data Science Dojo
- "Introduction to Data Science" - Harvard CS109

## ❓ Sıkça Sorulan Sorular

**S: Veri madenciliği ile makine öğrenmesi arasındaki fark nedir?**
C: Veri madenciliği daha geniş bir kavramdır ve veri keşfi, ön işleme, görselleştirme gibi tüm süreci kapsar. Makine öğrenmesi ise veri madenciliğinin model oluşturma kısmıdır.

**S: Python mi R mı öğrenmeliyim?**
C: Her ikisini de öğrenmenizi öneririz, ancak Python daha genel amaçlı ve endüstride daha yaygın kullanılır.

**S: Ne kadar matematik bilgisi gerekli?**
C: Temel istatistik, olasılık ve lineer cebir bilgisi yeterlidir. İleri konular için daha fazla matematik gerekebilir.

## 🔗 Faydalı Linkler
- [Kaggle](https://www.kaggle.com/) - Veri setleri ve kompetisyonlar
- [UCI ML Repository](https://archive.ics.uci.edu/ml/) - Standart veri setleri
- [scikit-learn](https://scikit-learn.org/) - Python ML kütüphanesi

---

**Sonraki Hafta:** Veri Kalitesi ve Ön İşleme
