# Hafta 8: Birliktelik Kuralı Madenciliği

## 📋 Giriş

Market sepet analizi, e-ticaret önerileri, çapraz satış stratejileri...

**Hedef:** X alındığında Y'de alınır mı?

## 🎯 Temel Kavramlar

### Itemset
Birlikte satın alınan ürün kümesi.
```
{Ekmek, Süt, Peynir}
```

### Transaction (İşlem)
Bir müşterinin alışveriş sepeti.
```
T1: {Ekmek, Süt}
T2: {Ekmek, Süt, Peynir}
T3: {Süt, Peynir}
```

### Association Rule (Birliktelik Kuralı)
```
X → Y
Ekmek → Süt
{Ekmek, Peynir} → Süt
```

## 📊 Metrikler

### 1. Support (Destek)
Bir itemset'in tüm işlemlerdeki oranı.

```
Support({X}) = |{X içeren işlemler}| / |Tüm işlemler|

Support({Ekmek, Süt}) = 3/5 = 0.6
```

**Yorumlama:**
- Support = 0.6 → İşlemlerin %60'ında birlikte alınıyor

### 2. Confidence (Güven)
X alındığında Y'nin de alınma olasılığı.

```
Confidence(X → Y) = Support(X ∪ Y) / Support(X)

Confidence(Ekmek → Süt) = Support({Ekmek, Süt}) / Support(Ekmek)
```

**Yorumlama:**
- Confidence = 0.75 → Ekmek alanların %75'i süt de alıyor

### 3. Lift
X ve Y'nin bağımsız olup olmadığını gösterir.

```
Lift(X → Y) = Confidence(X → Y) / Support(Y)
            = Support(X ∪ Y) / (Support(X) × Support(Y))
```

**Yorumlama:**
- Lift > 1: Pozitif korelasyon (X alınınca Y alma olasılığı artar)
- Lift = 1: Bağımsız (korelasyon yok)
- Lift < 1: Negatif korelasyon (X alınınca Y alma olasılığı azalır)

### 4. Conviction
```
Conviction(X → Y) = (1 - Support(Y)) / (1 - Confidence(X → Y))
```

Kural ne kadar güçlü?

### 5. Leverage
```
Leverage(X → Y) = Support(X ∪ Y) - Support(X) × Support(Y)
```

### 6. Kulpa
```
Kulpa(X → Y) = (Support(X ∪ Y) - Support(X) × Support(Y)) / (Support(X) × (1 - Support(X)))
```

## 🔍 Apriori Algoritması

### İlke
Bir itemset sık değilse, onun tüm supersetleri de sık değildir.

```
Support({Ekmek, Süt, Peynir}) ≤ Support({Ekmek, Süt})
```

### Algoritma Adımları

```
1. L1 = {sık 1-itemsets}
2. k = 2
3. While Lk-1 ≠ ∅:
    a. Ck = apriori_gen(Lk-1)  # Aday itemsetler
    b. Her işlem t için:
        Ct = subset(Ck, t)
        Her aday c ∈ Ct için:
            count[c] += 1
    c. Lk = {c ∈ Ck | count[c] ≥ min_support}
    d. k += 1
4. Return ∪kLk
```

### apriori_gen Fonksiyonu

**Join step:**
```
{A, B} ∪ {A, C} → {A, B, C}
```

**Prune step:**
```
Eğer {A, B, C}'nin herhangi bir (k-1) subset'i sık değilse, 
{A, B, C}'yi çıkar.
```

## 💻 Python Uygulaması

### mlxtend Kütüphanesi

```python
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Örnek veri
dataset = [
    ['Ekmek', 'Süt'],
    ['Ekmek', 'Süt', 'Peynir'],
    ['Süt', 'Peynir'],
    ['Ekmek', 'Süt', 'Peynir', 'Yumurta'],
    ['Ekmek', 'Yumurta']
]

# One-hot encoding
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print(df)
```

