# Hafta 10: Aykırı Değer Tespiti (Anomaly Detection)

## 📋 Anomali Nedir?

**Anomali (Outlier):** Normal davranıştan belirgin şekilde farklı olan gözlem.

### Anomali Tipleri

**1. Point Anomaly (Nokta Anomalisi)**
```
Tek bir veri noktası anormal
Örn: 1000 TL yerine 1,000,000 TL işlem
```

**2. Contextual Anomaly (Bağlamsal Anomali)**
```
Belirli bir bağlamda anormal
Örn: Kışın 35°C sıcaklık
```

**3. Collective Anomaly (Toplu Anomali)**
```
Tek başına normal, birlikte anormal
Örn: Aynı IP'den 1000 login denemesi
```

## 🎯 Kullanım Alanları

- **Fraud Detection:** Kredi kartı dolandırıcılığı
- **Network Security:** Siber saldırı tespiti
- **Healthcare:** Hastalık teşhisi
- **Manufacturing:** Arıza tespiti
- **Finance:** Piyasa manipülasyonu

## 📊 İstatistiksel Yöntemler

### 1. Z-Score (Standard Score)

```
Z = (x - μ) / σ

|Z| > 3 → Anomali
```

**Python:**
```python
from scipy import stats
import numpy as np

data = np.array([10, 12, 12, 13, 12, 11, 14, 100])
z_scores = np.abs(stats.zscore(data))
anomalies = np.where(z_scores > 3)

print("Anomali indexler:", anomalies)
```

**Avantajlar:** ✅ Basit, hızlı
**Dezavantajlar:** ❌ Gaussian varsayımı, tek boyut

### 2. IQR (Interquartile Range)

```
Q1 = 25. percentile
Q3 = 75. percentile
IQR = Q3 - Q1

Anomali: x < Q1 - 1.5×IQR veya x > Q3 + 1.5×IQR
```

**Python:**
```python
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies = (data < lower_bound) | (data > upper_bound)
```

**Avantajlar:** ✅ Outlier'a dayanıklı, non-parametric
**Dezavantajlar:** ❌ Tek boyut

## 🤖 Makine Öğrenmesi Yöntemleri

### 1. Isolation Forest

**İlke:** Anomaliler izole edilmesi daha kolay.

**Nasıl Çalışır:**
1. Rastgele öznitelik seç
2. Rastgele split değeri seç
3. Veriyi böl
4. Tekrarla
5. Anomaliler daha az split'le izole edilir

```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.1, random_state=42)
predictions = iso_forest.fit_predict(X)
# -1: anomaly, 1: normal

anomaly_scores = iso_forest.score_samples(X)  # Anomaly score
```

**Parametreler:**
- `contamination`: Anomali oranı (0.1 = %10)
- `n_estimators`: Ağaç sayısı (default: 100)
- `max_samples`: Her ağaç için sample sayısı

**Avantajlar:**
✅ Hızlı
✅ Çok boyutlu veri
✅ Unsupervised
✅ Outlier'a dayanıklı

### 2. Local Outlier Factor (LOF)

**İlke:** Bir noktanın komşularına göre yoğunluk anomalisini ölç.

**LOF Skoru:**
```
LOF > 1: Anomali (düşük yoğunluk)
LOF ≈ 1: Normal
LOF < 1: İç nokta (yüksek yoğunluk)
```

```python
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
predictions = lof.fit_predict(X)
# -1: anomaly, 1: normal

lof_scores = lof.negative_outlier_factor_  # LOF skorları (negatif)
```

**Parametreler:**
- `n_neighbors`: Komşu sayısı (10-50 arası)
- `contamination`: Anomali oranı

**Avantajlar:**
✅ Yerel yoğunluğa duyarlı
✅ Farklı yoğunluktaki kümelerde etkili

**Dezavantajlar:**
❌ Yavaş (her nokta için mesafe hesaplar)
❌ Yüksek boyutta zayıf

### 3. One-Class SVM

**İlke:** Normal verileri çevreleyen bir sınır bul.

```python
from sklearn.svm import OneClassSVM

ocsvm = OneClassSVM(kernel='rbf', gamma=0.001, nu=0.1)
predictions = ocsvm.fit_predict(X)
# -1: anomaly, 1: normal
```

