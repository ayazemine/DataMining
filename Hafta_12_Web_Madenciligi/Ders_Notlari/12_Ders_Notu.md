# Hafta 12: Web Madenciliği ve Tavsiye Sistemleri

## 📋 Web Madenciliği Nedir?

Web'den otomatik olarak yararlı bilgi çıkarma.

## 🌐 Web Madenciliği Türleri

### 1. Web Content Mining (İçerik Madenciliği)
- Metin, resim, video analizi
- Arama motorları
- Duygu analizi

### 2. Web Structure Mining (Yapı Madenciliği)
- Link analizi
- PageRank
- HITS algoritması

### 3. Web Usage Mining (Kullanım Madenciliği)
- Kullanıcı davranış analizi
- Clickstream analizi
- Session analizi

## 🔗 PageRank Algoritması

### Temel İdea
"Önemli sayfalardan gelen linkler daha değerlidir."

### Formül
```
PR(A) = (1-d) + d × Σ(PR(Ti) / C(Ti))

PR(A): A sayfasının PageRank'i
d: Damping factor (0.85)
Ti: A'ya link veren sayfalar
C(Ti): Ti'nin dışa verdiği link sayısı
```

### Python Implementasyonu

```python
import numpy as np

def pagerank(M, num_iterations=100, d=0.85):
    """
    M: Link matrisi (MxM), M[i][j] = 1 if i->j
    """
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    
    M_hat = (d * M + (1 - d) / N)
    
    for i in range(num_iterations):
        v = M_hat @ v
    
    return v

# Örnek
M = np.array([
    [0, 1/2, 1/2, 0],
    [1/3, 0, 0, 1/2],
    [1/3, 0, 0, 1/2],
    [1/3, 1/2, 1/2, 0]
])

ranks = pagerank(M)
print("PageRank skorları:", ranks.flatten())
```

### NetworkX ile PageRank

```python
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 2)])

pr = nx.pagerank(G, alpha=0.85)
print("PageRank:", pr)
```

## 🎯 HITS Algoritması

**Hyperlink-Induced Topic Search**

### İki Tür Sayfa
- **Authorities:** İyi içerik sayfaları
- **Hubs:** İyi authority'lere link veren sayfalar

### Formüller
```
Authority Score: a(p) = Σ h(q)  (p'ye link veren q'ların hub skorları)
Hub Score: h(p) = Σ a(q)  (p'nin link verdiği q'ların authority skorları)
```

```python
def hits(G, max_iter=100):
    nodes = list(G.nodes())
    h = {node: 1.0 for node in nodes}
    a = {node: 1.0 for node in nodes}
    
    for _ in range(max_iter):
        # Update authority
        for node in nodes:
            a[node] = sum(h[pred] for pred in G.predecessors(node))
        
        # Update hub
        for node in nodes:
            h[node] = sum(a[succ] for succ in G.successors(node))
        
        # Normalize
        norm_a = sum(a.values())
        norm_h = sum(h.values())
        a = {k: v/norm_a for k, v in a.items()}
        h = {k: v/norm_h for k, v in h.items()}
    
    return h, a

hubs, authorities = hits(G)
```

## 🛒 Tavsiye Sistemleri (Recommender Systems)

### Türleri

**1. Content-Based Filtering**
Ürün özelliklerine göre tavsiye.
```
Kullanıcı aksiyon filmlerini seviyor → Aksiyon filmleri öner
```

**2. Collaborative Filtering**
Benzer kullanıcıların tercihlerine göre tavsiye.
```
User A ve User B benzer → A'nın beğendiği, B'nin görmediğini öner
```

**3. Hybrid Systems**
Her iki yöntemi birleştir.

## 👥 Collaborative Filtering

### User-Based CF

**Adımlar:**
1. Kullanıcılar arası benzerlik hesapla
2. Benzer kullanıcıları bul
3. Onların beğendiği ürünleri öner

**Cosine Similarity:**
```python
from sklearn.metrics.pairwise import cosine_similarity

# user_item_matrix: kullanıcı x ürün
user_similarity = cosine_similarity(user_item_matrix)

# En benzer 5 kullanıcı
similar_users = user_similarity[user_id].argsort()[-6:-1][::-1]
```

### Item-Based CF

**Adımlar:**
1. Ürünler arası benzerlik hesapla
2. Kullanıcının beğendiği ürünlere benzer ürünler bul
3. Öner

