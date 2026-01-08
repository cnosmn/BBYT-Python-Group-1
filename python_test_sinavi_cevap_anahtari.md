# PYTHON PROGRAMLAMA DİLİ TEST SINAVI - CEVAP ANAHTARI

---

## BÖLÜM 1: ÇOKTAN SEÇMELİ SORULAR CEVAPLARI

1. **A)** type()
2. **C)** sayi_2
3. **C)** append()
4. **B)** [2, 3, 4]
5. **B)** Tuple değiştirilemez, liste değiştirilebilir
6. **B)** Sırasızdır ve tekrar eden eleman içeremez
7. **B)** sozluk.get("anahtar")
8. **A)** Doğru
9. **B)** 1, 3, 5, 7, 9
10. **B)** 15
11. **A)** return
12. **B)** Sınırsız sayıda pozisyonel argüman alır
13. **B)** Kendini çağıran fonksiyon
14. **A)** __init__()
15. **A)** Ahmet
16. **B)** __ (çift alt çizgi)
17. **A)** Verilerin ve fonksiyonların bir arada tutulması
18. **D)** len()
19. **C)** Bulunamadı
20. **A)** Yerel bir değişkeni global yapar

---

## BÖLÜM 2: BOŞLUK DOLDURMA SORULARI CEVAPLARI

1. **#** (diyez işareti)
2. **float**
3. **insert**
4. **parantez** veya **( )** veya **()**
5. **remove**, **discard**
6. **keys**
7. **==**
8. **and**
9. **1**, **10**
10. **break**
11. **continue**
12. **def**
13. **anahtar=değer** veya **key=value**
14. **recursion** veya **özyineleme**
15. **class**
16. **__init__**
17. **__init__**
18. **getter**, **setter**
19. **attribute** veya **özellik**
20. **pop**

---

## BÖLÜM 3: DOĞRU/YANLIŞ SORULARI CEVAPLARI

