# Hafta 1 - Ödev 2: Python Temel Alıştırmaları

## 📋 Ödev Açıklaması
Bu ödevde Python'un temel veri yapıları ve kontrol yapıları ile pratik yapacaksınız.

## 🎯 Öğrenme Hedefleri
- Python temel veri yapılarını kullanabilme
- Döngüler ve kontrol yapıları ile problem çözme
- Fonksiyon yazma becerisi kazanma
- Kod yazma pratiği yapma

## 💻 Alıştırmalar

### Alıştırma 1: Liste İşlemleri (10 puan)
Aşağıdaki işlemleri yapan Python kodu yazın:

```python
# Verilen liste
sayilar = [12, 45, 23, 67, 34, 89, 15, 56, 78, 90]

# Yapılacaklar:
# a) Listenin ortalamasını hesaplayın
# b) Çift sayıları yeni bir listeye aktarın
# c) 50'den büyük sayıları bulun
# d) Listeyi küçükten büyüğe sıralayın
# e) En büyük 3 sayıyı bulun
```

**Beklenen Çıktı:**
```
Ortalama: 50.9
Çift sayılar: [12, 34, 56, 78, 90]
50'den büyük: [67, 89, 56, 78, 90]
Sıralı liste: [12, 15, 23, 34, 45, 56, 67, 78, 89, 90]
En büyük 3: [90, 89, 78]
```

---

### Alıştırma 2: Sözlük İşlemleri (15 puan)
Bir öğrenci kayıt sistemi oluşturun:

```python
# 5 öğrencinin bilgilerini içeren bir sözlük listesi oluşturun
# Her öğrenci için: ad, numara, vize, final notları

# Yapılacaklar:
# a) Her öğrencinin genel ortalamasını hesaplayın (Vize %40, Final %60)
# b) En yüksek ortalamaya sahip öğrenciyi bulun
# c) Ortalaması 70'in üzerinde olan öğrencileri listeleyin
# d) Tüm öğrencilerin genel ortalamasını hesaplayın
```

**Örnek Veri Yapısı:**
```python
ogrenciler = [
    {"ad": "Ali Yılmaz", "no": "101", "vize": 75, "final": 80},
    {"ad": "Ayşe Demir", "no": "102", "vize": 85, "final": 90},
    # ...
]
```

---

### Alıştırma 3: String İşlemleri (10 puan)
Metin analizi yapın:

```python
metin = """
Veri madenciliği, büyük veri kümelerinden anlamlı bilgi ve 
kalıplar çıkarma sürecidir. Veri madenciliği teknikleri, 
işletmelerin veri odaklı kararlar almasına yardımcı olur.
"""

# Yapılacaklar:
# a) Toplam kelime sayısını bulun
# b) "veri" kelimesinin kaç kez geçtiğini bulun (büyük/küçük harf duyarsız)
# c) En uzun kelimeyi bulun
# d) Her kelimenin kaç kez geçtiğini gösteren sözlük oluşturun
# e) Cümle sayısını bulun
```

---

### Alıştırma 4: Fonksiyon Yazma (15 puan)
Aşağıdaki fonksiyonları yazın:

```python
def asal_mi(sayi):
    """
    Verilen sayının asal olup olmadığını kontrol eder
    Args:
        sayi (int): Kontrol edilecek sayı
    Returns:
        bool: Asal ise True, değilse False
    """
    # Kodunuzu buraya yazın
    pass

def fibonacci(n):
    """
    İlk n Fibonacci sayısını döndürür
    Args:
        n (int): Kaç tane Fibonacci sayısı
    Returns:
        list: Fibonacci sayıları listesi
    """
    # Kodunuzu buraya yazın
    pass

def faktoriyek(n):
    """
    n! (faktöriyel) hesaplar
    Args:
        n (int): Faktöriyeli alınacak sayı
    Returns:
        int: n!'in değeri
    """
    # Kodunuzu buraya yazın
    pass

def ebob(a, b):
    """
    İki sayının en büyük ortak bölenini bulur
    Args:
        a (int): İlk sayı
        b (int): İkinci sayı
    Returns:
        int: EBOB değeri
    """
    # Kodunuzu buraya yazın
    pass
```

**Test Kodları:**
```python
# Test edilecek
print(asal_mi(17))  # True
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(faktoriyel(5))  # 120
print(ebob(48, 18))  # 6
```

---

### Alıştırma 5: Veri Analizi (20 puan)
Bir sınıftaki öğrencilerin notlarını analiz edin:

```python
# Verilen veri
sinif_notlari = {
    "Matematik": [75, 82, 90, 68, 95, 78, 85, 72, 88, 91],
    "Fizik": [80, 75, 85, 70, 92, 76, 82, 74, 86, 89],
    "Kimya": [78, 85, 88, 72, 90, 80, 84, 76, 87, 93],
    "Biyoloji": [82, 78, 92, 75, 88, 79, 86, 73, 85, 90]
}

# Yapılacaklar:
# a) Her dersin ortalamasını hesaplayın
# b) En yüksek ve en düşük ortalamalı dersleri bulun
# c) Her öğrencinin (her dersin aynı indeksindeki öğrenci) 
#    genel ortalamasını hesaplayın
# d) Her derste kaç öğrenci 80'in üzerinde aldı?
# e) Tüm sınıfın genel ortalamasını hesaplayın
```