```python
# Ürün benzerliği
item_similarity = cosine_similarity(user_item_matrix.T)

# Kullanıcının beğendiği ürünler
liked_items = user_item_matrix[user_id] > 0

# Benzer ürünler
recommendations = item_similarity[liked_items].sum(axis=0)
```

## 🧮 Matrix Factorization

### SVD (Singular Value Decomposition)

```
R ≈ U × Σ × V^T

R: user_item_matrix (m × n)
U: user_features (m × k)
Σ: singular values (k × k)
V: item_features (n × k)
```

### Python ile SVD

```python
from scipy.sparse.linalg import svds

# SVD
U, sigma, Vt = svds(user_item_matrix, k=50)

# Tahmin
sigma = np.diag(sigma)
predictions = np.dot(np.dot(U, sigma), Vt)

# En yüksek skorlu ürünler
user_predictions = predictions[user_id]
top_items = user_predictions.argsort()[-10:][::-1]
```

### Surprise Kütüphanesi

```python
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate

# Veri yükleme
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader)

# SVD modeli
algo = SVD(n_factors=50, n_epochs=20, lr_all=0.005, reg_all=0.02)

# Cross-validation
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Eğitim
trainset = data.build_full_trainset()
algo.fit(trainset)

# Tahmin
pred = algo.predict(user_id, movie_id)
print(f"Predicted rating: {pred.est:.2f}")
```

## 📊 Değerlendirme Metrikleri

### Rating Prediction

**RMSE (Root Mean Square Error):**
```
RMSE = √(Σ(r̂ - r)² / n)
```

**MAE (Mean Absolute Error):**
```
MAE = Σ|r̂ - r| / n
```

### Top-N Recommendation

**Precision@K:**
```
Precision@K = |İlgili ∩ Önerilen| / K
```

**Recall@K:**
```
Recall@K = |İlgili ∩ Önerilen| / |İlgili|
```

**MAP (Mean Average Precision)**

**NDCG (Normalized Discounted Cumulative Gain)**

```python
from sklearn.metrics import ndcg_score

# y_true: gerçek relevance skorları
# y_score: tahmin skorları
ndcg = ndcg_score([y_true], [y_score], k=10)
```

## 🎬 Pratik Örnek: Film Tavsiye Sistemi

```python
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

# MovieLens veri seti
ratings = pd.read_csv('ratings.csv')

# Surprise formatına çevir
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(data, test_size=0.2)

# Model
algo = SVD(n_factors=100, n_epochs=20)
algo.fit(trainset)

# Test
predictions = algo.test(testset)

# Metriklere
from surprise import accuracy
rmse = accuracy.rmse(predictions)
mae = accuracy.mae(predictions)

# Kullanıcıya tavsiye
def get_top_n_recommendations(algo, user_id, n=10):
    # Tüm filmler
    all_movies = ratings['movieId'].unique()
    
    # Kullanıcının izlediği filmler
    watched = ratings[ratings['userId'] == user_id]['movieId'].values
    
    # İzlemediği filmler
    not_watched = [m for m in all_movies if m not in watched]
    
    # Tahminler
    predictions = [algo.predict(user_id, movie_id) for movie_id in not_watched]
    
    # Sırala
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    # Top N
    return predictions[:n]

# Örnek kullanım
user_id = 1
recommendations = get_top_n_recommendations(algo, user_id, n=10)

print(f"Top 10 film tavsiyeleri (User {user_id}):")
for pred in recommendations:
    print(f"MovieID: {pred.iid}, Predicted Rating: {pred.est:.2f}")
```

## 🔥 Cold Start Problemi

Yeni kullanıcı/ürün için yeterli veri yok.

### Çözümler
1. **Hybrid approach:** Content-based + collaborative
2. **Popularity-based:** Popüler ürünleri öner
3. **User profiling:** İlk kayıtta tercihler sor
4. **Side information:** Demographic bilgi kullan

## 💡 İpuçları

1. **Implicit feedback:** Like, click, view → explicit rating'den daha bol
2. **Temporal dynamics:** Kullanıcı tercihleri zamanla değişir
3. **Diversity:** Sadece benzer ürün önerme
4. **Serendipity:** Sürpriz öneriler
5. **Context-aware:** Zaman, lokasyon, cihaz bilgisi kullan
6. **Scalability:** Büyük veri setleri için approximate methods

## 📚 Kütüphaneler

- **Surprise:** Python için collaborative filtering
- **LightFM:** Hybrid recommender systems
- **Implicit:** Implicit feedback için CF
- **TensorFlow Recommenders:** Neural collaborative filtering
- **NetworkX:** Graph-based methods (PageRank, HITS)