1. **Y** (Yanlış - değişken isimleri sayı ile başlayamaz)
2. **D** (Doğru)
3. **D** (Doğru)
4. **Y** (Yanlış - set içinde aynı eleman birden fazla kez bulunamaz)
5. **D** (Doğru)
6. **D** (Doğru)
7. **Y** (Yanlış - for döngüsü listeler, stringler vb. ile de çalışır)
8. **D** (Doğru)
9. **D** (Doğru)
10. **Y** (Yanlış - continue bir sonraki iterasyona geçer, döngüyü sonlandırmaz)
11. **Y** (Yanlış - fonksiyonlar parametre almayabilir)
12. **Y** (Yanlış - fonksiyonlar değer döndürmeyebilir)
13. **D** (Doğru)
14. **D** (Doğru)
15. **D** (Doğru)
16. **D** (Doğru)
17. **Y** (Yanlış - __init__ metodu nesne oluşturulurken çağrılır, sınıf tanımlanırken değil)
18. **Y** (Yanlış - private attribute'lere doğrudan erişilemez, getter/setter kullanılmalı)
19. **D** (Doğru)
20. **D** (Doğru)

---

## BÖLÜM 4: KOD TAMAMLAMA SORULARI CEVAPLARI

**1.**
```python
def toplam_bul(n):
    toplam = 0
    for i in range(1, n + 1):  # n + 1
        toplam = toplam + i    # toplam + i
    return toplam              # toplam
```

**2.**
```python
def en_buyuk_bul(liste):
    en_buyuk = liste[0]
    for eleman in liste:
        if eleman > en_buyuk:  # en_buyuk
            en_buyuk = eleman  # eleman
    return en_buyuk            # en_buyuk
```

**3.**
```python
def cift_mi_tek_mi(sayi):
    if sayi % 2 == 0:  # 0
        return "Çift"
    else:
        return "Tek"
```

**4.**
```python
cift_sayilar = []
for sayi in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if sayi % 2 == 0:              # 0
        cift_sayilar.append(sayi)   # cift_sayilar
print(cift_sayilar)
```

**5.**
```python
sozluk = {"a": 10, "b": 20, "c": 30}
toplam = 0
for deger in sozluk.values():  # values
    toplam += deger            # deger
print(toplam)
```

**6.**
```python
def uzunluk_bul(metin):
    sayac = 0
    for karakter in metin:  # metin
        sayac += 1          # 1
    return sayac            # sayac
```

**7.**
```python
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1           # 1
    else:
        return n * faktoriyel(n - 1)  # n - 1
```

**8.**
```python
class Ogrenci:
    def __init__(self, isim, numara):  # __init__
        self.isim = isim               # isim
        self.numara = numara           # numara

ogrenci1 = Ogrenci("Ahmet", 123)
print(ogrenci1.isim)
```

**9.**
```python
def ters_cevir(liste):
    ters_liste = []
    for i in range(len(liste) - 1, -1, -1):  # -1
        ters_liste.append(liste[i])          # i
    return ters_liste
```

**10.**
```python
sayac = 1
while sayac <= 10:  # 10
    print(sayac)
    sayac += 1      # 1
```

**11.**
```python
def topla(*args):
    toplam = 0
    for sayi in args:    # args
        toplam += sayi   # sayi
    return toplam

print(topla(1, 2, 3, 4, 5))
```

**12.**
```python
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def bilgi_yazdir(self):
        print("Marka:", self.marka, "Model:", self.model)  # marka, model

araba1 = Araba("Toyota", "Corolla")
araba1.bilgi_yazdir()
```

**13.**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
birlesim = set1.union(set2)  # union
print(birlesim)
```

**14.**
```python
liste = [1, 2, 3, 2, 4, 2, 5]
sayac = liste.count(2)  # count
print(sayac)
```

**15.**
```python
sozluk = {"a": 1, "b": 2}
sozluk.update({"c": 3})  # update
print(sozluk)
```

**16.**
```python
def fibonacci(n):
    if n <= 1:
        return n              # n
    elif n == 2:
        return 1              # 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # n - 2
```

**17.**
```python
class Insan:
    def __init__(self, isim):
        self.__isim = isim      # __
    
    def get_isim(self):
        return self.__isim      # __

insan1 = Insan("Mehmet")
print(insan1.get_isim())
```

**18.**
```python
for i in range(1, 11):        # 11
    for j in range(1, 11):    # 11
        print(i, "x", j, "=", i * j)  # j
```

**19.**
```python
sayi = 10

def artir():
    global sayi  # global
    sayi += 5

artir()
print(sayi)
```

**20.**
```python
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:    # 0
            return False     # False
    return True              # True
```

---

## PUANLAMA KRİTERLERİ

### Bölüm 1: Çoktan Seçmeli (40 puan)
- Her doğru cevap: 2 puan
- Her yanlış cevap: 0 puan

### Bölüm 2: Boşluk Doldurma (40 puan)
- Her doğru cevap: 2 puan
- Kısmen doğru cevaplar: Öğretmenin takdirine göre 1 puan
- Yanlış cevap: 0 puan

### Bölüm 3: Doğru/Yanlış (20 puan)
- Her doğru cevap: 1 puan
- Her yanlış cevap: 0 puan

### Bölüm 4: Kod Tamamlama (60 puan)
- Her soru için:
  - Tam doğru: 3 puan
  - Kısmen doğru: 1-2 puan (öğretmenin takdirine göre)
  - Yanlış/Boş: 0 puan

**TOPLAM: 160 puan**

---

## NOTLANDIRMA ÖNERİSİ

- **140-160 puan:** Çok İyi (5)
- **120-139 puan:** İyi (4)
- **100-119 puan:** Orta (3)
- **80-99 puan:** Geçer (2)
- **0-79 puan:** Başarısız (1)

---

## AÇIKLAMALAR

### Önemli Notlar:
1. Kod tamamlama sorularında öğrencilerin yazdığı kodların çalışır durumda olması önemlidir.
2. Boşluk doldurma sorularında eş anlamlı veya kabul edilebilir alternatif cevaplar değerlendirilebilir.
3. Doğru/Yanlış sorularında öğrencilerin neden yanlış olduğunu açıklayabilmeleri ek puan olarak değerlendirilebilir.
4. Kod tamamlama sorularında öğrencilerin kod yazım stili ve Python best practices'e uygunluğu göz önünde bulundurulabilir.

### Öğrencilere Öneriler:
- Kod tamamlama sorularında boşlukları doldururken Python sözdizimine dikkat edin.
- Değişken isimlendirmelerinde tutarlı olun.
- Kodun çalışır durumda olduğundan emin olun.
- Zamanınızı iyi yönetin, her soruya yeterince zaman ayırın.

