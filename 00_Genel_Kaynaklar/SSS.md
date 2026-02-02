# Veri Madenciliği Sıkça Sorulan Sorular (SSS)

## 📚 Genel Ders Soruları

### Ders Hakkında

**S: Bu ders için ön koşul var mı?**
C: Temel programlama bilgisi (Python tercih edilir) ve temel istatistik bilgisi yeterlidir. İleri düzey matematik gerekmez.

**S: Python mi R mı öğrenmeliyim?**
C: Python öneririz. Daha genel amaçlı, endüstride yaygın kullanılır ve daha fazla kaynak bulunur.

**S: Dersi geçmek için minimum not nedir?**
C: 60/100 genel ortalama ile dersi geçebilirsiniz.

**S: Devamsızlık sınırı nedir?**
C: %30 devamsızlık yapmış öğrenciler sınava giremez (14 haftanın 4'ünden fazla).

### Değerlendirme

**S: Vize ve final sınav formatı nasıl?**
C: 
- Vize: Çoktan seçmeli + açık uçlu sorular (7. hafta)
- Final: Kapsamlı yazılı sınav + proje sunumu (14. hafta)

**S: Ödevler zorunlu mu?**
C: Evet, ödevler toplam notun %20'sini oluşturur ve teslim edilmesi zorunludur.

**S: Grup projesinde bireysel değerlendirme var mı?**
C: Evet, grup notu + bireysel katkı değerlendirmesi yapılır.

---

## 💻 Teknik Sorular

### Kurulum ve Ortam

**S: Anaconda kurulumu zorunlu mu?**
C: Hayır, ancak şiddetle tavsiye edilir. Alternatif olarak pip ile kütüphaneler kurabilirsiniz.

**S: Jupyter Notebook çalışmıyor, ne yapmalıyım?**
C:
```bash
# Terminalde şunları deneyin:
jupyter notebook --generate-config
# Tarayıcı ayarlarınızı kontrol edin
# Anaconda Prompt'tan çalıştırmayı deneyin
```

**S: Mac/Linux kullanıyorum, farklılık var mı?**
C: Hayır, Python platform bağımsızdır. Bazı komutlar terminal/command prompt'ta farklı olabilir.

### Python ve Kütüphaneler

**S: Pandas ile NumPy arasındaki fark nedir?**
C:
- **NumPy:** Sayısal hesaplamalar, diziler (arrays)
- **Pandas:** Veri manipülasyonu, DataFrame yapısı, daha kullanıcı dostu

**S: Scikit-learn versiyonu önemli mi?**
C: Evet, bazı fonksiyonlar versiyonlar arası değişebilir. 1.0+ versiyonunu kullanmanızı öneririz.

**S: GPU gerekli mi?**
C: Hayır, derste işlenen konular için CPU yeterlidir. Derin öğrenme için GPU faydalı olabilir.

---

## 📊 Veri Madenciliği Kavramları

### Genel Kavramlar

**S: Veri madenciliği ile makine öğrenmesi arasındaki fark nedir?**
C:
- **Veri Madenciliği:** Daha geniş kavram, veri keşfi, temizleme, görselleştirme, analiz
- **Makine Öğrenmesi:** Veri madenciliğinin bir alt kümesi, model oluşturma ve tahmin

**S: Supervised vs Unsupervised learning farkı?**
C:
- **Supervised:** Etiketli veri ile öğrenme (sınıflandırma, regresyon)
- **Unsupervised:** Etiketsiz veri (kümeleme, boyut indirgeme)

**S: Sınıflandırma ile kümeleme arasındaki fark?**
C:
- **Sınıflandırma:** Önceden tanımlı sınıflara atama (supervised)
- **Kümeleme:** Benzer verileri gruplama (unsupervised)

### Algoritmalar

**S: Hangi algoritmayı ne zaman kullanmalıyım?**
C:
- **Karar Ağaçları:** Yorumlanabilirlik önemli, kategorik + sayısal veri
- **k-NN:** Basit problemler, küçük-orta veri setleri
- **SVM:** Yüksek boyutlu veri, ikili sınıflandırma
- **Random Forest:** Genel amaçlı, robust
- **Naïve Bayes:** Metin sınıflandırma, hız önemli

**S: En iyi algoritma hangisi?**
C: "No Free Lunch Theorem" - Her problem için en iyi algoritma yoktur. Veri setinize göre deneyerek bulmalısınız.

**S: Karar ağacı neden overfit oluyor?**
C: Ağaç çok derinleşirse eğitim verisini ezberler. Çözüm: max_depth, min_samples_split gibi parametrelerle sınırlayın veya pruning yapın.

### Veri Ön İşleme

**S: Eksik değerleri silmeli mi doldurmalı mıyım?**
C:
- < %5 eksik: Silebilirsiniz
- %5-20: Doldurma düşünün (ortalama, medyan, mod)
- > %20: Dikkatli olun, özniteliği kaldırabilirsiniz

**S: Normalizasyon her zaman gerekli mi?**
C:
Gerekli:
- KNN, SVM, Neural Networks
- Gradient descent kullanan algoritmalar

Gereksiz:
- Karar ağaçları
- Random Forest
- Naive Bayes

**S: One-hot encoding ne zaman kullanılır?**
C: Nominal (sırasız) kategorik değişkenler için. Örnek: Renk (kırmızı, mavi, yeşil).
Ordinal (sıralı) değişkenler için label encoding yeterli. Örnek: Eğitim (lise, lisans, yüksek lisans).

### Model Değerlendirme

**S: Accuracy yeterli bir metrik mi?**
C: Hayır, özellikle dengesiz veri setlerinde yanıltıcı olabilir. Precision, Recall, F1-Score da bakın.

**S: Overfitting nasıl tespit edilir?**
C:
- Eğitim skoru yüksek, test skoru düşük
- Cross-validation skoru test skorundan çok farklı
- Validation curve grafiğinde büyük fark

**S: Train-test split oranı ne olmalı?**
C:
- Genel: 80-20 veya 70-30
- Küçük veri (<1000): 60-40 veya cross-validation
- Büyük veri (>100K): 90-10 bile olabilir

**S: K-fold cross-validation'da K kaç olmalı?**
C:
- Genelde K=5 veya K=10
- Küçük veri setlerinde K=n (Leave-One-Out)
- Hesaplama maliyeti yüksekse K=3

---

## 🔧 Pratik Problemler ve Çözümler

### Hata Mesajları

**S: "ModuleNotFoundError: No module named 'sklearn'"**
C:
```bash
pip install scikit-learn
# veya
conda install scikit-learn
```

**S: "ValueError: could not convert string to float"**
C: Kategorik verileri encode etmelisiniz:
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['column'] = le.fit_transform(df['column'])
```

**S: "MemoryError" hatası alıyorum**
C:
- Veri setini parçalara bölün
- Chunk processing kullanın
- Gereksiz sütunları silin
- Daha küçük veri tipi kullanın (float32 yerine float16)

### Performans Sorunları

**S: Modelim çok yavaş çalışıyor**
C:
- Veri setini küçültün (sampling)
- PCA ile boyut indirgeme yapın
- Daha basit algoritma deneyin
- Hiperparametre sayısını azaltın
- Paralel işleme kullanın (n_jobs=-1)

**S: Cross-validation çok uzun sürüyor**
C:
- K değerini azaltın (10 yerine 5)
- Daha az parametre kombinasyonu deneyin
- RandomizedSearchCV kullanın (GridSearchCV yerine)

---

## 📖 Öğrenme Stratejileri

**S: Matematiği anlamadan veri madenciliği öğrenebilir miyim?**
C: Evet, başlangıç seviyesinde. Ancak ileri seviyede matematik bilgisi faydalıdır. Önce pratik yapın, sonra teoriye girin.

**S: En iyi öğrenme kaynağı nedir?**
C:
1. Hands-on practice (en önemli)
2. Kaggle competitions
3. Online kurslar (Coursera, edX)
4. Kitaplar (Python Machine Learning)
5. Araştırma makaleleri (ileri seviye)

**S: Kaggle'a nasıl başlamalıyım?**
C:
1. Titanic competition ile başlayın (başlangıç)
2. Başkaların notebook'larını inceleyin
3. Kendi çözümünüzü geliştirin
4. Topluluğa katılın, sorular sorun

**S: Günde kaç saat çalışmalıyım?**
C:
- Minimum: 2 saat (ders + lab)
- Önerilen: 3-4 saat
- Hafta sonu: Projelere odaklanın

---

## 🎓 Kariyer ve Gelecek

**S: Veri bilimci olmak için başka ne öğrenmeliyim?**
C:
- SQL ve veritabanları
- İleri Python (OOP, decorators)
- Git/GitHub
- Derin öğrenme (TensorFlow/PyTorch)
- Cloud platformları (AWS, Azure, GCP)
- İş bilgisi (domain knowledge)

**S: Hangi sektörlerde iş imkanı var?**
C:
- Fintech ve bankacılık
- E-ticaret
- Sağlık
- Telekomünikasyon
- Otomotiv
- Perakende
- Sosyal medya ve reklam

**S: Staj nasıl bulabilirim?**
C:
- Kaggle profili oluşturun
- GitHub'da projelerinizi paylaşın
- LinkedIn'de aktif olun
- Şirketlere direkt başvurun
- Üniversite kariyer fuarlarına katılın

---

## 🆘 Yardım ve Destek

**S: Takıldığım bir konu olursa nereye sorabilirim?**
C:
1. Ders forumu/LMS
2. Ofis saatleri (Pazartesi-Çarşamba 14:00-16:00)
3. E-posta: [ders_hocasi@uni.edu.tr]
4. Stack Overflow (genel Python soruları)
5. Kaggle forums

**S: Proje için grup bulamıyorum**
C: Ders forumunda "Grup arıyorum" başlığı açın veya ofis saatlerinde bildirin, yardımcı oluruz.

**S: Sınav soruları nereden çıkıyor?**
C:
- Ders notları (%50)
- Lab uygulamaları (%30)
- Ödevler (%20)

---

## 💡 İpuçları ve Püf Noktalar

**S: Hızlı öğrenmenin sırrı nedir?**
C:
1. Her gün kod yazın (consistency)
2. Hatalardan öğrenin (debug etmeyi öğrenin)
3. Başkalarının kodunu okuyun
4. Projeler yapın (teori değil pratik)
5. Toplulukta aktif olun

**S: En çok yapılan hatalar nelerdir?**
C:
1. Data leakage (test verisini eğitimde kullanma)
2. Overfit etmeyi fark etmeme
3. Cross-validation yapmama
4. Ölçeklendirmeyi unutma
5. Baseline model yapmama
6. Sonuçları yorumlamama

**S: Kod yazarken nelere dikkat etmeliyim?**
C:
- Anlamlı değişken isimleri
- Yorumlar ekleyin
- Fonksiyonlara bölen (modüler kod)
- Version control kullanın (Git)
- Notebook'ları düzenli tutun

---

## 📧 İletişim

Başka sorularınız için:
- **E-posta:** [ders_hocasi@universite.edu.tr]
- **Forum:** [LMS linki]
- **Ofis Saatleri:** Pazartesi ve Çarşamba, 14:00-16:00

**Son Güncelleme:** Şubat 2026
