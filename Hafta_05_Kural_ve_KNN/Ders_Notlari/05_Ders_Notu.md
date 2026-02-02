# Hafta 5: Kural Çıkarımı ve k-NN Algoritması

## 📋 Hafta Hedefleri
- Birliktelik kurallarını anlama
- Apriori algoritmasını öğrenme
- Market sepet analizi yapabilme
- k-NN algoritmasını kavrama
- Mesafe metriklerini kullanabilme

## 📚 Birliktelik Kuralları (Association Rules)

### Temel Kavramlar

**Örnek:** Market sepet analizi
```
İşlem 1: {Ekmek, Süt, Peynir}
İşlem 2: {Ekmek, Süt}
İşlem 3: {Ekmek, Peynir}
İşlem 4: {Süt, Peynir}
İşlem 5: {Ekmek, Süt, Peynir, Yumurta}
```

### Metrikler

**Support (Destek):**
```
Support(X) = İşlemde X'in bulunma sayısı / Toplam işlem sayısı
Support({Ekmek, Süt}) = 3/5 = 0.6
```

**Confidence (Güven):**
```
Confidence(X → Y) = Support(X ∪ Y) / Support(X)
Confidence(Ekmek → Süt) = Support({Ekmek, Süt}) / Support(Ekmek)
                         = 0.6 / 0.8 = 0.75
```

**Lift:**
```
Lift(X → Y) = Confidence(X → Y) / Support(Y)
Lift > 1: Pozitif korelasyon
Lift = 1: Bağımsız
Lift < 1: Negatif korelasyon
```

### Apriori Algoritması

**İlke:** Bir itemset sık değilse, onun tüm supersetleri de sık değildir.

**Adımlar:**
1. Minimum support belirle
2. 1-itemset'leri bul
3. Sık olanları seç
4. k-itemset'leri oluştur
5. Sık olanları bul
6. Tekrarla

## 🎯 k-NN (k-Nearest Neighbors)

### Algoritma

1. K değerini seç (örn: k=5)
2. Test örneği için tüm eğitim örneklerine mesafeyi hesapla
3. En yakın k komşuyu bul
4. Çoğunluk oylamasıyla sınıfı belirle

### Mesafe Metrikleri

**Euclidean Distance:**
```
d = √(Σ(x_i - y_i)²)
```

**Manhattan Distance:**
```
d = Σ|x_i - y_i|
```

**Minkowski Distance:**
```
d = (Σ|x_i - y_i|^p)^(1/p)
```

### k-NN Parametreleri

- **k değeri:** Küçük k → overfitting, Büyük k → underfitting
- **Mesafe metriği:** Euclidean, Manhattan, vb.
- **Ağırlıklandırma:** Uniform vs distance-weighted

### Avantajlar & Dezavantajlar

✅ Basit ve sezgisel
✅ Varsayım gerektirmez
✅ Çok sınıflı problemlerde etkili

❌ Yavaş (tüm mesafeleri hesaplar)
❌ Bellek yoğun
❌ Ölçeklendirme gerektirir
❌ Yüksek boyutta zayıf (curse of dimensionality)

## 💻 Python Uygulaması

```python
# Apriori
from mlxtend.frequent_patterns import apriori, association_rules

frequent_items = apriori(df, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_items, metric="confidence", min_threshold=0.7)

# k-NN
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
```

## 📝 Ödevler
- Market sepet analizi projesi
- k-NN ile sınıflandırma
- k değeri optimizasyonu
