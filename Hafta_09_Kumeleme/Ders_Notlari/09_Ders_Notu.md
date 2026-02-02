# Hafta 9: Kümeleme Algoritmaları

## 📋 Kümeleme Nedir?

**Unsupervised learning** - Etiket yok, benzer verileri gruplama

### Kullanım Alanları
- Müşteri segmentasyonu
- Görüntü segmentasyonu
- Anomali tespiti
- Veri sıkıştırma
- Ön işleme

## 🎯 K-Means Algoritması

### Algoritma Adımları
1. K merkez noktası rastgele seç
2. Her veriyi en yakın merkeze ata
3. Merkezleri güncelle (kümenin ortalaması)
4. Değişim olmazsa dur, yoksa 2'ye dön

### K-Means++
Başlangıç merkezlerini akıllıca seçerek daha iyi sonuç.

### K Değeri Seçimi

**Elbow Method:**
```python
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
plt.plot(range(1, 11), inertias)
```

**Silhouette Score:**
```
s = (b - a) / max(a, b)
s ∈ [-1, 1], yüksek iyi
```

### Avantajlar & Dezavantajlar

✅ Basit ve hızlı
✅ Büyük veri setlerinde etkili
✅ Ölçeklenebilir

❌ K değeri önceden bilinmeli
❌ Aykırı değerlere duyarlı
❌ Küresel olmayan kümeler için zayıf
❌ Farklı boyut/yoğunlukta kümeler için uygun değil

## 🌳 Hiyerarşik Kümeleme

### Agglomerative (Bottom-Up)
1. Her veri ayrı küme
2. En yakın iki kümeyi birleştir
3. Tek küme kalana kadar tekrarla

### Divisive (Top-Down)
1. Tüm veri tek küme
2. En heterojen kümeyi böl
3. Her veri ayrı küme olana kadar

### Linkage Metodları
- **Single:** En yakın noktalar arası mesafe
- **Complete:** En uzak noktalar arası mesafe
- **Average:** Ortalama mesafe
- **Ward:** Varyans minimizasyonu (en popüler)

### Dendrogram
```python
from scipy.cluster.hierarchy import dendrogram, linkage

Z = linkage(X, method='ward')
dendrogram(Z)
plt.show()
```

## 🎨 DBSCAN (Density-Based)

### Parametreler
- **eps (ε):** Komşuluk yarıçapı
- **min_samples:** Minimum nokta sayısı

### Nokta Tipleri
- **Core point:** eps içinde min_samples kadar komşu var
- **Border point:** Core point komşusu ama kendisi core değil
- **Noise:** Ne core ne border (outlier)

### Avantajlar
✅ K değeri gerekmez
✅ Herhangi şekilde küme bulabilir
✅ Noise/outlier tespit eder
✅ Farklı boyutlarda kümeler

❌ eps ve min_samples seçimi zor
❌ Farklı yoğunlukta kümeler için zayıf

## 📊 Küme Değerlendirme

### İç Metrikler (Internal)
- **Silhouette Score:** [-1, 1], yüksek iyi
- **Davies-Bouldin Index:** Düşük iyi
- **Calinski-Harabasz Index:** Yüksek iyi

### Dış Metrikler (External) - Etiket varsa
- **Adjusted Rand Index (ARI)**
- **Normalized Mutual Information (NMI)**

## 💻 Python Kodu

```python
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Hiyerarşik
hierarchical = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = hierarchical.fit_predict(X)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)

# Değerlendirme
score = silhouette_score(X, labels)
print(f"Silhouette Score: {score:.3f}")
```

## 🎯 Hangi Algoritmayı Seçmeli?

- **K-Means:** Hızlı, küresel kümeler, K biliniyor
- **Hiyerarşik:** K bilinmiyor, küçük veri, dendrogram gerekli
- **DBSCAN:** Farklı şekiller, outlier önemli, yoğunluk tabanlı

## 📈 Görselleştirme

```python
import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], 
            kmeans.cluster_centers_[:, 1], 
            marker='x', s=200, c='red', label='Merkezler')
plt.legend()
plt.show()
```
