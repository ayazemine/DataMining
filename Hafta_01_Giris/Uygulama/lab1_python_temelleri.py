"""
Hafta 1 - Lab 1: Python Kurulumu ve Temel Veri Yapıları
Veri Madenciliği Dersi
"""

# ============================================================================
# 1. PYTHON TEMELLERİ
# ============================================================================

print("=" * 50)
print("Python'a Hoş Geldiniz!")
print("=" * 50)

# Python versiyonunu kontrol edelim
import sys
print(f"\nPython Versiyonu: {sys.version}")

# ============================================================================
# 2. DEĞİŞKENLER VE VERİ TİPLERİ
# ============================================================================

print("\n" + "=" * 50)
print("VERİ TİPLERİ")
print("=" * 50)

# Sayısal tipler
sayi_int = 42
sayi_float = 3.14
sayi_complex = 2 + 3j

print(f"\nInteger: {sayi_int}, Tip: {type(sayi_int)}")
print(f"Float: {sayi_float}, Tip: {type(sayi_float)}")
print(f"Complex: {sayi_complex}, Tip: {type(sayi_complex)}")

# String (Metin)
isim = "Veri Madenciliği"
print(f"\nString: {isim}, Tip: {type(isim)}")
print(f"Uzunluk: {len(isim)}")
print(f"Büyük harf: {isim.upper()}")
print(f"Küçük harf: {isim.lower()}")

# Boolean
dogru = True
yanlis = False
print(f"\nBoolean: {dogru}, Tip: {type(dogru)}")

# ============================================================================
# 3. LİSTELER (LISTS)
# ============================================================================

print("\n" + "=" * 50)
print("LİSTELER")
print("=" * 50)

# Liste oluşturma
notlar = [85, 90, 78, 92, 88]
isimler = ["Ali", "Ayşe", "Mehmet", "Fatma"]
karisik = [1, "iki", 3.0, True, [5, 6]]

print(f"\nNotlar: {notlar}")
print(f"İsimler: {isimler}")
print(f"Karışık liste: {karisik}")

# Liste işlemleri
print(f"\nİlk not: {notlar[0]}")
print(f"Son not: {notlar[-1]}")
print(f"İlk üç not: {notlar[:3]}")

# Eleman ekleme
notlar.append(95)
print(f"Not eklendikten sonra: {notlar}")

# Liste istatistikleri
print(f"\nOrtalama not: {sum(notlar) / len(notlar):.2f}")
print(f"En yüksek not: {max(notlar)}")
print(f"En düşük not: {min(notlar)}")
print(f"Not sayısı: {len(notlar)}")

# ============================================================================
# 4. TUPLE (DEĞİŞTİRİLEMEZ LİSTELER)
# ============================================================================

print("\n" + "=" * 50)
print("TUPLE")
print("=" * 50)

koordinat = (10, 20)
renkler = ("kırmızı", "yeşil", "mavi")

print(f"\nKoordinat: {koordinat}")
print(f"X: {koordinat[0]}, Y: {koordinat[1]}")
print(f"Renkler: {renkler}")

# ============================================================================
# 5. SÖZLÜKLER (DICTIONARIES)
# ============================================================================

print("\n" + "=" * 50)
print("SÖZLÜKLER")
print("=" * 50)

# Öğrenci bilgileri
ogrenci = {
    "ad": "Ali Yılmaz",
    "no": "12345",
    "bolum": "Bilgisayar Mühendisliği",
    "notlar": [85, 90, 78, 92]
}

print(f"\nÖğrenci: {ogrenci}")
print(f"Ad: {ogrenci['ad']}")
print(f"Notlar: {ogrenci['notlar']}")
print(f"Ortalama: {sum(ogrenci['notlar']) / len(ogrenci['notlar']):.2f}")

# Yeni anahtar ekleme
ogrenci["email"] = "ali.yilmaz@uni.edu"
print(f"\nGüncellenmiş öğrenci: {ogrenci}")

# Tüm anahtarları görme
print(f"\nAnahtarlar: {ogrenci.keys()}")
print(f"Değerler: {ogrenci.values()}")

# ============================================================================
# 6. KÜMELER (SETS)
# ============================================================================

print("\n" + "=" * 50)
print("KÜMELER")
print("=" * 50)

sayilar_1 = {1, 2, 3, 4, 5}
sayilar_2 = {4, 5, 6, 7, 8}

print(f"\nKüme 1: {sayilar_1}")
print(f"Küme 2: {sayilar_2}")
print(f"Birleşim: {sayilar_1 | sayilar_2}")
print(f"Kesişim: {sayilar_1 & sayilar_2}")
print(f"Fark: {sayilar_1 - sayilar_2}")

# ============================================================================
# 7. KONTROL YAPILARI
# ============================================================================

print("\n" + "=" * 50)
print("KONTROL YAPILARI")
print("=" * 50)

# if-elif-else
not_ortalama = 75

if not_ortalama >= 85:
    harf_notu = "AA"
elif not_ortalama >= 70:
    harf_notu = "BA"
elif not_ortalama >= 60:
    harf_notu = "BB"
