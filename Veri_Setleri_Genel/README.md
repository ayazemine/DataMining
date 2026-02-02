# Veri Madenciliği Dersi - Genel Veri Setleri

Bu klasör, ders boyunca kullanılacak çeşitli veri setlerini içermektedir.

## 📊 Veri Setleri Listesi

### 1. Klasik ML Veri Setleri

#### Iris Dataset
- **Dosya:** `iris.csv`
- **Kayıt:** 150
- **Öznitelik:** 4 (sepal length, sepal width, petal length, petal width)
- **Sınıf:** 3 (Setosa, Versicolor, Virginica)
- **Kullanım:** Sınıflandırma, kümeleme

#### Titanic Dataset
- **Dosya:** `titanic.csv`
- **Kayıt:** 30
- **Öznitelik:** 11 (age, sex, class, fare, vb.)
- **Hedef:** Survived (0/1)
- **Kullanım:** Binary sınıflandırma, EDA

#### Wine Quality Dataset
- **Dosya:** `wine_quality.csv`
- **Kayıt:** 30
- **Öznitelik:** 11 (kimyasal özellikler)
- **Hedef:** Quality (3-8)
- **Kullanım:** Multi-class sınıflandırma

### 2. E-Ticaret Veri Setleri

#### Online Retail Dataset
- **Dosya:** `online_retail.csv`
- **Kayıt:** 541,909
- **İçerik:** İşlemler, ürünler, müşteriler
- **Kullanım:** Market sepet analizi, müşteri segmentasyonu

#### Customer Churn Dataset
- **Dosya:** `customer_churn.csv`
- **Kayıt:** 20
- **Öznitelik:** 20
- **Hedef:** Churn (Yes/No)
- **Kullanım:** Müşteri kaybı tahmini

### 3. Metin Veri Setleri

#### IMDB Movie Reviews
- **Dosya:** `imdb_reviews.csv`
- **Kayıt:** 30
- **İçerik:** Film yorumları ve sentiment
- **Kullanım:** Duygu analizi, metin sınıflandırma

#### Twitter Sentiment
- **Dosya:** `twitter_sentiment.csv`
- **Kayıt:** 30
- **İçerik:** Tweets ve duygular
- **Kullanım:** Sosyal medya analizi

### 4. Sağlık Veri Setleri

#### Heart Disease Dataset
- **Dosya:** `heart_disease.csv`
- **Kayıt:** 303
- **Öznitelik:** 13 (yaş, kolesterol, vb.)
- **Hedef:** Disease (0-4)
- **Kullanım:** Hastalık tahmini

#### Diabetes Dataset
- **Dosya:** `diabetes.csv`
- **Kayıt:** 768
- **Öznitelik:** 8
- **Hedef:** Outcome (0/1)
- **Kullanım:** Binary sınıflandırma

### 5. Finansal Veri Setleri

#### Credit Card Fraud
- **Dosya:** `credit_card_fraud.csv`
- **Kayıt:** 284,807
- **Öznitelik:** 30 (PCA transformed)
- **Hedef:** Class (0/1) - highly imbalanced
- **Kullanım:** Anomali tespiti, dengesiz sınıf

#### Loan Prediction
- **Dosya:** `loan_prediction.csv`
- **Kayıt:** 614
- **Öznitelik:** 12
- **Hedef:** Loan_Status (Y/N)
- **Kullanım:** Kredi onay tahmini

### 6. Zaman Serisi Veri Setleri

#### Stock Prices
- **Dosya:** `stock_prices.csv`
- **Kayıt:** Time series
- **İçerik:** Tarih, Open, High, Low, Close, Volume
- **Kullanım:** Zaman serisi analizi, tahmin

#### Air Quality
- **Dosya:** `air_quality.csv`
- **Kayıt:** 30
- **İçerik:** Saatlik hava kalitesi ölçümleri
- **Kullanım:** Zaman serisi, regresyon

### 7. Resim Veri Setleri (Bağlantılar)

#### MNIST
- **Boyut:** 70,000 el yazısı rakam
- **Kullanım:** Görüntü sınıflandırma
- **İndirme:** sklearn.datasets.load_digits()

#### Fashion MNIST
- **Boyut:** 70,000 kıyafet görseli
- **Kullanım:** Görüntü sınıflandırma

### 8. Kümeleme Veri Setleri

#### Mall Customers
- **Dosya:** `mall_customers.csv`
- **Kayıt:** 50
- **Öznitelik:** 5 (CustomerID, Gender, Age, Income, Spending Score)
- **Kullanım:** Müşteri segmentasyonu

#### Wholesale Customers
- **Dosya:** `wholesale_customers.csv`
- **Kayıt:** 30
- **Öznitelik:** 8
- **Kullanım:** K-means, hiyerarşik kümeleme

## 📥 Veri Setlerini İndirme

### Python ile İndirme
```python
import pandas as pd
from sklearn.datasets import load_iris, load_wine

# Iris
iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target

# Kaggle CLI ile
# !kaggle datasets download -d <dataset-name>
```

### Kaynak Siteler
1. **UCI ML Repository:** https://archive.ics.uci.edu/ml/
2. **Kaggle Datasets:** https://www.kaggle.com/datasets
3. **OpenML:** https://www.openml.org/
4. **Google Dataset Search:** https://datasetsearch.research.google.com/
5. **Data.gov:** https://data.gov/
6. **Awesome Public Datasets:** https://github.com/awesomedata/awesome-public-datasets

## 📋 Veri Seti Kullanım Rehberi

### 1. Veri Setini Yükleme
```python
import pandas as pd

df = pd.read_csv('veri_seti.csv')
print(df.head())
print(df.info())
print(df.describe())
```

### 2. Eksik Değer Kontrolü
```python
print(df.isnull().sum())
```

### 3. Temel İstatistikler
```python
print(df.describe())
print(df['column'].value_counts())
```

### 4. Görselleştirme
```python
import matplotlib.pyplot as plt
import seaborn as sns

df.hist(figsize=(12, 10))
plt.show()

sns.pairplot(df)
plt.show()
```

## ⚖️ Lisans ve Kullanım

- Veri setleri eğitim amaçlı kullanım içindir

## 🔄 Güncelleme

Bu klasör düzenli olarak yeni veri setleriyle güncellenecektir.

**Son Güncelleme:** Şubat 2026
