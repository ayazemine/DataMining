# Hafta 13: Büyük Veri Teknolojileri

## 📋 Büyük Veri Nedir?

### 3V Modeli (Klasik)
- **Volume (Hacim):** TB, PB, EB boyutunda veri
- **Velocity (Hız):** Hızlı veri akışı
- **Variety (Çeşitlilik):** Farklı formatlarda veri

### 5V Modeli (Genişletilmiş)
- **Veracity (Doğruluk):** Veri kalitesi
- **Value (Değer):** İş değeri

## 🐘 Hadoop Ekosistemi

### Hadoop Nedir?
Dağıtık veri depolama ve işleme framework'ü.

### Bileşenler

**1. HDFS (Hadoop Distributed File System)**
- Verileri bloklar halinde dağıtık depolar
- Varsayılan blok boyutu: 128 MB
- Replication: Her blok 3 kopya (varsayılan)
- NameNode: Metadata yönetimi
- DataNode: Veri depolama

**2. YARN (Yet Another Resource Negotiator)**
- Kaynak yönetimi
- İş planlama
- ResourceManager + NodeManager

**3. MapReduce**
- Dağıtık veri işleme modeli
- Map: Paralel işlem
- Reduce: Sonuçları birleştir

## 🗺️ MapReduce Programlama Modeli

### Map Fonksiyonu
```
map(key1, value1) → list(key2, value2)
```

### Reduce Fonksiyonu
```
reduce(key2, list(value2)) → list(value3)
```

### Örnek: Kelime Sayma (Word Count)

**Input:**
```
Hello World
Hello Hadoop
```

**Map Phase:**
```
(Hello, 1)
(World, 1)
(Hello, 1)
(Hadoop, 1)
```

**Shuffle & Sort:**
```
(Hadoop, [1])
(Hello, [1, 1])
(World, [1])
```

**Reduce Phase:**
```
(Hadoop, 1)
(Hello, 2)
(World, 1)
```

## ⚡ Apache Spark

### Spark vs Hadoop

| Özellik | Hadoop MapReduce | Apache Spark |
|---------|------------------|--------------|
| Hız | Yavaş (disk I/O) | Hızlı (in-memory) |
| Kullanım | Karmaşık | Kolay (Python, Scala, Java, R) |
| ML/Graph | Sınırlı | MLlib, GraphX |
| Streaming | Zor | Spark Streaming |

### Spark RDD (Resilient Distributed Dataset)

Dağıtık, değişmez veri koleksiyonu.

**Transformations (Lazy):**
- map, filter, flatMap
- join, union
- groupByKey, reduceByKey

**Actions (Eager):**
- count, collect, save
- reduce, fold

### PySpark Örnek

```python
from pyspark.sql import SparkSession

# Spark session oluştur
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Veri oku
text = spark.read.text("input.txt")

# Word count
from pyspark.sql.functions import explode, split

words = text.select(explode(split(text.value, " ")).alias("word"))
word_count = words.groupBy("word").count()

# Sonuçları göster
word_count.show()
```

### Spark DataFrame

Pandas benzeri API, dağıtık.

```python
# CSV okuma
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# SQL sorguları
df.createOrReplaceTempView("people")
result = spark.sql("SELECT * FROM people WHERE age > 30")

# Transformations
df.select("name", "age") \
  .filter(df.age > 21) \
  .groupBy("age").count() \
  .show()
```

## 🤖 Spark MLlib

Dağıtık makine öğrenmesi kütüphanesi.

### Örnek: Classification

```python
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

# Feature vector oluştur
assembler = VectorAssembler(
    inputCols=["feature1", "feature2", "feature3"],
    outputCol="features"
)
df_features = assembler.transform(df)

# Train-test split
train, test = df_features.randomSplit([0.7, 0.3])

# Model eğit
lr = LogisticRegression(featuresCol="features", labelCol="label")
model = lr.fit(train)

# Tahmin
predictions = model.transform(test)

# Değerlendirme
from pyspark.ml.evaluation import BinaryClassificationEvaluator
evaluator = BinaryClassificationEvaluator()
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")
```

### MLlib Algoritmaları
- **Classification:** Logistic Regression, Decision Trees, Random Forest, Naive Bayes
- **Regression:** Linear Regression, Generalized Linear Models
- **Clustering:** K-Means, Gaussian Mixture
- **Collaborative Filtering:** ALS

## 📊 Spark Streaming

Gerçek zamanlı veri işleme.

```python
from pyspark.streaming import StreamingContext

# StreamingContext oluştur (1 saniye batch)
ssc = StreamingContext(spark.sparkContext, 1)

# Veri akışı
lines = ssc.socketTextStream("localhost", 9999)

# Transformations
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
word_counts = pairs.reduceByKey(lambda a, b: a + b)

# Çıktı
word_counts.pprint()

# Başlat
ssc.start()
ssc.awaitTermination()
```

## 🔧 Spark Deployment

### Local Mode
```python
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("MyApp") \
    .getOrCreate()
```

### Cluster Mode
- **Standalone:** Spark'ın kendi cluster manager'ı
- **YARN:** Hadoop YARN üzerinde
- **Mesos:** Apache Mesos üzerinde
- **Kubernetes:** K8s üzerinde

## 💡 Best Practices

1. **Partitioning:** Veriyi uygun şekilde bölümle
2. **Caching:** Sık kullanılan verileri cache'le
3. **Broadcast variables:** Küçük lookup table'ları broadcast et
4. **Avoid shuffling:** Shuffle işlemlerini minimize et
5. **Use DataFrames:** RDD yerine DataFrame tercih et
6. **Memory tuning:** Executor/driver memory'yi optimize et

## 🎯 Ne Zaman Büyük Veri Araçları?

**Kullan:**
- Veri > RAM
- Dağıtık işlem gerekli
- Ölçeklenebilirlik önemli
- Streaming veri

**Kullanma:**
- Veri < 10 GB
- Tek makine yeterli
- Pandas/NumPy ile hallediliyor

## 📚 Kaynaklar

- Apache Spark: https://spark.apache.org/
- PySpark Documentation: https://spark.apache.org/docs/latest/api/python/
- Databricks: https://databricks.com/ (Spark platformu)
- Kaggle Spark Tutorials

## 💻 Kurulum

```bash
# PySpark kurulumu
pip install pyspark

# Jupyter'da kullanım
pip install jupyter
jupyter notebook
```

```python
# Notebook'ta Spark başlatma
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()
```
