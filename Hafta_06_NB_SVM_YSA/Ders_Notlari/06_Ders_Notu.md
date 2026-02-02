# Hafta 6: Naïve Bayes, SVM ve Yapay Sinir Ağları

## 📋 Naïve Bayes

### Bayes Teoremi
```
P(A|B) = P(B|A) × P(A) / P(B)

P(Sınıf|Öznitelikler) = P(Öznitelikler|Sınıf) × P(Sınıf) / P(Öznitelikler)
```

### Naïve Varsayımı
Tüm öznitelikler birbirinden bağımsızdır (naive = saf):
```
P(x₁, x₂, ..., xₙ|C) = P(x₁|C) × P(x₂|C) × ... × P(xₙ|C)
```

### Naïve Bayes Türleri

**Gaussian Naïve Bayes:** Sürekli değerler için
**Multinomial Naïve Bayes:** Metin sınıflandırma
**Bernoulli Naïve Bayes:** Binary öznitelikler

### Avantajlar
✅ Hızlı ve verimli
✅ Az veri ile çalışır
✅ Metin sınıflandırmada etkili
✅ Çok sınıflı problemler için uygun

## 🎯 Support Vector Machines (SVM)

### Temel Fikir
İki sınıfı ayıran **en geniş marjinli** hiper düzlem bul.

### SVM Bileşenleri
- **Destek vektörleri:** Marjine en yakın örnekler
- **Marjin:** Hiper düzlem ile destek vektörleri arası mesafe
- **Hiper düzlem:** Sınıfları ayıran karar sınırı

### Kernel Trick
Doğrusal ayrılamayan verileri yüksek boyuta taşı:

**Linear Kernel:** K(x,y) = x·y
**Polynomial Kernel:** K(x,y) = (x·y + c)^d
**RBF (Gaussian) Kernel:** K(x,y) = exp(-γ||x-y||²)
**Sigmoid Kernel:** K(x,y) = tanh(αx·y + c)

### C Parametresi
- Küçük C: Yumuşak marjin (basit model)
- Büyük C: Sert marjin (karmaşık model)

## 🧠 Yapay Sinir Ağları (YSA)

### Perceptron
En basit YSA modeli:
```
y = f(Σ(wᵢxᵢ) + b)
```

### Çok Katmanlı Ağlar (MLP)
- **Giriş katmanı:** Öznitelikler
- **Gizli katmanlar:** Öğrenme
- **Çıkış katmanı:** Tahmin

### Aktivasyon Fonksiyonları
- **Sigmoid:** σ(x) = 1/(1+e^(-x))
- **ReLU:** f(x) = max(0, x)
- **Tanh:** tanh(x)
- **Softmax:** Çıkış katmanı için

### Backpropagation
Hataları geriye yayarak ağırlıkları güncelleme.

## 💻 Python Kodu

```python
# Naïve Bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_train, y_train)

# SVM
from sklearn.svm import SVC
svm = SVC(kernel='rbf', C=1.0)
svm.fit(X_train, y_train)

# Neural Network
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000)
mlp.fit(X_train, y_train)
```

## 📊 Karşılaştırma

| Algoritma | Hız | Accuracy | Yorumlanabilirlik |
|-----------|-----|----------|-------------------|
| Naïve Bayes | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| SVM | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Neural Net | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
