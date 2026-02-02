# Hafta 7: Ensemble Learning ve Model Değerlendirme

## 📋 Ensemble Learning Nedir?

Birden fazla modeli birleştirerek daha iyi tahmin yapma.

**Motivasyon:** "Birlik güçtür" - Çok sayıda zayıf model, bir güçlü model oluşturabilir.

## 🎯 Ensemble Türleri

### 1. Bagging (Bootstrap Aggregating)

**İlke:** Paralel modeller, varyansı azalt

**Bootstrap:** Yerine koyarak örnekleme
- Orijinal veri: N örnek
- Bootstrap sample: N örnek (tekrarlı)
- Her model farklı bootstrap sample'da eğitilir

**Voting:**
- Classification: Çoğunluk oylaması
- Regression: Ortalama

### 2. Boosting

**İlke:** Sıralı modeller, bias'ı azalt

Her yeni model, önceki modellerin hatalarına odaklanır.

**Adımlar:**
1. İlk model eğit
2. Hatalı örneklere ağırlık ver
3. Yeni model eğit
4. Tekrarla

### 3. Stacking

Farklı modellerin çıktılarını bir meta-model ile birleştir.

## 🌲 Random Forest

**Karar ağaçlarının bagging'i + öznitelik rastgeleliği**

### Algoritma
```
For b = 1 to B:
    1. Bootstrap sample oluştur
    2. Her split'te rastgele m öznitelik seç
    3. Karar ağacı oluştur (tam büyüt, budama yok)
    
Tahmin = Tüm ağaçların ortalaması/çoğunluk oylaması
```

### Parametreler
- **n_estimators:** Ağaç sayısı (100-500 iyi)
- **max_depth:** Maksimum derinlik
- **min_samples_split:** Bölme için minimum örnek
- **max_features:** Her split'te kullanılacak öznitelik sayısı
  - "sqrt": √n (classification default)
  - "log2": log₂(n)
  - None: Tüm öznitelikler

### Avantajlar
✅ Yüksek accuracy
✅ Overfitting'e dayanıklı
✅ Feature importance
✅ Out-of-bag (OOB) error
✅ Paralel eğitilebilir

❌ Yorumlaması zor
❌ Büyük model boyutu
❌ Yavaş tahmin

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)

# Feature importance
importances = rf.feature_importances_
```

## 🚀 Gradient Boosting

### AdaBoost (Adaptive Boosting)

```
1. Tüm örneklere eşit ağırlık ver: w_i = 1/N
2. For m = 1 to M:
    a. Ağırlıklı veriyle model eğit
    b. Hata hesapla
    c. Model ağırlığı hesapla: α_m
    d. Yanlış örneklere daha fazla ağırlık ver
3. Final = Σ(α_m × model_m)
```

### Gradient Boosting Machine (GBM)

Gradient descent ile hataları azaltma.

```
F_0(x) = başlangıç tahmini
For m = 1 to M:
    1. Residual hesapla: r = y - F_(m-1)(x)
    2. Yeni model eğit: h_m(x) ≈ r
    3. Güncelle: F_m(x) = F_(m-1)(x) + η × h_m(x)
```

### XGBoost (Extreme Gradient Boosting)

**Gelişmiş GBM implementasyonu**
- Regularization (L1, L2)
- Paralel işlem
- Tree pruning
- Missing value handling

```python
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
model.fit(X_train, y_train)
```

## 📊 Model Karşılaştırma

| Algoritma | Hız | Accuracy | Overfitting | Yorumlama |
|-----------|-----|----------|-------------|-----------|
| Tek Ağaç | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Random Forest | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| AdaBoost | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| XGBoost | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |

## 🎯 Model Değerlendirme - Derinlemesine

### Cross-Validation Stratejileri

**K-Fold CV:**
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
```

**Stratified K-Fold:** Sınıf dağılımını korur
```python
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5)
for train_idx, test_idx in skf.split(X, y):
    # ...
```

**Time Series Split:** Zaman serisi için
```python
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)
```

### ROC Curve ve AUC

```python
from sklearn.metrics import roc_curve, auc

y_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
```

### Precision-Recall Curve

Dengesiz veri setleri için ROC'tan daha bilgilendirici.

```python
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_test, y_proba)
plt.plot(recall, precision)
```

### Learning Curve

Model ne kadar veri ile ne kadar öğreniyor?

```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(
    model, X, y, cv=5, 
    train_sizes=np.linspace(0.1, 1.0, 10)
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Train')
plt.plot(train_sizes, test_scores.mean(axis=1), label='Test')
plt.xlabel('Training Examples')
plt.ylabel('Score')
plt.legend()
```

## 🔧 Hiperparametre Optimizasyonu

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)
print("Best score:", grid.best_score_)
```

### Randomized Search
Daha hızlı, rastgele kombinasyonlar dener.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    model, param_distributions=param_grid,
    n_iter=20, cv=5, random_state=42
)
```

## 💡 İpuçları

1. **Başla basit:** Önce tek model, sonra ensemble
2. **Cross-validation:** Her zaman CV kullan
3. **Baseline:** Basit bir baseline model oluştur
4. **Feature engineering:** Model kadar önemli
5. **Compute trade-off:** Accuracy vs hız dengesi
6. **Hyperparameter tuning:** Sonunda yap, önce değil
