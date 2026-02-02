# Hafta 3: Keşifsel Veri Analizi (EDA) ve Görselleştirme

## 📋 Hafta Hedefleri
- Betimsel istatistik kavramlarını anlama
- Veri görselleştirme tekniklerini öğrenme
- Matplotlib ve Seaborn kullanımı
- Veri dağılımlarını yorumlama
- Korelasyon analizi yapabilme

## 📚 Teorik İçerik

### 1. Keşifsel Veri Analizi (EDA) Nedir?

EDA, veriyi anlamanın ilk adımıdır:
- Verinin yapısını ve özelliklerini keşfetme
- Kalıpları ve ilişkileri görsel olarak inceleme
- Hipotezler oluşturma
- Modelleme öncesi içgörü (insight) kazanma

![EDA Süreci (CRISP-DM)](https://media.geeksforgeeks.org/wp-content/uploads/20250806130212782461/file.webp)
*Şekil 1: Keşifsel Veri Analizi*

#### EDA'nın Temel Amaçları
1.  **Veri Kalitesi Kontrolü:** Eksik, hatalı veya tutarsız verileri belirlemek.
2.  **Dağılım Analizi:** Değişkenlerin nasıl dağıldığını (Normal, Çarpık vb.) anlamak.
3.  **Aykırı Değer (Outlier) Tespiti:** Analizi bozabilecek uç değerleri yakalamak.
4.  **İlişki Keşfi:** Değişkenler arasındaki korelasyonu ve nedensellik ipuçlarını bulmak.

### 2. Betimsel İstatistik (Descriptive Statistics)

Veriyi özetlemek için kullanılan temel istatistiksel metriklerdir.

#### 2.1. Merkezi Eğilim Ölçüleri

*   **Ortalama (Mean - $\mu$):** Verilerin ağırlık merkezi.
    $$ \mu = \frac{\sum x}{n} $$
    *   *Not:* Aykırı değerlere karşı çok hassastır.

*   **Medyan (Median):** Veri küçükten büyüğe sıralandığında tam ortadaki değer.
    *   *Avantaj:* Aykırı değerlere karşı dirençlidir (Robust). Gelir dağılımı gibi çarpık verilerde ortalamadan daha iyi temsil eder.

*   **Mod (Mode):** En sık tekrar eden değer.
    *   *Kullanım:* Kategorik veriler (örn: En çok satılan ürün rengi) için tek merkezi eğilim ölçüsüdür.

#### 2.2. Yayılım (Dağılım) Ölçüleri

*   **Varyans ($\sigma^2$) ve Standart Sapma ($\sigma$):** Verilerin ortalamadan ne kadar uzaklaştığının ölçüsüdür.
    $$ \sigma = \sqrt{\frac{\sum(x - \mu)^2}{n}} $$
    *   Düşük standart sapma: Veriler ortalamaya yakın toplanmış.
    *   Yüksek standart sapma: Veriler geniş bir alana yayılmış.

*   **Çeyrekler Arası Aralık (IQR - Interquartile Range):**
    $$ IQR = Q3 (75\%) - Q1 (25\%) $$
    *   Verinin ortadaki %50'lik kısmının yayıldığı aralığı gösterir.

#### 2.3. Dağılım Şekli

![Skewness Dağılımlar](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Relationship_between_mean_and_median_under_different_skewness.png/640px-Relationship_between_mean_and_median_under_different_skewness.png)
*Şekil 2: Sola Çarpık (Negatif), Simetrik ve Sağa Çarpık (Pozitif) Dağılımlar*

*   **Çarpıklık (Skewness):** Dağılımın simetrisini ölçer.
    *   *Simetrik:* Mean = Median
    *   *Sağa Çarpık (Positive):* Kuyruk sağda, Mean > Median (Örn: Maaşlar)
    *   *Sola Çarpık (Negative):* Kuyruk solda, Mean < Median (Örn: Sınav notları - eğer sınav kolaysa)

*   **Basıklık (Kurtosis):** Dağılımın kuyruklarının ağırlığını ölçer.
    *   *Leptokurtic (Sivri):* Aşırı uç değerler barındırır.
    *   *Platykurtic (Basık):* Uç değer ihtimali azdır.

### 3. Veri Görselleştirme Teknikleri

Görselleştirme, sayıların anlatamadığı hikayeyi gösterir.

#### 3.1. Tek Değişkenli (Univariate) Analiz

**Histogram**
*   Sürekli değişkenlerin frekans dağılımını gösterir.
*   *Kullanım:* Veri normal dağılıyor mu? Çarpıklık var mı?
![Histogram Örneği](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Histogram_of_arrivals_per_minute.svg/320px-Histogram_of_arrivals_per_minute.svg.png)

**Box Plot (Kutu Grafiği)**
*   Verinin 5 sayılık özetini (Min, Q1, Median, Q3, Max) ve aykırı değerleri gösterir.
*   *Kullanım:* Gruplar arası karşılaştırma yapmak (örn: Cinsiyete göre maaş dağılımı).
![Boxplot Yapısı](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Boxplot_vs_PDF.svg/640px-Boxplot_vs_PDF.svg.png)

**Bar Chart (Sütun Grafiği)**
*   Kategorik verilerin frekansını gösterir.

**Pie Chart**
*   *Uyarı:* 5'ten fazla kategori varsa veya farklar küçükse kullanmaktan kaçının. İnsan gözü açıları kıyaslamakta zorlanır.

#### 3.2. İki Değişkenli (Bivariate) Analiz

**Scatter Plot (Saçılım Grafiği)**
*   İki sayısal değişken arasındaki ilişkiyi noktalarla gösterir.
*   *Kullanım:* Korelasyon var mı? İlişki doğrusal mı?
![Scatter Plot Örneği](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Scatter_plot.jpg/640px-Scatter_plot.jpg)

**Heatmap (Isı Haritası)**
*   Değerlerin büyüklüğünü renklerle ifade eder. Genellikle Korelasyon Matrisini görselleştirmek için kullanılır.
![Heatmap Örneği](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Correlogram_mtcars.png/600px-Correlogram_mtcars.png)

**Line Plot**
*   Zaman serilerinde değişimi (trend) görmek için kullanılır.

### 4. Korelasyon Analizi

İki değişken arasındaki ilişkinin yönünü ve şiddetini ölçer.

*   **Pearson Korelasyon Katsayısı ($r$):** Doğrusal ilişkiyi ölçer.
    *   Prosedür: Veriler normal dağılmalı ve ilişki lineer olmalı.
    *   Değer: -1 (Tam negatif) ile +1 (Tam pozitif) arasında.

*   **Spearman Korelasyon Katsayısı ($\rho$):** Sıralama (Rank) tabanlıdır.
    *   Prosedür: Doğrusal olmayan ama monoton (biri artarken diğeri de artan/azalan) ilişkilerde veya outlier olduğunda kullanılır.

![Korelasyon Tipleri](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Correlation_examples2.svg/600px-Correlation_examples2.svg.png)
*Şekil 3: Pozitif, Negatif ve İlişkisiz Durumlar*

> ⚠️ **Önemli:** Korelasyon, nedensellik (causation) anlamına gelmez! Dondurma satışları ile boğulma vakaları yüksek korelasyonludur ama sebebi "Sıcaklık"tır.

### 5. Veri Dağılımları ve Aykırı Değerler

#### Aykırı Değer (Outlier) Tespiti

Verinin genel karakterine uymayan gözlemlerdir.

**1. IQR (Interquartile Range) Yöntemi (Tukey's Fences)**
Boxplot mantığına dayanır. Dağılımdan bağımsızdır (Non-parametric).
*   **Alt Sınır:** $Q1 - 1.5 \times IQR$
*   **Üst Sınır:** $Q3 + 1.5 \times IQR$

**2. Z-Score Yöntemi**
Veri normal dağılıyorsa kullanılır.
*   Eğer bir veri noktasının Z-skoru (Ortalamadan kaç standart sapma uzakta olduğu) $|Z| > 3$ ise aykırı kabul edilir.

```python
# Z-Score ile outlier tespiti
from scipy import stats
import numpy as np
z_scores = np.abs(stats.zscore(df['maas']))
outliers = df[z_scores > 3]
```

### 6. Görselleştirme İçin İpuçları (Best Practices)

1.  **Gereksiz Süslemelerden Kaçının (Chartjunk):** 3D efektleri, gölgeler ve karışık arka planlar veriyi okumayı zorlaştırır.
2.  **Renkleri Bilinçli Kullanın:** Kategorik ayrım için zıt renkler, şiddet/büyüklük için aynı rengin tonlarını (gradient) kullanın.
3.  **Başlık ve Etiketler:** Grafiğin ne anlattığını (Başlık) ve eksenlerin ne olduğunu (X/Y Label) mutlaka belirtin.
4.  **Ölçeklendirme:** Y eksenini 0'dan başlatmak genellikle en dürüst yaklaşımdır. Aralığı daraltmak manipülasyona açık olabilir.
2. **Netlik:** Eksen etiketleri, başlık, legend
3. **Renk kullanımı:** Anlamlı ve erişilebilir
4. **Ölçek:** Uygun eksen aralıkları
5. **Bağlam:** Ne gösterdiğinizi açıklayın

#### Kaçınılması Gerekenler
- ❌ 3D grafikler (gerekmedikçe)
- ❌ Çok fazla renk
- ❌ Yanıltıcı eksen ölçekleri
- ❌ Pie chart (5+ kategori için)

## 💻 Uygulama İçeriği

### Lab 1: Matplotlib Temelleri
- Figure ve axes oluşturma
- Farklı plot tipleri
- Özelleştirme (colors, styles, markers)

### Lab 2: Seaborn ile İleri Görselleştirme
- Distribution plots
- Categorical plots
- Relationship plots
- Matrix plots

### Lab 3: Gerçek Veri ile EDA
- Kaggle veri seti analizi
- Tam EDA raporu oluşturma

## 📝 Ödevler

### Ödev 1: EDA Raporu
Verilen veri setinin kapsamlı EDA raporu

### Ödev 2: Görselleştirme Alıştırmaları
10 farklı görselleştirme tipi oluşturma

## 📖 Okuma Listesi

### Zorunlu
- Tan et al., Bölüm 2: Data
- "The Visual Display of Quantitative Information" - Edward Tufte (seçme bölümler)

### Önerilen
- "Storytelling with Data" - Cole Nussbaumer Knaflic
- Matplotlib ve Seaborn dokümantasyonu

## 🎨 Renk Paletleri

```python
# Seaborn renk paletleri
sns.color_palette("deep")      # Varsayılan
sns.color_palette("husl", 8)   # 8 farklı renk
sns.color_palette("Set2")      # Yumuşak renkler
sns.color_palette("viridis")   # Perceptually uniform
```

## 🔑 Anahtar Kavramlar
- Exploratory Data Analysis (EDA)
- Descriptive statistics
- Central tendency: mean, median, mode
- Dispersion: variance, std, IQR
- Correlation vs causation
- Skewness and kurtosis
- Outlier detection
- Data visualization principles

## 💡 Pratik İpuçları

1. **Her zaman EDA ile başlayın:**
   ```python
   df.head()
   df.info()
   df.describe()
   df.corr()
   ```

2. **Görselleştirmeleri kaydedin:**
   ```python
   plt.savefig('plot.png', dpi=300, bbox_inches='tight')
   ```

3. **Korelasyonu görselleştirin:**
   ```python
   sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
   ```

4. **Subplots kullanın:**
   ```python
   fig, axes = plt.subplots(2, 2, figsize=(12, 10))
   ```

## ❓ Sıkça Sorulan Sorular

**S: Histogram'da kaç bin kullanmalıyım?**
C: Sturges' rule: bins = 1 + log₂(n). Veya 10-30 arası deneyin.

**S: Korelasyon yüksekse ne yapmalıyım?**
C: Yüksek korelasyonlu özniteliklerden birini kaldırabilirsiniz (multicollinearity).

**S: Aykırı değerleri her zaman silmeli miyim?**
C: Hayır! Önce nedenini araştırın. Veri girişi hatası olabilir veya gerçek bir aykırılık olabilir.

---

**Sonraki Hafta:** Karar Ağaçları Algoritmaları
