"""
Örnek Jupyter Notebook Şablonu - Veri Madenciliği Dersi

Bu şablon, haftalık lab çalışmalarınız için kullanabileceğiniz
standart bir yapı sunmaktadır.
"""

# ============================================================================
# KÜTÜPHANE İMPORT
# ============================================================================

# Veri işleme
import numpy as np
import pandas as pd

# Görselleştirme
import matplotlib.pyplot as plt
import seaborn as sns

# Makine öğrenmesi
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Uyarıları kapat
import warnings
warnings.filterwarnings('ignore')

# Görselleştirme ayarları
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("✓ Kütüphaneler yüklendi")

# ============================================================================
# VERİ YÜKLEME
# ============================================================================

# Veri setini yükle
df = pd.read_csv('../Veri_Setleri/veri.csv')

# İlk bakış
print("Veri Seti Boyutu:", df.shape)
print("\nİlk 5 satır:")
print(df.head())

# ============================================================================
# TEMEL BİLGİLER
# ============================================================================

# Veri tipi bilgileri
print("\nVeri Tipleri:")
print(df.info())

# İstatistiksel özetler
print("\nİstatistiksel Özet:")
print(df.describe())

# Eksik değer kontrolü
print("\nEksik Değerler:")
print(df.isnull().sum())

# ============================================================================
# KEŞİFSEL VERİ ANALİZİ (EDA)
# ============================================================================

# Hedef değişkenin dağılımı
plt.figure(figsize=(10, 5))
df['target'].value_counts().plot(kind='bar')
plt.title('Hedef Değişken Dağılımı')
plt.xlabel('Sınıf')
plt.ylabel('Frekans')
plt.show()

# Korelasyon matrisi
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Korelasyon Matrisi')
plt.show()

# Pair plot (küçük veri setleri için)
# sns.pairplot(df, hue='target')
# plt.show()

# ============================================================================
# VERİ ÖN İŞLEME
# ============================================================================

# Eksik değerleri doldurma
df.fillna(df.mean(), inplace=True)

# Kategorik değişkenleri encode etme
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    if column != 'target':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

# Öznitelik ve hedef ayrımı
X = df.drop('target', axis=1)
y = df['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nEğitim seti: {X_train.shape}")
print(f"Test seti: {X_test.shape}")

# ============================================================================
# MODEL EĞİTİMİ
# ============================================================================

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Modelleri tanımla
models = {
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

# Her modeli eğit ve değerlendir
results = {}
for name, model in models.items():
    # Eğitim
    model.fit(X_train_scaled, y_train)
    
    # Tahmin
    y_pred = model.predict(X_test_scaled)
    
    # Skorlar
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    
    results[name] = {
        'train_score': train_score,
        'test_score': test_score,
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'y_pred': y_pred
    }
    
    print(f"\n{name}:")
    print(f"  Eğitim Skoru: {train_score:.4f}")
    print(f"  Test Skoru: {test_score:.4f}")
    print(f"  CV Ortalama: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# ============================================================================
# MODEL DEĞERLENDİRME
# ============================================================================

# En iyi modeli seç
best_model_name = max(results, key=lambda x: results[x]['test_score'])
best_model = models[best_model_name]
y_pred_best = results[best_model_name]['y_pred']

print(f"\n{'='*50}")
print(f"En İyi Model: {best_model_name}")
print(f"{'='*50}")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_best))

# Confusion matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred_best)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(f'Confusion Matrix - {best_model_name}')
plt.ylabel('Gerçek')
plt.xlabel('Tahmin')
plt.show()

# Model karşılaştırma grafiği
comparison_df = pd.DataFrame({
    'Model': list(results.keys()),
    'Test Score': [results[m]['test_score'] for m in results],
    'CV Mean': [results[m]['cv_mean'] for m in results]
})

plt.figure(figsize=(10, 6))
x = np.arange(len(comparison_df))
width = 0.35

plt.bar(x - width/2, comparison_df['Test Score'], width, label='Test Score')
plt.bar(x + width/2, comparison_df['CV Mean'], width, label='CV Mean')

plt.xlabel('Model')
plt.ylabel('Skor')
plt.title('Model Karşılaştırması')
plt.xticks(x, comparison_df['Model'])
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================================
# SONUÇLAR VE YORUMLAR
# ============================================================================

print("\n" + "="*50)
print("SONUÇLAR")
print("="*50)

print(f"""
1. En iyi performans gösteren model: {best_model_name}
2. Test doğruluğu: {results[best_model_name]['test_score']:.4f}
3. Cross-validation ortalaması: {results[best_model_name]['cv_mean']:.4f}

Yorumlar:
- Model performansları karşılaştırıldığında...
- Cross-validation sonuçları...
- Confusion matrix'e göre...
- Gelecek iyileştirmeler:
  * Hiperparametre optimizasyonu (GridSearchCV)
  * Öznitelik mühendisliği
  * Farklı algoritmalar deneme
  * Ensemble yöntemleri
""")

print("\n✓ Analiz tamamlandı!")
