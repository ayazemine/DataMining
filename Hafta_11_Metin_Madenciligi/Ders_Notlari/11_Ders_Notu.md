# Hafta 11: Metin Madenciliği ve NLP

## 📋 Metin Madenciliği Nedir?

Yapısal olmayan metinlerden bilgi çıkarma süreci.

### Uygulama Alanları
- Duygu analizi (Sentiment Analysis)
- Spam filtreleme
- Chatbot'lar
- Makine çevirisi
- Metin özetleme
- Soru-cevap sistemleri

## 🔧 Metin Ön İşleme

### 1. Tokenization (Simgeleme)
```python
text = "Veri madenciliği çok ilginç!"
tokens = text.split()  # ['Veri', 'madenciliği', 'çok', 'ilginç!']
```

### 2. Lowercasing (Küçük harfe çevirme)
```python
text = text.lower()  # "veri madenciliği çok ilginç!"
```

### 3. Noktalama İşaretlerini Kaldırma
```python
import string
text = text.translate(str.maketrans('', '', string.punctuation))
```

### 4. Stop Words (Durak Kelimeleri) Kaldırma
```python
from nltk.corpus import stopwords
stop_words = set(stopwords.words('turkish'))
tokens = [w for w in tokens if w not in stop_words]
```

### 5. Stemming (Kök Bulma)
```python
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('turkish')
stemmed = [stemmer.stem(word) for word in tokens]
```

### 6. Lemmatization (Kök Sözcük Bulma)
```python
import spacy
nlp = spacy.load('tr_core_news_sm')
doc = nlp(text)
lemmas = [token.lemma_ for token in doc]
```

## 📊 Metin Temsili

### Bag of Words (BoW)
```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'Veri madenciliği öğreniyorum',
    'Python ile veri analizi',
    'Metin madenciliği projesi'
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

### TF-IDF (Term Frequency-Inverse Document Frequency)

**TF:** Kelime sıklığı
```
TF(t, d) = (Dokümandaki t sayısı) / (Dokümandaki toplam kelime)
```

**IDF:** Ters doküman frekansı
```
IDF(t) = log(Toplam doküman / t içeren doküman)
```

**TF-IDF:**
```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=1000)
X = tfidf.fit_transform(corpus)
```

## 😊 Duygu Analizi (Sentiment Analysis)

### Yaklaşımlar

**1. Sözlük Tabanlı (Lexicon-Based)**
```python
positive_words = ['iyi', 'güzel', 'harika', 'mükemmel']
negative_words = ['kötü', 'berbat', '안좋은']

def sentiment_score(text):
    words = text.lower().split()
    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)
    return pos - neg
```

**2. Makine Öğrenmesi Tabanlı**
```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Veri: (metin, etiket) - etiket: 0=negatif, 1=pozitif
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

nb = MultinomialNB()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)
```

**3. Derin Öğrenme Tabanlı**
- LSTM, GRU
- BERT, GPT
- Transformer modelleri

## 📖 Konu Modelleme (Topic Modeling)

### LDA (Latent Dirichlet Allocation)

Her doküman, konuların bir karışımıdır.
Her konu, kelimelerin bir dağılımıdır.

```python
from sklearn.decomposition import LatentDirichletAllocation

lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X)

# Konuları görüntüle
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda.components_):
    top_words = [feature_names[i] for i in topic.argsort()[-10:]]
    print(f"Konu {topic_idx}: {', '.join(top_words)}")
```

## 🌐 Word Embeddings

### Word2Vec
Kelimeleri vektör uzayında temsil eder.

```python
from gensim.models import Word2Vec

sentences = [['veri', 'madenciliği'], ['metin', 'analizi']]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

# Benzer kelimeler
similar = model.wv.most_similar('veri', topn=5)
```

## 💻 Pratik Örnek: Twitter Duygu Analizi

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Veri yükleme
df = pd.read_csv('tweets.csv')

# Ön işleme
def preprocess(text):
    text = text.lower()
    # Daha fazla ön işleme...
    return text

df['clean_text'] = df['text'].apply(preprocess)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['clean_text'])
y = df['sentiment']  # 0: negatif, 1: pozitif

# Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Değerlendirme
y_pred = nb.predict(X_test)
print(classification_report(y_test, y_pred))
```

## 🔑 Önemli Kütüphaneler

- **NLTK:** Natural Language Toolkit
- **spaCy:** Hızlı NLP kütüphanesi
- **Gensim:** Topic modeling ve word embeddings
- **TextBlob:** Basit sentiment analysis
- **Transformers (Hugging Face):** BERT, GPT modelleri

## 📚 Türkçe NLP Kaynakları

```python
# NLTK Türkçe
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
turkish_stops = stopwords.words('turkish')

# spaCy Türkçe
# python -m spacy download tr_core_news_sm
import spacy
nlp = spacy.load('tr_core_news_sm')
```

## 🎯 İpuçları

1. **Veri temizliği önemli:** Metin verisi çok kirli olabilir
2. **Domain knowledge:** Sosyal medya vs haber metni farklı
3. **Class imbalance:** Duygu analizinde sık görülür
4. **Preprocessing pipeline:** Tutarlı ön işleme
5. **Model seçimi:** Başla basit (Naive Bayes), gerekirse karmaşıklaştır
