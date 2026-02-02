# Kurulum Rehberi - Veri Madenciliği Dersi

## Python Kurulumu

### 1. Anaconda İndirme ve Kurulum
Anaconda, Python ve veri bilimi kütüphanelerini bir arada sunan bir dağıtımdır.

**İndirme:**
- [Anaconda İndirme Sayfası](https://www.anaconda.com/download)
- Python 3.10 veya üzeri versiyonu seçin
- İşletim sisteminize uygun versiyonu indirin

**Kurulum Adımları:**
1. İndirdiğiniz dosyayı çalıştırın
2. Kurulum sihirbazını takip edin
3. "Add Anaconda to PATH" seçeneğini işaretleyin (önerilir)
4. Kurulum tamamlandıktan sonra terminal/command prompt'u yeniden başlatın

### 2. Gerekli Kütüphaneleri Yükleme

Terminal/Anaconda Prompt'u açın ve aşağıdaki komutları çalıştırın:

```bash
# Temel veri bilimi kütüphaneleri
conda install numpy pandas matplotlib seaborn jupyter

# Makine öğrenmesi kütüphaneleri
conda install scikit-learn

# Metin madenciliği kütüphaneleri
pip install nltk
pip install spacy
python -m spacy download tr_core_news_sm

# Web scraping kütüphaneleri
pip install beautifulsoup4
pip install requests
pip install selenium

# Görselleştirme kütüphaneleri
pip install plotly
pip install wordcloud

# Veri tabanı kütüphaneleri
pip install sqlalchemy
pip install pymongo

# Diğer yardımcı kütüphaneler
pip install openpyxl
pip install xlrd
pip install missingno
pip install imbalanced-learn
```

### 3. Kurulumu Test Etme

Jupyter Notebook açın:
```bash
jupyter notebook
```

Yeni bir notebook oluşturun ve aşağıdaki kodu çalıştırın:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Seaborn version:", sns.__version__)
print("Scikit-learn version:", sklearn.__version__)

# Basit bir test
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
print("\nİris veri seti başarıyla yüklendi!")
print(df.head())
```

## R Kurulumu (Opsiyonel)

### 1. R İndirme ve Kurulum
- [R İndirme Sayfası](https://cran.r-project.org/)
- İşletim sisteminize uygun versiyonu indirin ve kurun

### 2. RStudio Kurulumu
- [RStudio İndirme Sayfası](https://posit.co/download/rstudio-desktop/)
- RStudio Desktop (ücretsiz) versiyonunu indirin ve kurun

### 3. Gerekli R Paketlerini Yükleme

R console'da veya RStudio'da aşağıdaki komutları çalıştırın:

```R
# Temel paketler
install.packages("tidyverse")
install.packages("caret")

# Veri görselleştirme
install.packages("ggplot2")
install.packages("plotly")

# Makine öğrenmesi
install.packages("rpart")
install.packages("randomForest")
install.packages("e1071")
install.packages("class")

# Veri işleme
install.packages("dplyr")
install.packages("tidyr")
install.packages("data.table")

# Model değerlendirme
install.packages("pROC")
install.packages("ROCR")
```

## IDE Alternatifleri

### Visual Studio Code
- Python ve R için mükemmel destek
- [VS Code İndirme](https://code.visualstudio.com/)
- Python ve Jupyter eklentilerini yükleyin

### PyCharm
- Python için profesyonel IDE
- [PyCharm Community Edition (Ücretsiz)](https://www.jetbrains.com/pycharm/)

### Spyder
- Anaconda ile birlikte gelir
- MATLAB benzeri arayüz
- Başlatmak için terminal'de `spyder` yazın

## Git ve GitHub Kurulumu

### Git Kurulumu
- [Git İndirme](https://git-scm.com/downloads)
- İşletim sisteminize uygun versiyonu kurun

### GitHub Hesabı
- [GitHub](https://github.com) üzerinden ücretsiz hesap oluşturun
- Proje ve ödevlerinizi burada yönetebilirsiniz

### Git Yapılandırması
```bash
git config --global user.name "Adınız Soyadınız"
git config --global user.email "email@example.com"
```

## Büyük Veri Araçları (13. Hafta için)

### Apache Spark (Opsiyonel)
Daha sonra kurulacak, 13. hafta öncesinde detaylı talimatlar verilecektir.

## Sorun Giderme

### Yaygın Sorunlar

**Problem:** `conda` komutu bulunamıyor
**Çözüm:** Anaconda'yı PATH'e ekleyin veya Anaconda Prompt kullanın

**Problem:** Kütüphane import hatası
**Çözüm:** 
```bash
pip install --upgrade [kütüphane_adı]
# veya
conda install [kütüphane_adı]
```

**Problem:** Jupyter Notebook açılmıyor
**Çözüm:**
```bash
jupyter notebook --generate-config
# Tarayıcı ayarlarını kontrol edin
```

## Yardım ve Destek

- **Anaconda Dokümantasyonu:** https://docs.anaconda.com/
- **Python Resmi Dokümantasyonu:** https://docs.python.org/
- **Scikit-learn Dokümantasyonu:** https://scikit-learn.org/
- **Stack Overflow:** https://stackoverflow.com/

## Donanım Gereksinimleri

**Minimum:**
- İşlemci: Dual-core 2.0 GHz
- RAM: 4 GB
- Disk: 10 GB boş alan

**Önerilen:**
- İşlemci: Quad-core 2.5 GHz+
- RAM: 8 GB+
- Disk: 20 GB+ boş alan
- GPU: CUDA destekli (derin öğrenme için opsiyonel)

---

Kurulumla ilgili sorunlarınız için ders hocası veya asistanlarla iletişime geçebilirsiniz.
