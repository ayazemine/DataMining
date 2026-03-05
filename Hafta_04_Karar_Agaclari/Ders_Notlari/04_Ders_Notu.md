# Hafta 4: Karar Ağaçları (Decision Trees)

## 📋 Hafta Hedefleri
- Sınıflandırma kavramını anlama
- Karar ağaçları algoritmasını öğrenme
- ID3, C4.5 ve CART algoritmalarını karşılaştırma
- Bilgi kazancı ve Gini indeksi hesaplama
- Scikit-learn ile karar ağacı modeli oluşturma

## 📚 Teorik İçerik

### 1. Sınıflandırmaya Giriş

#### Sınıflandırma Nedir?
- Denetimli öğrenme (Supervised Learning) görevidir
- Etiketli veriyle model eğitme
- Yeni verileri kategorilere atama

#### Sınıflandırma vs Regresyon
- **Sınıflandırma:** Kategorik hedef değişken (spam/ham, hasta/sağlıklı)
- **Regresyon:** Sürekli hedef değişken (fiyat, sıcaklık)

#### Sınıflandırma Süreci
1. **Eğitim (Training):** Model oluşturma
2. **Test (Testing):** Model değerlendirme
3. **Tahmin (Prediction):** Yeni verileri sınıflandırma

### 2. Karar Ağaçları Nedir?

#### Temel Yapı
```
            [Hava Durumu?]
           /      |      \
      Güneşli   Yağmur   Bulutlu
        /         |         \
   [Nem > 70?]  [Hayır]  [Evet]
    /    \
  Hayır  Evet
   |      |
[Evet] [Hayır]
```

#### Bileşenler
- **Kök Düğüm (Root Node):** En üstteki düğüm
- **İç Düğümler (Internal Nodes):** Karar noktaları
- **Yaprak Düğümler (Leaf Nodes):** Sınıf etiketleri
- **Dal (Branch):** Karar yolu

#### Avantajlar ✅
- Anlaşılması kolay (white box model)
- Görselleştirilebilir
- Hem sayısal hem kategorik veri ile çalışır
- Veri ön işleme minimal
- Doğrusal olmayan ilişkileri yakalayabilir

#### Dezavantajlar ❌
- Aşırı öğrenme (overfitting) eğilimi
- Küçük veri değişikliklerine duyarlı
- Dengesiz sınıflarda performans düşer
- XOR gibi problemlerde zayıf

### 3. Karar Ağacı Oluşturma (Induction)

#### Genel Algoritma
```
BuildTree(Data, Attributes):
    if all same class:
        return leaf with that class
    if no more attributes:
        return leaf with majority class
    
    best_attr = SelectBestAttribute(Data, Attributes)
    tree = new node with best_attr
    
    for each value v of best_attr:
        subset = data where best_attr = v
        subtree = BuildTree(subset, Attributes - {best_attr})
        add subtree to tree
    
    return tree
```

#### Öznitelik Seçimi
En iyi özniteliği seçmek için metrikler:
- **Bilgi Kazancı (Information Gain):** ID3
- **Kazanç Oranı (Gain Ratio):** C4.5
- **Gini İndeksi (Gini Index):** CART

### 4. ID3 Algoritması

#### Entropi (Entropy)
Veri setindeki belirsizlik ölçüsü:
```
Entropy(S) = -Σ p_i × log₂(p_i)
```

**Örnek:**
- 9 pozitif, 5 negatif örnek
- Entropy = -(9/14)×log₂(9/14) - (5/14)×log₂(5/14) = 0.940

#### Bilgi Kazancı (Information Gain)
```
Gain(S, A) = Entropy(S) - Σ (|S_v|/|S|) × Entropy(S_v)
```

**Adımlar:**
1. Tüm öznitelikler için bilgi kazancını hesapla
2. En yüksek kazançlı özniteliği seç
3. O özniteliğe göre böl
4. Alt kümeler için tekrarla

**Örnek Hesaplama:**

Dataset:
(img width="298" height="279" alt="image" src="https://github.com/user-attachments/assets/64d5a6fe-c033-436f-8128-d01126f1492f" /)

```
Day  Outlook  Temp   Humidity  Wind   PlayTennis
D1   Sunny    Hot    High      Weak   No
D2   Sunny    Hot    High      Strong No
D3   Overcast Hot    High      Weak   Yes
D4   Rain     Mild   High      Weak   Yes
D5   Rain     Cool   Normal    Weak   Yes
...
```

1. Entropy(S) = -9/14 × log₂(9/14) - 5/14 × log₂(5/14) = 0.940

2. Outlook özniteliği için:
   - Sunny: 2 Yes, 3 No → Entropy = 0.971
   - Overcast: 4 Yes, 0 No → Entropy = 0
   - Rain: 3 Yes, 2 No → Entropy = 0.971
   
   Gain(S, Outlook) = 0.940 - (5/14×0.971 + 4/14×0 + 5/14×0.971) = 0.246