**Parametreler:**
- `nu`: Anomali oranı üst sınırı
- `kernel`: 'rbf', 'linear', 'poly'
- `gamma`: RBF kernel parametresi

### 4. Autoencoder (Derin Öğrenme)

**İlke:** Normal veriyi öğren, reconstruct et. Yüksek reconstruction error → anomali.

```python
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# Autoencoder
input_dim = X.shape[1]
encoding_dim = 8

input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Eğitim
autoencoder.fit(X_train, X_train, epochs=50, batch_size=32, validation_split=0.1)

# Tahmin
reconstructions = autoencoder.predict(X_test)
mse = np.mean(np.power(X_test - reconstructions, 2), axis=1)
threshold = np.percentile(mse, 95)
anomalies = mse > threshold
```

## 🔍 Zaman Serisi Anomali Tespiti

### 1. Moving Average

```python
window_size = 5
rolling_mean = data.rolling(window=window_size).mean()
rolling_std = data.rolling(window=window_size).std()

upper_bound = rolling_mean + 3 * rolling_std
lower_bound = rolling_mean - 3 * rolling_std

anomalies = (data > upper_bound) | (data < lower_bound)
```

### 2. ARIMA Residuals

```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(data, order=(1, 1, 1))
fitted = model.fit()
residuals = fitted.resid

threshold = 3 * np.std(residuals)
anomalies = np.abs(residuals) > threshold
```

### 3. Prophet (Facebook)

```python
from prophet import Prophet

df = pd.DataFrame({'ds': dates, 'y': values})
model = Prophet(interval_width=0.99)
model.fit(df)

forecast = model.predict(df)

# Anomali: gerçek değer prediction interval dışında
anomalies = (df['y'] < forecast['yhat_lower']) | (df['y'] > forecast['yhat_upper'])
```

## 📈 Değerlendirme Metrikleri

### Etiketli Veri Varsa

```python
from sklearn.metrics import classification_report, confusion_matrix, f1_score

# y_true: 0=normal, 1=anomaly
print(classification_report(y_true, y_pred))

tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print(f"True Negatives: {tn}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")
print(f"True Positives: {tp}")
```

### Etiketsiz Veri

- **Silhouette Score**
- **DBSCAN ile karşılaştırma**
- **Manuel inceleme**

## 💻 Pratik Örnek: Kredi Kartı Fraud Detection

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Veri yükleme
df = pd.read_csv('creditcard.csv')

# Ölçeklendirme
scaler = StandardScaler()
df['Amount_scaled'] = scaler.fit_transform(df[['Amount']])

# Öznitelikler
features = df.drop(['Time', 'Class'], axis=1)
X = features.values
y = df['Class'].values  # 0: normal, 1: fraud

# Model
iso_forest = IsolationForest(contamination=0.001, random_state=42)
y_pred = iso_forest.fit_predict(X)

# -1 → 1 (anomaly), 1 → 0 (normal)
y_pred = np.where(y_pred == -1, 1, 0)

# Değerlendirme
print(classification_report(y, y_pred, target_names=['Normal', 'Fraud']))
```

## 🎯 Hangi Yöntemi Seçmeli?

| Durum | Önerilen Yöntem |
|-------|----------------|
| Tek boyutlu veri | Z-Score, IQR |
| Çok boyutlu, hızlı | Isolation Forest |
| Yerel yoğunluk önemli | LOF |
| Yüksek boyutlu, karmaşık | Autoencoder |
| Zaman serisi | Moving Average, Prophet |
| Etiketli veri var | Supervised learning (Random Forest, XGBoost) |

## 💡 İpuçları

1. **Contamination parametresi:** Domain knowledge ile belirle
2. **Preprocessing:** Scaling/normalization önemli
3. **Multiple methods:** Birden fazla yöntem dene, karşılaştır
4. **Threshold tuning:** Business requirements'a göre ayarla
5. **False positives:** Çok anomali bulma, gerçek anormalileri kaçırabilir
6. **Visualization:** Anomalileri görselleştir, manuel kontrol et
7. **Feature engineering:** İyi öznitelikler anomali tespitini iyileştirir

## 📚 Kütüphaneler

- **PyOD:** Python Outlier Detection (20+ algoritma)
- **scikit-learn:** IsolationForest, LOF, OneClassSVM
- **TensorFlow/Keras:** Autoencoder
- **Prophet:** Zaman serisi anomali