Output:
```
   Ekmek  Peynir   Süt  Yumurta
0   True   False  True    False
1   True    True  True    False
2  False    True  True    False
3   True    True  True     True
4   True   False False     True
```

### Sık Itemset Bulma

```python
# Apriori
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
print(frequent_itemsets)
```

Output:
```
   support    itemsets
0      0.8      (Ekmek)
1      0.6     (Peynir)
2      0.8        (Süt)
3      0.6  (Ekmek, Süt)
4      0.6 (Peynir, Süt)
```

### Kural Çıkarma

```python
# Kurallar
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
```

Output:
```
  antecedents consequents  support  confidence      lift
0      (Ekmek)       (Süt)     0.6        0.75  0.9375
1       (Süt)    (Peynir)     0.6        0.75  1.2500
```

### Tüm Metrikler

```python
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print(rules.columns)
# ['antecedents', 'consequents', 'antecedent support', 'consequent support',
#  'support', 'confidence', 'lift', 'leverage', 'conviction']
```

## 🛒 Gerçek Dünya Örneği: Market Sepet Analizi

```python
# Gerçek market verisi
df_market = pd.read_csv('transactions.csv')

# Gruplama (işlem bazlı)
basket = df_market.groupby(['TransactionID', 'Product'])['Quantity'].sum().unstack().fillna(0)

# Binary'e çevir (alındı/alınmadı)
basket_sets = basket.applymap(lambda x: 1 if x > 0 else 0)

# Apriori
frequent_items = apriori(basket_sets, min_support=0.05, use_colnames=True)

# Kurallar
rules = association_rules(frequent_items, metric="lift", min_threshold=1.0)

# En iyi kurallar
top_rules = rules.sort_values('lift', ascending=False).head(10)
print(top_rules)
```

## 📈 FP-Growth Algoritması

Apriori'den daha hızlı alternatif.

**Avantajlar:**
- Tek pass ile FP-tree oluşturur
- Aday itemset üretmez
- Büyük veri setlerinde daha hızlı

```python
from mlxtend.frequent_patterns import fpgrowth

frequent_items_fp = fpgrowth(df, min_support=0.4, use_colnames=True)
```

## 🎯 Uygulama Senaryoları

### 1. E-Ticaret Önerileri
```
"Bu ürünü alanlar şunları da aldı"
{Laptop} → {Laptop Çantası, Mouse}
```

### 2. Çapraz Satış
```
{Kredi Kartı} → {Sigorta}
```

### 3. Raf Yerleşimi
```
Birlikte alınan ürünleri yakın raflara koy
```

### 4. Kampanya Stratejisi
```
{Bebek Bezi} → {Bebek Maması}
Birlikte indirim yap
```

## ⚠️ Dikkat Edilmesi Gerekenler

1. **Simpson's Paradox:** Genel veriye bakıldığında farklı, alt gruplara bakıldığında farklı sonuç
2. **Spurious correlations:** Sahte korelasyonlar
3. **Min support çok düşük:** Çok fazla kural
4. **Min support çok yüksek:** Hiç kural yok
5. **Confidence ≠ Causation:** Korelasyon ≠ Nedensellik

## 💡 İpuçları

1. **Domain knowledge kullan:** Anlamsız kuralları filtrele
2. **Lift'e odaklan:** Confidence tek başına yeterli değil
3. **Interestingness measures:** Farklı metrikleri dene
4. **Temporal analysis:** Zaman boyutunu ekle
5. **Visualization:** Kuralları görselleştir (networkx, plotly)

## 📊 Görselleştirme

```python
import networkx as nx
import matplotlib.pyplot as plt

# Graph oluştur
G = nx.DiGraph()

for _, row in rules.iterrows():
    G.add_edge(str(row['antecedents']), 
               str(row['consequents']), 
               weight=row['lift'])

# Çiz
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=10, arrows=True)
plt.title('Association Rules Network')
plt.show()
```
