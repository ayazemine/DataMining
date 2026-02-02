# Python ile Veri Madenciliği - Hızlı Başvuru Rehberi

## 📦 Temel Kütüphaneler

### Import'lar
```python
# Veri işleme
import numpy as np
import pandas as pd

# Görselleştirme
import matplotlib.pyplot as plt
import seaborn as sns

# Makine öğrenmesi
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
```

---

## 📊 Pandas Hızlı Referans

### Veri Okuma/Yazma
```python
# CSV okuma
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', sep=';', encoding='utf-8')

# Excel okuma
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# Yazma
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

### Temel İşlemler
```python
# İlk bakış
df.head()          # İlk 5 satır
df.tail()          # Son 5 satır
df.shape           # (satır, sütun)
df.columns         # Sütun isimleri
df.info()          # Veri tipleri ve eksik değerler
df.describe()      # İstatistiksel özet

# Sütun seçme
df['column']              # Tek sütun (Series)
df[['col1', 'col2']]      # Birden fazla sütun (DataFrame)

# Satır filtreleme
df[df['age'] > 30]
df[(df['age'] > 30) & (df['city'] == 'İstanbul')]
df[df['name'].str.contains('Ali')]

# Sıralama
df.sort_values('age')                    # Artan
df.sort_values('age', ascending=False)   # Azalan
df.sort_values(['city', 'age'])          # Çoklu
```

### Eksik Değerler
```python
# Kontrol
df.isnull().sum()
df.isna().sum()

# Silme
df.dropna()                  # Tüm NA'ları sil
df.dropna(subset=['age'])    # Belirli sütundaki NA'ları sil

# Doldurma
df.fillna(0)                        # 0 ile doldur
df.fillna(df.mean())                # Ortalama ile
df['age'].fillna(df['age'].median(), inplace=True)
df.fillna(method='ffill')           # İleri doldur
df.fillna(method='bfill')           # Geri doldur
```

### Gruplama ve Aggregation
```python
# Gruplama
df.groupby('city')['salary'].mean()
df.groupby(['city', 'gender']).agg({
    'salary': ['mean', 'median', 'std'],
    'age': 'mean'
})

# Value counts
df['city'].value_counts()
df['city'].value_counts(normalize=True)  # Yüzde
```

### Veri Dönüştürme
```python
# Yeni sütun ekleme
df['new_col'] = df['col1'] + df['col2']
df['age_group'] = df['age'].apply(lambda x: 'young' if x < 30 else 'old')

# Kategorik değişken dönüştürme
df['gender'] = df['gender'].map({'M': 0, 'F': 1})

# One-hot encoding
pd.get_dummies(df, columns=['city'])

# Veri tipi değiştirme
df['age'] = df['age'].astype(int)
df['date'] = pd.to_datetime(df['date'])
```

---

## 🔢 NumPy Hızlı Referans

```python
# Dizi oluşturma
arr = np.array([1, 2, 3, 4, 5])
arr = np.zeros((3, 4))      # 3x4 sıfır matrisi
arr = np.ones((2, 3))       # 2x3 bir matrisi
arr = np.random.rand(3, 3)  # 3x3 rastgele [0,1)

# İstatistiksel işlemler
np.mean(arr)
np.median(arr)
np.std(arr)
np.min(arr)
np.max(arr)
np.sum(arr)

# Matematiksel işlemler
np.sqrt(arr)
np.log(arr)
np.exp(arr)
arr ** 2

# Reshaping
arr.reshape(3, 4)
arr.flatten()
```

---

## 📈 Matplotlib ve Seaborn

### Matplotlib Temel
```python
# Line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Line')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
plt.scatter(x, y, c='red', alpha=0.5)

# Histogram
plt.hist(data, bins=20, edgecolor='black')

# Bar plot
plt.bar(categories, values)

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
```

### Seaborn
```python
# Distribution plot
sns.histplot(df['age'], kde=True)
sns.boxplot(x='city', y='salary', data=df)
sns.violinplot(x='city', y='salary', data=df)

# Relationship
sns.scatterplot(x='age', y='salary', hue='gender', data=df)
sns.lineplot(x='date', y='value', data=df)

# Categorical
sns.countplot(x='city', data=df)
sns.barplot(x='city', y='salary', data=df)

# Matrix
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Pair plot
sns.pairplot(df, hue='target')
```

---

## 🤖 Scikit-learn Hızlı Referans

### Veri Hazırlama

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Label encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)
```

### Model Eğitimi

```python
# Model oluştur
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=5, random_state=42)

# Eğit
model.fit(X_train, y_train)

# Tahmin
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)  # Olasılıklar

# Skor
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
```

### Model Değerlendirme

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

# Metrikler
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Classification report
print(classification_report(y_test, y_pred))

# ROC-AUC (binary classification)
roc_auc = roc_auc_score(y_test, y_proba[:, 1])
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score, cross_validate

# Basit CV
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Çoklu metrik
cv_results = cross_validate(
    model, X, y, cv=5,
    scoring=['accuracy', 'precision_weighted', 'recall_weighted']
)
```

### Hiperparametre Optimizasyonu

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(
    DecisionTreeClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
print("Best parameters:", grid_search.best_params_)
print("Best score:", grid_search.best_score_)

# Randomized Search (daha hızlı)
random_search = RandomizedSearchCV(
    model, param_distributions=param_grid,
    n_iter=10, cv=5, random_state=42
)
```

### Popüler Algoritmalar

```python
# Decision Tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=5)

# Random Forest
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, max_depth=10)

# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)

# Support Vector Machine
from sklearn.svm import SVC
clf = SVC(kernel='rbf', C=1.0)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

# Logistic Regression
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(max_iter=1000)
```

---

## 🎯 Kümeleme

```python
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Silhouette score
score = silhouette_score(X, labels)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)
```

---

## 💡 Faydalı Kod Parçacıkları

### Model Pipeline
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

### Feature Importance
```python
# Tree-based modeller için
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
    'feature': X.columns,
    'importance': importances
}).sort_values('importance', ascending=False)

print(feature_importance_df)
```

### Confusion Matrix Görselleştirme
```python
import seaborn as sns
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
```

### ROC Curve
```python
from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_test, y_proba[:, 1])
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

## 🔍 Debugging ve Profiling

```python
# Veri boyutunu kontrol et
print(X_train.shape, X_test.shape)

# Veri tiplerini kontrol et
print(df.dtypes)

# Eksik değerleri kontrol et
print(df.isnull().sum())

# Unique değerleri kontrol et
print(df['column'].nunique())

# Memory kullanımı
print(df.memory_usage(deep=True))

# Execution time
import time
start = time.time()
# kod...
print(f"Time: {time.time() - start:.2f}s")
```

---

Bu rehber, ders boyunca sıkça kullanacağınız kodları hızlı bir şekilde bulmanız için hazırlanmıştır. 

**İpucu:** Bu dosyayı yazdırıp yanınızda bulundurun! 📄