#### ID3'ün Zayıf Yönleri
- Çok değerli öznitelikleri tercih eder
- Sayısal özniteliklerle doğrudan çalışmaz
- Eksik değerleri yönetemez
- Budama (pruning) yapmaz → aşırı öğrenme

### 5. C4.5 Algoritması

ID3'ün geliştirilmiş hali:

#### Kazanç Oranı (Gain Ratio)
```
GainRatio(S, A) = Gain(S, A) / SplitInfo(S, A)

SplitInfo(S, A) = -Σ (|S_v|/|S|) × log₂(|S_v|/|S|)
```

- Çok değerli öznitelikleri cezalandırır
- Daha dengeli bölme yapar

#### C4.5'un İyileştirmeleri
- ✅ Sayısal özniteliklerle çalışır (threshold belirleme)
- ✅ Eksik değerleri yönetir
- ✅ Budama (pruning) yapar
- ✅ Kazanç oranı kullanır

### 6. CART (Classification and Regression Trees)

#### Gini İndeksi
```
Gini(S) = 1 - Σ p_i²
```

**Örnek:**
- 9 pozitif, 5 negatif
- Gini = 1 - [(9/14)² + (5/14)²] = 0.459

#### Gini Split
```
GiniSplit(S, A) = Σ (|S_v|/|S|) × Gini(S_v)
```

En düşük Gini Split değerine sahip özniteliği seç

#### CART Özellikleri
- Binary splits (ikili bölme)
- Hem sınıflandırma hem regresyon
- Sayısal ve kategorik verilerle çalışır
- Cost-complexity pruning

### 7. Budama (Pruning)

#### Neden Budama?
- Aşırı öğrenmeyi önler
- Genelleme yeteneğini artırır
- Modeli basitleştirir

#### Budama Türleri

**Pre-pruning (Erken Durdurma)**
- Ağaç büyürken bazı dalları büyütmeme
- Kriterler:
  - Maksimum derinlik
  - Minimum örnek sayısı
  - Minimum bilgi kazancı

**Post-pruning (Sonradan Budama)**
- Ağacı tam büyüt
- Sonra gereksiz dalları kes
- Daha etkili ama yavaş

#### Cost-Complexity Pruning
```
Cost(T) = Error(T) + α × |Leaves(T)|
```
- α: Complexity parameter
- Hata ve karmaşıklık dengesi

### 8. Model Değerlendirme

#### Karmaşıklık Matrisi (Confusion Matrix)
```
                Predicted
              Pos    Neg
Actual  Pos   TP     FN
        Neg   FP     TN
```

#### Metrikler
```
Accuracy = (TP + TN) / Total

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
```

## 💻 Uygulama İçeriği

### Lab 1: Scikit-learn ile Karar Ağacı
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Model oluşturma
clf = DecisionTreeClassifier(criterion='gini', max_depth=5)
clf.fit(X_train, y_train)

# Tahmin
y_pred = clf.predict(X_test)

# Değerlendirme
print(accuracy_score(y_test, y_pred))
```

### Lab 2: Karar Ağacını Görselleştirme
```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=features)
plt.show()
```

## 📝 Ödevler

### Ödev 1: Elle Karar Ağacı Oluşturma
Küçük veri setinde manuel bilgi kazancı hesaplama

### Ödev 2: Scikit-learn Uygulaması
Iris veri setinde karar ağacı modeli

## 🔑 Anahtar Kavramlar
- Supervised learning
- Decision tree induction
- Entropy and information gain
- Gini index
- ID3, C4.5, CART
- Overfitting and pruning
- Confusion matrix
- Model evaluation metrics

## 💡 Pratik İpuçları

1. **Max depth ayarlayın:**
   ```python
   clf = DecisionTreeClassifier(max_depth=5)
   ```

2. **Min samples split:**
   ```python
   clf = DecisionTreeClassifier(min_samples_split=10)
   ```

3. **Feature importance:**
   ```python
   importances = clf.feature_importances_
   ```

4. **Cross-validation kullanın:**
   ```python
   from sklearn.model_selection import cross_val_score
   scores = cross_val_score(clf, X, y, cv=5)
   ```

## ❓ Sıkça Sorulan Sorular

**S: Gini mi Entropy mi kullanmalıyım?**
C: Genelde çok fark etmez. Gini biraz daha hızlı hesaplanır.

**S: Max depth ne kadar olmalı?**
C: Cross-validation ile bulun. Genelde 3-10 arası iyi sonuç verir.

**S: Karar ağacı regresyon için kullanılabilir mi?**
C: Evet, CART hem sınıflandırma hem regresyon yapabilir.

---

**Sonraki Hafta:** Kural Çıkarımı ve k-NN Algoritması