else:
    harf_notu = "CC"

print(f"\nOrtalama: {not_ortalama}, Harf Notu: {harf_notu}")

# ============================================================================
# 8. DÖNGÜLER
# ============================================================================

print("\n" + "=" * 50)
print("DÖNGÜLER")
print("=" * 50)

# for döngüsü
print("\nÖğrenci notları:")
notlar = [85, 90, 78, 92, 88]
for i, not_degeri in enumerate(notlar, 1):
    print(f"Öğrenci {i}: {not_degeri}")

# while döngüsü
print("\n1'den 5'e kadar sayılar:")
sayac = 1
while sayac <= 5:
    print(sayac, end=" ")
    sayac += 1
print()

# ============================================================================
# 9. LİST COMPREHENSION
# ============================================================================

print("\n" + "=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# Kareleri alma
sayilar = [1, 2, 3, 4, 5]
kareler = [x**2 for x in sayilar]
print(f"\nSayılar: {sayilar}")
print(f"Kareler: {kareler}")

# Çift sayıları filtreleme
cift_sayilar = [x for x in range(1, 11) if x % 2 == 0]
print(f"Çift sayılar: {cift_sayilar}")

# ============================================================================
# 10. FONKSİYONLAR
# ============================================================================

print("\n" + "=" * 50)
print("FONKSİYONLAR")
print("=" * 50)

def ortalama_hesapla(notlar):
    """Notların ortalamasını hesaplar"""
    return sum(notlar) / len(notlar)

def harf_notu_bul(ortalama):
    """Ortalamaya göre harf notu döndürür"""
    if ortalama >= 85:
        return "AA"
    elif ortalama >= 70:
        return "BA"
    elif ortalama >= 60:
        return "BB"
    else:
        return "CC"

# Fonksiyonları kullanma
ogrenci_notlari = [85, 90, 78, 92, 88]
ort = ortalama_hesapla(ogrenci_notlari)
harf = harf_notu_bul(ort)

print(f"\nNotlar: {ogrenci_notlari}")
print(f"Ortalama: {ort:.2f}")
print(f"Harf Notu: {harf}")

# ============================================================================
# 11. VERİ BİLİMİ KÜTÜPHANELERİ - İLK BAKIŞ
# ============================================================================

print("\n" + "=" * 50)
print("VERİ BİLİMİ KÜTÜPHANELERİ")
print("=" * 50)

# NumPy - Sayısal hesaplamalar
import numpy as np

dizi = np.array([1, 2, 3, 4, 5])
print(f"\nNumPy dizisi: {dizi}")
print(f"Ortalama: {np.mean(dizi)}")
print(f"Standart sapma: {np.std(dizi)}")
print(f"Kare alma: {dizi ** 2}")

# Pandas - Veri analizi (önizleme)
import pandas as pd

veri = {
    'İsim': ['Ali', 'Ayşe', 'Mehmet', 'Fatma'],
    'Yaş': [22, 23, 21, 24],
    'Not': [85, 90, 78, 92]
}

df = pd.DataFrame(veri)
print("\nPandas DataFrame:")
print(df)
print(f"\nOrtalama not: {df['Not'].mean():.2f}")

# ============================================================================
# ALIŞTIRMALAR
# ============================================================================

print("\n" + "=" * 50)
print("ALIŞTIRMALAR")
print("=" * 50)

print("""
1. [1, 2, 3, 4, 5] listesinin çift sayılarını bulun
2. Bir sözlük oluşturun: 3 öğrencinin ad ve notlarını içersin
3. 1'den 100'e kadar olan sayıların toplamını hesaplayan bir fonksiyon yazın
4. Bir listedeki en büyük ve en küçük sayıyı bulan fonksiyon yazın
5. Verilen bir metnin kelime sayısını bulan fonksiyon yazın
""")

# Örnek çözümler
print("\nÖrnek Çözümler:\n")

# 1. Çift sayıları bulma
sayilar = [1, 2, 3, 4, 5]
ciftler = [x for x in sayilar if x % 2 == 0]
print(f"1. Çift sayılar: {ciftler}")

# 2. Öğrenci sözlüğü
ogrenciler = {
    'Ali': 85,
    'Ayşe': 90,
    'Mehmet': 78
}
print(f"2. Öğrenciler: {ogrenciler}")

# 3. Toplam hesaplama
def toplam_hesapla(n):
    return sum(range(1, n + 1))

print(f"3. 1'den 100'e toplam: {toplam_hesapla(100)}")

# 4. Min-max bulma
def min_max_bul(liste):
    return min(liste), max(liste)

sayilar = [5, 2, 9, 1, 7]
minimum, maksimum = min_max_bul(sayilar)
print(f"4. Min: {minimum}, Max: {maksimum}")

# 5. Kelime sayısı
def kelime_say(metin):
    return len(metin.split())

metin = "Veri madenciliği çok ilginç bir alan"
print(f"5. Kelime sayısı: {kelime_say(metin)}")

print("\n" + "=" * 50)
print("Lab 1 Tamamlandı!")
print("=" * 50)