---

### Alıştırma 6: List Comprehension (10 puan)
List comprehension kullanarak aşağıdaki listeleri oluşturun:

```python
# a) 1'den 100'e kadar olan sayıların kareleri
kareler = # Kodunuz

# b) 1'den 50'ye kadar olan çift sayılar
cift_sayilar = # Kodunuz

# c) 1'den 100'e kadar 3'e veya 5'e bölünebilen sayılar
bolunebilen = # Kodunuz

# d) "Python" kelimesindeki sesli harfler
kelime = "Python"
sesli_harfler = # Kodunuz

# e) İki listenin kartezyen çarpımı
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
kartezyen = # Kodunuz  # [(1, 'a'), (1, 'b'), ...]
```

---

### Alıştırma 7: Nested (İç İçe) Yapılar (20 puan)
Bir şirketin departman ve çalışan bilgilerini yönetin:

```python
# Veri yapısı
sirket = {
    "IT": {
        "calisanlar": ["Ali", "Ayşe", "Mehmet"],
        "maaslar": [8000, 9000, 7500],
        "deneyim_yillari": [3, 5, 2]
    },
    "Pazarlama": {
        "calisanlar": ["Fatma", "Ahmet"],
        "maaslar": [7000, 7500],
        "deneyim_yillari": [4, 3]
    },
    "Muhasebe": {
        "calisanlar": ["Zeynep", "Can", "Elif"],
        "maaslar": [6500, 7000, 6800],
        "deneyim_yillari": [2, 4, 3]
    }
}

# Yapılacaklar:
# a) Toplam çalışan sayısını bulun
# b) En yüksek maaşlı çalışanı ve departmanını bulun
# c) Her departmanın ortalama maaşını hesaplayın
# d) En deneyimli çalışanı bulun
# e) Toplam maaş bütçesini hesaplayın
# f) Maaşı 7000'den fazla olan çalışanları listeleyin
```

---

## 📏 Teknik Gereksinimler

### Dosya Yapısı
Tüm alıştırmaları tek bir Python dosyasında çözün:
- **Dosya adı:** `AdSoyad_Odev2.py`
- Her alıştırma için açıklayıcı yorumlar ekleyin
- Çıktıları ekrana yazdırın

### Kod Standartları
- Anlamlı değişken isimleri kullanın
- Her fonksiyona docstring ekleyin
- Kodu düzenli ve okunabilir yazın
- PEP 8 standartlarına uygun yazın

## ✅ Değerlendirme Kriterleri

| Alıştırma | Puan | Değerlendirme |
|-----------|------|---------------|
| Alıştırma 1 | 10 | Liste işlemleri doğruluğu |
| Alıştırma 2 | 15 | Sözlük kullanımı ve hesaplamalar |
| Alıştırma 3 | 10 | String işlemleri |
| Alıştırma 4 | 15 | Fonksiyon yazma becerisi |
| Alıştırma 5 | 20 | Veri analizi mantığı |
| Alıştırma 6 | 10 | List comprehension kullanımı |
| Alıştırma 7 | 20 | İç içe veri yapıları |
| **Toplam** | **100** | |

## 📅 Teslim Tarihi
- **Son Tarih:** [Hafta 3 Çarşamba, 23:59]
- **Teslim Yöntemi:** [LMS üzerinden .py dosyası yükleme]

## 💡 İpuçları

1. **Her alıştırmayı adım adım çözün:** Karmaşık görünen problemleri küçük parçalara bölün
2. **Print ile test edin:** Her adımda sonuçları yazdırarak kontrol edin
3. **Built-in fonksiyonları kullanın:** `sum()`, `len()`, `max()`, `min()` gibi
4. **List comprehension tercih edin:** Daha kısa ve Pythonic kod
5. **Hata mesajlarını okuyun:** Hata mesajları size ipucu verir

## 📚 Yardımcı Kaynaklar

- Python resmi dokümantasyonu: https://docs.python.org/3/
- W3Schools Python Tutorial: https://www.w3schools.com/python/
- Real Python: https://realpython.com/

## ❓ Örnek Çözüm (Alıştırma 1)

```python
# Alıştırma 1: Liste İşlemleri

sayilar = [12, 45, 23, 67, 34, 89, 15, 56, 78, 90]

# a) Ortalama
ortalama = sum(sayilar) / len(sayilar)
print(f"Ortalama: {ortalama}")

# b) Çift sayılar
cift_sayilar = [x for x in sayilar if x % 2 == 0]
print(f"Çift sayılar: {cift_sayilar}")

# c) 50'den büyük
buyuk_sayilar = [x for x in sayilar if x > 50]
print(f"50'den büyük: {buyuk_sayilar}")

# d) Sıralama
sirali = sorted(sayilar)
print(f"Sıralı liste: {sirali}")

# e) En büyük 3
en_buyuk_3 = sorted(sayilar, reverse=True)[:3]
print(f"En büyük 3: {en_buyuk_3}")
```

---

**Başarılar!** 🐍
