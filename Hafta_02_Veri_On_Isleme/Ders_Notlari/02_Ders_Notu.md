# Hafta 2: Veri Ön İşleme ve Veri Kalitesi

## 📋 Hafta Hedefleri
- Veri kalitesi problemlerini tanımlama
- Veri temizleme tekniklerini öğrenme
- Eksik veri yönetim stratejilerini uygulama
- Veri dönüştürme ve normalizasyon yapabilme
- Pandas kütüphanesi ile pratik veri işleme

## 📚 Teorik İçerik

### 1. Veri Kalitesi (Data Quality)

Veri madenciliğinin başarısı, kullanılan verinin kalitesine doğrudan bağlıdır ("Garbage In, Garbage Out"). Kaliteli veri, amaca uygunluğu ifade eder.

#### Veri Kalitesi Boyutları (6 Temel Boyut)
Veri kalitesi genellikle 6 ana boyutta değerlendirilir:

![datadimension](https://images.ctfassets.net/7p3vnbbznfiw/7nxnoLC5va86n2dYIqoCdJ/c468ee8c8d25d0b702abdac2ba53a486/6.-6-elements-of-data-quality--1024x768.png)

1.  **Tamlık (Completeness):** 
    - Bir veri setindeki eksik verilerin yüzdesi, tamlığı belirlemek için kullanılır.
    - *Not:* Mal ve hizmetlere ilişkin verilerin doğruluğu, potansiyel alıcıların satış kalemlerini değerlendirmesi, karşılaştırması ve seçmesi için de esastır.

2.  **Güncellik (Timeliness):** 
    - Verinin herhangi bir zamanda ne kadar güncel veya eski olduğunu ifade eder.
    - *Örnek:* Müşteri verileriniz 2008 yılına aitse ve şu an 2021 yılındaysanız, güncellik ile ilgili ciddi bir sorun vardır.

3.  **Geçerlilik (Validity):** 
    - Belirli firma politikalarına, prosedürlerine veya formatlarına uymayan veriler geçersiz kabul edilir.
    - *Örnek:* Bir müşterinin doğum tarihi birçok sistem tarafından istenebilir. Ancak tüketici doğum tarihini yanlış formatta veya imkansız bir tarih olarak girerse, veri kalitesi doğrudan etkilenir.

4.  **Bütünlük (Integrity):** 
    - Bilginin ne kadar güvenilir (dependable) ve itimat edilir (trustworthy) olduğu veri bütünlüğü olarak adlandırılır.
    - *Soru:* Elimizdeki gerçekler ve istatistikler ne kadar doğru ve güvenilirdir?

5.  **Benzersizlik (Uniqueness):** 
    - Müşteri profilleriyle en sık ilişkilendirilen veri kalitesi niteliğidir.
    - Uzun vadeli karlılık ve başarı, genellikle her tüketiciye bağlı performans ölçümleri dahil olmak üzere, benzersiz müşteri verilerinin hatasız derlenmesine dayanır (Mükerrer kayıtların olmaması).

6.  **Tutarlılık (Consistency):** 
    - Analitik çalışmalar en sık veri tutarlılığı ile ilişkilendirilir.
    - Bilgi toplama kaynağının, departmanın veya şirketin belirli hedeflerine uygun olarak verileri doğru bir şekilde edindiğini ve farklı kaynaklar arasında çelişki olmadığını garanti eder.

#### Temel Veri Sorunları
1.  **Gürültü (Noise):** Veri içindeki rastgele hatalar veya varyans. (Örn: Sensör ısınması nedeniyle GPS sinyalindeki 2 metrelik sapma).
2.  **Aykırı Değerler (Outliers):** Verinin genel dağılımından istatistiksel olarak çok sapan değerler. (Örn: Ortalama maaşın 20.000 TL olduğu bir grupta bir kişinin 1.000.000 TL alması).
3.  **Eksik Değerler (Missing Values):** Kaydedilmemiş veriler. En sık karşılaşılan problemdir.

### 2. Eksik Değerler (Missing Values)

Eksik veriyi yönetmek için öncelikle **nedenini** anlamak gerekir. Körlemesine doldurma yapmak (imputation) yanlılığa (bias) yol açabilir.

#### Eksiklik Mekanizmaları
1.  **MCAR (Missing Completely At Random - Tamamen Rastgele):**
    - Eksiklik verinin kendisinden veya diğer değişkenlerden bağımsızdır.
    - *Örnek:* Laboratuvarda numune taşıyan tüpün yanlışlıkla kırılması.
    - *Analiz:* Veri kaybı sadece örneklem boyutunu azaltır, sonucu çarpıtmaz (unbiased).

2.  **MAR (Missing At Random - Rastgele):**
    - Eksiklik, veri setindeki diğer gözlemlenen değişkenlerle açıklanabilir.
    - *Örnek:* Erkeklerin depresyon anketini doldurma olasılığının kadınlara göre daha düşük olması. Burada eksiklik "Cinsiyet" değişkeni ile ilişkilidir.
    - *Çözüm:* Diğer değişkenleri kullanarak tahminleme (Imputation) yapılmalıdır.

3.  **MNAR (Missing Not At Random - Rastgele Olmayan):**
    - Eksiklik, eksik olan değerin kendisiyle ilişkilidir.
    - *Örnek:* Obezite anketinde, kilosu çok yüksek olan kişilerin kilo bilgisini girmemesi.
    - *Analiz:* En zor durumdur. Doldurma yapmak sonucu bozabilir. Özel modelleme gerekir.

#### Eksik Veri ile Başa Çıkma Stratejileri

**A. Silme (Deletion)**
- **Listwise (Satır Silme):** En az bir hücresi eksik olan satırı tamamen sil. Veri kaybı az ise (%5 altı) ve durum MCAR ise uygundur.
- **Pairwise:** Sadece analiz edilen iki değişken (korelasyon vb.) doluysa kullan, diğerlerini yok say.
- **Dropping Features (Sütun Silme):** Bir sütunun büyük çoğunluğu (%60-70+) boşsa o özelliği analizden çıkarmak.

**B. Doldurma (Imputation)**
- **İstatistiksel Yöntemler:** Sayısal veriler için Ortalama/Medyan, kategorik veriler için Mod (en sık tekrar eden) atama. Basittir ancak verinin varyansını yapay olarak düşürür.
- **Zaman Serisi Yöntemleri:** Bir önceki değeri (Forward Fill) veya bir sonraki değeri (Backward Fill) kopyalama.
- **K-NN Imputation:** Eksik örneğe öznitelik uzayında en benzeyen 'k' adet komşuyu bulup onların ortalamasını alma.
- **Model Tabanlı (Regression/Iterative):** Eksik değişkeni "hedef değişken" (target) kabul edip diğer değişkenlerle onu tahmin eden bir model kurma (MICE - Multivariate Imputation by Chained Equations).

### 3. Gürültülü Veri ve Düzeltme

**Gürültü**, ölçülen değişkendeki rastgele hata veya varyanstır.

#### Gürültü Azaltma (Smoothing) Teknikleri
1.  **Binning (Kutulama/Öbekleme):** Sıralı veri değerlerini "kutulara" bölerek yerel yumuşatma sağlar.
    - *Equal-width:* Değer aralığını eşit parçalara bölme (0-10, 10-20...).
    - *Equal-depth:* Her kutuda eşit sayıda veri olacak şekilde bölme.
    - *Smoothing methods:* Kutudaki değerleri kutu ortalaması (mean) veya medyanı ile değiştirme.
2.  **Regresyon:** Veriyi temsil eden en iyi doğruyu/eğriyi bularak, noktaları bu fonksiyona yaklaştırma.
3.  **Aykırı Değer Analizi (Clustering/IQR):** Kümeleme algoritmaları ile grupların dışında kalanları tespit etme veya IQR (Interquartile Range) yöntemi ile alt/üst sınırları aşanları temizleme.

### 4. Veri Dönüştürme (Data Transformation)

Ham veriyi, madencilik algoritmalarının daha verimli çalışacağı bir matematiksel uzaya taşıma işlemidir.

#### 4.1. Ölçeklendirme (Scaling) neden gereklidir?
Mesafe tabanlı algoritmalar (KNN, K-Means, SVM) ve Gradient Descent kullanan yöntemler (Sinir Ağları, Lojistik Regresyon), değişkenlerin sayısal büyüklüklerinden etkilenir. Örneğin, "Yaş" (0-100) ve "Maaş" (0-50000) değişkenleri varsa, model "Maaş" değişkenindeki 1 birimlik değişimi önemsiz, "Yaş"takini önemli görebilir veya tam tersi mesafe hesabında Maaş domine edebilir.

**A. Min-Max Normalization:**
- Veriyi belirli bir aralığa (genellikle [0, 1]) lineer olarak sıkıştırır.
- **Formül:** $X_{yeni} = \frac{X - X_{min}}{X_{max} - X_{min}}$
- *Kullanım:* Veri dağılımı hakkında bilgi yoksa veya görüntü işleme gibi (piksel değerleri) sınırlı aralıklar için. Outlierlara karşı çok hassastır.

**B. Z-Score Standardization:**
- Veriyi ortalaması 0, standart sapması 1 olacak şekilde (Standart Normal Dağılım) dönüştürür.
- **Formül:** $X_{yeni} = \frac{X - \mu}{\sigma}$
- *Kullanım:* Veride aykırı değerler varsa Min-Max'e göre daha dirençlidir. Birçok ML algoritması için varsayılan tercihtir.

#### 4.2. Ayrıklaştırma (Discretization)
Sürekli veriyi kategorik aralıklara bölme. (Yaş -> Çocuk, Genç, Yaşlı).
- Karar ağacı gibi algoritmaların performansını artırabilir ve gürültü etkisini azaltır.

### 5. Veri Entegrasyonu ve İndirgeme
- **Veri Entegrasyonu:** Farklı veritabanlarından gelen verilerin birleştirilmesi.
  - *Schema Matching:* Farklı isimlendirmeleri eşleştirme (Cust_ID = Customer_Number).
  - *Redundancy:* Korelasyon analizi ile tekrar eden bilgilerin (örn: Doğum tarihi varken Yaş bilgisinin de olması) tespiti.
- **Veri İndirgeme:**
  - **Boyut İndirgeme (Dimensionality Reduction):** PCA (Principal Component Analysis) gibi yöntemlerle verinin özünü koruyarak öznitelik sayısını azaltma.
  - **Öznitelik Seçimi (Feature Selection):** Modele en çok katkı sağlayan sütunları seçme, diğerlerini atma.

### 6. Veri Kodlama (Encoding)

Makine öğrenmesi modelleri matematiksel işlemler yapar, metin (string) veriyi işleyemez.

- **Label Encoding:** Kategorileri 0, 1, 2 gibi tamsayılara çevirir.
  - *Risk:* Model, sayılar arasında büyüklük ilişkisi kurabilir (Elma=1, Armut=2 -> Armut > Elma?). Sadece Ordinal (sıralı) verilerde (Eğitim Seviyesi vb.) kullanılmalıdır.
- **One-Hot Encoding:** Her kategori için yeni bir sütun (0/1) oluşturur.
  - *Risk:* Kategori sayısı çok fazlaysa (örn: 1000 farklı mahalle) çok fazla sütun oluşur (Dummy Variable Trap ve Boyut Laneti).

## 💻 Uygulama İçeriği

### Lab 1: Pandas ile Veri Temizleme
- CSV dosyası okuma
- Eksik değerleri tespit etme ve doldurma
- Duplicated değerleri bulma ve silme
- Veri tipleri dönüştürme

### Lab 2: Veri Dönüştürme ve Normalizasyon
- Min-Max normalization
- Z-score standardization
- Log transformation
- One-hot encoding

## 📝 Ödevler

### Ödev 1: Veri Temizleme Projesi
Verilen kirli veri setini temizleyin ve rapor hazırlayın

### Ödev 2: Pandas Alıştırmaları
10 farklı pandas operasyonu yapın

## 📖 Okuma Listesi

### Zorunlu
- Han et al., Bölüm 3: Data Preprocessing
- Pandas Dokümantasyonu

### Önerilen
- "Tidy Data" - Hadley Wickham
- "Missing Data Imputation" - Little & Rubin

## 🔑 Anahtar Kavramlar
- Missing values (MCAR, MAR, MNAR)
- Imputation techniques
- Normalization vs Standardization
- Outlier detection
- One-hot encoding
- Data quality dimensions

## 💡 Pratik İpuçları

1. **Her zaman veriyi inceleyin:**
   ```python
   df.info()
   df.describe()
   df.isnull().sum()
   ```

2. **Eksik veri oranını kontrol edin:**
   - %5'ten az: Silebilirsiniz
   - %5-20: Doldurma düşünün
   - %20+: Dikkatli olun, özniteliği kaldırabilirsiniz

3. **Aykırı değerleri görselleştirin:**
   - Boxplot kullanın
   - IQR yöntemi uygulayın

4. **Normalizasyon seçimi:**
   - Gaussian dağılım: Standardization
   - Bounded değerler: Min-Max normalization
   - Tree-based modeller: Genelde normalizasyon gereksiz

## ❓ Sıkça Sorulan Sorular

**S: Eksik değerleri silmeli mi doldurmalı mıyım?**
C: %5'ten az eksiklik varsa silebilirsiniz. Daha fazlaysa, verinin MCAR/MAR/MNAR olup olmadığına bakın ve uygun imputation yöntemi seçin.

**S: Normalizasyon zorunlu mu?**
C: Model tipine bağlı. KNN, SVM, Neural Networks için önemlidir. Karar ağaçları ve Random Forest için gerekli değildir.

**S: One-hot encoding ne zaman kullanılır?**
C: Nominal (sırasız) kategorik değişkenler için. Ordinal değişkenler için label encoding tercih edilebilir.

## 📊 Örnek Kod Parçaları

```python
import pandas as pd
import numpy as np

# Veri okuma
df = pd.read_csv('data.csv')

# Eksik değer kontrolü
print(df.isnull().sum())

# Eksik değerleri doldurma
df['age'].fillna(df['age'].mean(), inplace=True)

# Normalizasyon
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

# One-hot encoding
df = pd.get_dummies(df, columns=['city'])
```

---

**Sonraki Hafta:** Keşifsel Veri Analizi ve Görselleştirme