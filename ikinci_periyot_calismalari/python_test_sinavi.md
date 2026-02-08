# PYTHON PROGRAMLAMA DİLİ TEST SINAVI

**Öğrenci Adı Soyadı:** ___________________________  
**Tarih:** ___________________________  
**Süre:** 90 dakika

---

## BÖLÜM 1: ÇOKTAN SEÇMELİ SORULAR (20 Soru - Her biri 2 puan)

**1.** Python'da bir değişkenin veri tipini öğrenmek için hangi fonksiyon kullanılır?
- A) type()
- B) typeof()
- C) datatype()
- D) gettype()

**2.** Aşağıdakilerden hangisi Python'da geçerli bir değişken ismidir?
- A) 2sayi
- B) sayi-2
- C) sayi_2
- D) sayi 2

**3.** Bir listenin sonuna eleman eklemek için hangi metod kullanılır?
- A) add()
- B) insert()
- C) append()
- D) extend()

**4.** Aşağıdaki kodun çıktısı nedir?
```python
liste = [1, 2, 3, 4, 5]
print(liste[1:4])
```
- A) [1, 2, 3]
- B) [2, 3, 4]
- C) [1, 2, 3, 4]
- D) [2, 3, 4, 5]

**5.** Tuple (demet) ile liste arasındaki temel fark nedir?
- A) Tuple sıralıdır, liste sırasızdır
- B) Tuple değiştirilemez, liste değiştirilebilir
- C) Tuple sadece sayı içerir, liste her şeyi içerir
- D) Fark yoktur, aynı şeydir

**6.** Set (küme) veri yapısının özelliklerinden hangisi doğrudur?
- A) Sıralıdır ve tekrar eden eleman içerebilir
- B) Sırasızdır ve tekrar eden eleman içeremez
- C) Sıralıdır ve tekrar eden eleman içeremez
- D) Sırasızdır ve tekrar eden eleman içerebilir

**7.** Sözlük (dictionary) içinde bir anahtarın değerine erişmek için hangi yöntem hata vermez?
- A) sozluk["anahtar"]
- B) sozluk.get("anahtar")
- C) Her ikisi de hata vermez
- D) Her ikisi de hata verir

**8.** Aşağıdaki kodun çıktısı nedir?
```python
sayi = 10
if sayi > 5 and sayi < 15:
    print("Doğru")
else:
    print("Yanlış")
```
- A) Doğru
- B) Yanlış
- C) Hata verir
- D) Hiçbir şey yazdırmaz

**9.** `range(1, 10, 2)` fonksiyonu hangi sayıları üretir?
- A) 1, 2, 3, 4, 5, 6, 7, 8, 9
- B) 1, 3, 5, 7, 9
- C) 2, 4, 6, 8, 10
- D) 1, 3, 5, 7, 9, 11

**10.** Aşağıdaki kodun çıktısı nedir?
```python
toplam = 0
for i in range(1, 6):
    toplam += i
print(toplam)
```
- A) 10
- B) 15
- C) 20
- D) 25

**11.** Bir fonksiyondan değer döndürmek için hangi anahtar kelime kullanılır?
- A) return
- B) break
- C) continue
- D) yield

**12.** `*args` parametresi ne işe yarar?
- A) Sınırsız sayıda anahtar-değer çifti alır
- B) Sınırsız sayıda pozisyonel argüman alır
- C) Sadece bir argüman alır
- D) Hiçbir argüman almaz

**13.** Recursive (özyinelemeli) fonksiyon nedir?
- A) Kendini çağırmayan fonksiyon
- B) Kendini çağıran fonksiyon
- C) Parametre almayan fonksiyon
- D) Değer döndürmeyen fonksiyon

**14.** Bir sınıftan nesne oluşturmak için hangi metod otomatik olarak çağrılır?
- A) __init__()
- B) __new__()
- C) __create__()
- D) __start__()

**15.** Aşağıdaki kodun çıktısı nedir?
```python
class Ogrenci:
    def __init__(self, isim):
        self.isim = isim

ogrenci1 = Ogrenci("Ahmet")
print(ogrenci1.isim)
```
- A) Ahmet
- B) isim
- C) ogrenci1
- D) Hata verir

**16.** Private (özel) bir attribute oluşturmak için hangi ön ek kullanılır?
- A) #
- B) __ (çift alt çizgi)
- C) _ (tek alt çizgi)
- D) private

**17.** Encapsulation (kapsülleme) nedir?
- A) Verilerin ve fonksiyonların bir arada tutulması
- B) Bir sınıfın başka bir sınıftan türetilmesi
- C) Aynı isimde farklı fonksiyonlar yazılması
- D) Sınıfların soyutlanması

**18.** Bir listenin eleman sayısını öğrenmek için hangi fonksiyon kullanılır?
- A) count()
- B) size()
- C) length()
- D) len()

**19.** Aşağıdaki kodun çıktısı nedir?
```python
sozluk = {"a": 1, "b": 2, "c": 3}
print(sozluk.get("d", "Bulunamadı"))
```
- A) 4
- B) None
- C) Bulunamadı
- D) Hata verir

**20.** `global` anahtar kelimesi ne işe yarar?
- A) Yerel bir değişkeni global yapar
- B) Global bir değişkeni yerel yapar
- C) Değişkeni siler
- D) Değişkenin tipini değiştirir

---

## BÖLÜM 2: BOŞLUK DOLDURMA SORULARI (20 Soru - Her biri 2 puan)

**1.** Python'da yorum satırı oluşturmak için `_____` sembolü kullanılır.

**2.** `_____` veri tipi ondalıklı sayıları temsil eder.

**3.** Bir listenin belirli bir index'ine eleman eklemek için `_____()` metodu kullanılır.

**4.** Tuple (demet) oluşturmak için elemanlar `_____` içine alınır.

**5.** Set (küme) içinden bir elemanı silmek için `_____()` veya `_____()` metodu kullanılır.

**6.** Sözlük içindeki tüm anahtarları almak için `_____()` metodu kullanılır.

**7.** `_____` operatörü "eşit mi?" kontrolü yapar.

**8.** `_____` operatörü "ve" mantıksal işlemini yapar.

**9.** `range(1, 11)` fonksiyonu `_____` ile `_____` arasındaki sayıları üretir (11 dahil değil).

**10.** Döngüden çıkmak için `_____` anahtar kelimesi kullanılır.

**11.** Döngüde bir sonraki iterasyona geçmek için `_____` anahtar kelimesi kullanılır.

**12.** Fonksiyon tanımlamak için `_____` anahtar kelimesi kullanılır.

**13.** `**kwargs` parametresi `_____` formatında argümanlar alır.

**14.** Bir fonksiyonun kendini çağırmasına `_____` denir.

**15.** Sınıf tanımlamak için `_____` anahtar kelimesi kullanılır.

**16.** Sınıfın yapıcı metodu `_____` olarak adlandırılır.

**17.** Sınıftan nesne oluştururken otomatik çağrılan metod `_____` metodudur.

**18.** Private attribute'lere erişmek için genellikle `_____` ve `_____` metodları kullanılır.

**19.** `@property` decorator'ı bir metodu `_____` gibi kullanmamızı sağlar.

**20.** Bir listenin son elemanını silmek için `_____()` metodu kullanılır.

### BOŞLUK DOLDURMA CEVAPLARI:
1. # (diyez işareti)
2. float
3. insert
4. parantez veya () veya ( )
5. remove, discard
6. keys
7. ==
8. and
9. 1, 10
10. break
11. continue
12. def
13. anahtar=değer veya key=value
14. recursion veya özyineleme
15. class
16. __init__
17. __init__
18. getter, setter
19. attribute veya özellik
20. pop

---

## BÖLÜM 3: DOĞRU/YANLIŞ SORULARI (20 Soru - Her biri 1 puan)

**1.** Python'da değişken isimleri sayı ile başlayabilir. (D/Y)

**2.** Liste değiştirilebilir (mutable) bir veri yapısıdır. (D/Y)

**3.** Tuple değiştirilemez (immutable) bir veri yapısıdır. (D/Y)

**4.** Set içinde aynı eleman birden fazla kez bulunabilir. (D/Y)

**5.** Sözlük içindeki anahtarlar benzersiz olmalıdır. (D/Y)

**6.** `if-elif-else` yapısında birden fazla `elif` kullanılabilir. (D/Y)

**7.** `for` döngüsü sadece sayılarla çalışır. (D/Y)

**8.** `while` döngüsü koşul doğru olduğu sürece çalışır. (D/Y)

**9.** `break` anahtar kelimesi döngüden çıkmak için kullanılır. (D/Y)

**10.** `continue` anahtar kelimesi döngüyü tamamen sonlandırır. (D/Y)

**11.** Fonksiyonlar mutlaka parametre almalıdır. (D/Y)

**12.** Fonksiyonlar mutlaka değer döndürmelidir. (D/Y)

**13.** `*args` tuple formatında argümanlar alır. (D/Y)

**14.** `**kwargs` dictionary formatında argümanlar alır. (D/Y)

**15.** Recursive fonksiyonlar mutlaka bir base case (temel durum) içermelidir. (D/Y)

**16.** Bir sınıftan birden fazla nesne oluşturulabilir. (D/Y)

**17.** `__init__` metodu sınıf tanımlanırken otomatik çağrılır. (D/Y)

**18.** Private attribute'lere doğrudan erişilebilir. (D/Y)

**19.** `@property` decorator'ı bir metodu attribute gibi kullanmamızı sağlar. (D/Y)

**20.** `global` anahtar kelimesi fonksiyon içinde global değişkeni değiştirmek için kullanılır. (D/Y)

### DOĞRU/YANLIŞ CEVAPLARI:
1. Y (Yanlış - değişken isimleri sayı ile başlayamaz)
2. D (Doğru)
3. D (Doğru)
4. Y (Yanlış - set içinde aynı eleman birden fazla kez bulunamaz)
5. D (Doğru)
6. D (Doğru)
7. Y (Yanlış - for döngüsü listeler, stringler vb. ile de çalışır)
8. D (Doğru)
9. D (Doğru)
10. Y (Yanlış - continue bir sonraki iterasyona geçer, döngüyü sonlandırmaz)
11. Y (Yanlış - fonksiyonlar parametre almayabilir)
12. Y (Yanlış - fonksiyonlar değer döndürmeyebilir)
13. D (Doğru)
14. D (Doğru)
15. D (Doğru)
16. D (Doğru)
17. Y (Yanlış - __init__ metodu nesne oluşturulurken çağrılır, sınıf tanımlanırken değil)
18. Y (Yanlış - private attribute'lere doğrudan erişilemez, getter/setter kullanılmalı)
19. D (Doğru)
20. D (Doğru)

---

## BÖLÜM 4: KOD TAMAMLAMA SORULARI (20 Soru - Her biri 3 puan)

**1.** Aşağıdaki kodu tamamlayınız. Fonksiyon 1'den n'e kadar olan sayıların toplamını döndürmelidir.

```python
def toplam_bul(n):
    toplam = 0
    for i in range(1, _____):
        toplam = _____
    return _____
```

**2.** Aşağıdaki kodu tamamlayınız. Fonksiyon bir listenin en büyük elemanını bulmalıdır.

```python
def en_buyuk_bul(liste):
    en_buyuk = liste[0]
    for eleman in liste:
        if eleman > _____:
            en_buyuk = _____
    return _____
```

**3.** Aşağıdaki kodu tamamlayınız. Fonksiyon bir sayının çift mi tek mi olduğunu kontrol etmelidir.

```python
def cift_mi_tek_mi(sayi):
    if sayi % 2 == _____:
        return "Çift"
    else:
        return "Tek"
```

**4.** Aşağıdaki kodu tamamlayınız. Liste içindeki çift sayıları filtrelemelidir.

```python
cift_sayilar = []
for sayi in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if sayi % 2 == _____:
        _____.append(sayi)
print(cift_sayilar)
```

**5.** Aşağıdaki kodu tamamlayınız. Sözlük içindeki değerlerin toplamını bulmalıdır.

```python
sozluk = {"a": 10, "b": 20, "c": 30}
toplam = 0
for deger in sozluk._____():
    toplam += _____
print(toplam)
```

**6.** Aşağıdaki kodu tamamlayınız. Fonksiyon bir string'in uzunluğunu döndürmelidir.

```python
def uzunluk_bul(metin):
    sayac = 0
    for karakter in _____:
        sayac += _____
    return _____
```

**7.** Aşağıdaki kodu tamamlayınız. Recursive fonksiyon faktöriyel hesaplamalıdır.

```python
def faktoriyel(n):
    if n == 0 or n == 1:
        return _____
    else:
        return n * faktoriyel(_____)
```

**8.** Aşağıdaki kodu tamamlayınız. Sınıf tanımını ve __init__ metodunu tamamlayınız.

```python
class Ogrenci:
    def _____(self, isim, numara):
        self.isim = _____
        self.numara = _____

ogrenci1 = Ogrenci("Ahmet", 123)
print(ogrenci1.isim)
```

**9.** Aşağıdaki kodu tamamlayınız. Fonksiyon bir listenin elemanlarını tersine çevirmelidir.

```python
def ters_cevir(liste):
    ters_liste = []
    for i in range(len(liste) - 1, -1, _____):
        ters_liste.append(liste[_____])
    return ters_liste
```

**10.** Aşağıdaki kodu tamamlayınız. While döngüsü ile 1'den 10'a kadar sayıları yazdırmalıdır.

```python
sayac = 1
while sayac <= _____:
    print(sayac)
    sayac += _____
```

**11.** Aşağıdaki kodu tamamlayınız. Fonksiyon *args kullanarak tüm sayıların toplamını bulmalıdır.

```python
def topla(*args):
    toplam = 0
    for sayi in _____:
        toplam += _____
    return toplam

print(topla(1, 2, 3, 4, 5))
```

**12.** Aşağıdaki kodu tamamlayınız. Sınıf metodunu tamamlayınız.

```python
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def bilgi_yazdir(self):
        print("Marka:", self._____, "Model:", self._____)

araba1 = Araba("Toyota", "Corolla")
araba1.bilgi_yazdir()
```

**13.** Aşağıdaki kodu tamamlayınız. Set birleşim işlemi yapmalıdır.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
birlesim = set1._____(set2)
print(birlesim)
```

**14.** Aşağıdaki kodu tamamlayınız. Liste içindeki belirli bir elemanın kaç kez geçtiğini bulmalıdır.

```python
liste = [1, 2, 3, 2, 4, 2, 5]
sayac = liste._____(2)
print(sayac)
```

**15.** Aşağıdaki kodu tamamlayınız. Sözlük içine yeni bir anahtar-değer çifti eklemelidir.

```python
sozluk = {"a": 1, "b": 2}
sozluk._____({"c": 3})
print(sozluk)
```

**16.** Aşağıdaki kodu tamamlayınız. Recursive fonksiyon Fibonacci sayısını hesaplamalıdır.

```python
def fibonacci(n):
    if n <= 1:
        return _____
    elif n == 2:
        return _____
    else:
        return fibonacci(n - 1) + fibonacci(_____)
```

**17.** Aşağıdaki kodu tamamlayınız. Private attribute için getter metodu yazmalıdır.

```python
class Insan:
    def __init__(self, isim):
        self._____isim = isim
    
    def get_isim(self):
        return self._____isim

insan1 = Insan("Mehmet")
print(insan1.get_isim())
```

**18.** Aşağıdaki kodu tamamlayınız. İç içe döngü ile çarpım tablosu oluşturmalıdır.

```python
for i in range(1, _____):
    for j in range(1, _____):
        print(i, "x", j, "=", i * _____)
```

**19.** Aşağıdaki kodu tamamlayınız. Global değişkeni fonksiyon içinde değiştirmelidir.

```python
sayi = 10

def artir():
    _____ sayi
    sayi += 5

artir()
print(sayi)
```

**20.** Aşağıdaki kodu tamamlayınız. Fonksiyon bir sayının asal olup olmadığını kontrol etmelidir.

```python
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
        if sayi % i == _____:
            return _____
    return _____
```

### KOD TAMAMLAMA CEVAPLARI:

**1.**
```python
def toplam_bul(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam = toplam + i
    return toplam
```
Boşluklar: `n + 1`, `toplam + i`, `toplam`

**2.**
```python
def en_buyuk_bul(liste):
    en_buyuk = liste[0]
    for eleman in liste:
        if eleman > en_buyuk:
            en_buyuk = eleman
    return en_buyuk
```
Boşluklar: `en_buyuk`, `eleman`, `en_buyuk`

**3.**
```python
def cift_mi_tek_mi(sayi):
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"
```
Boşluk: `0`

**4.**
```python
cift_sayilar = []
for sayi in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)
print(cift_sayilar)
```
Boşluklar: `0`, `cift_sayilar`

**5.**
```python
sozluk = {"a": 10, "b": 20, "c": 30}
toplam = 0
for deger in sozluk.values():
    toplam += deger
print(toplam)
```
Boşluklar: `values`, `deger`

**6.**
```python
def uzunluk_bul(metin):
    sayac = 0
    for karakter in metin:
        sayac += 1
    return sayac
```
Boşluklar: `metin`, `1`, `sayac`

**7.**
```python
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)
```
Boşluklar: `1`, `n - 1`

**8.**
```python
class Ogrenci:
    def __init__(self, isim, numara):
        self.isim = isim
        self.numara = numara

ogrenci1 = Ogrenci("Ahmet", 123)
print(ogrenci1.isim)
```
Boşluklar: `__init__`, `isim`, `numara`

**9.**
```python
def ters_cevir(liste):
    ters_liste = []
    for i in range(len(liste) - 1, -1, -1):
        ters_liste.append(liste[i])
    return ters_liste
```
Boşluklar: `-1`, `i`

**10.**
```python
sayac = 1
while sayac <= 10:
    print(sayac)
    sayac += 1
```
Boşluklar: `10`, `1`

**11.**
```python
def topla(*args):
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

print(topla(1, 2, 3, 4, 5))
```
Boşluklar: `args`, `sayi`

**12.**
```python
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def bilgi_yazdir(self):
        print("Marka:", self.marka, "Model:", self.model)

araba1 = Araba("Toyota", "Corolla")
araba1.bilgi_yazdir()
```
Boşluklar: `marka`, `model`

**13.**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
birlesim = set1.union(set2)
print(birlesim)
```
Boşluk: `union`

**14.**
```python
liste = [1, 2, 3, 2, 4, 2, 5]
sayac = liste.count(2)
print(sayac)
```
Boşluk: `count`

**15.**
```python
sozluk = {"a": 1, "b": 2}
sozluk.update({"c": 3})
print(sozluk)
```
Boşluk: `update`

**16.**
```python
def fibonacci(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
Boşluklar: `n`, `1`, `n - 2`

**17.**
```python
class Insan:
    def __init__(self, isim):
        self.__isim = isim
    
    def get_isim(self):
        return self.__isim

insan1 = Insan("Mehmet")
print(insan1.get_isim())
```
Boşluklar: `__`, `__`

**18.**
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
```
Boşluklar: `11`, `11`, `j`

**19.**
```python
sayi = 10

def artir():
    global sayi
    sayi += 5

artir()
print(sayi)
```
Boşluk: `global`

**20.**
```python
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True
```
Boşluklar: `0`, `False`, `True`

---

## DEĞERLENDİRME

- **Bölüm 1 (Çoktan Seçmeli):** 20 soru × 2 puan = 40 puan
- **Bölüm 2 (Boşluk Doldurma):** 20 soru × 2 puan = 40 puan
- **Bölüm 3 (Doğru/Yanlış):** 20 soru × 1 puan = 20 puan
- **Bölüm 4 (Kod Tamamlama):** 20 soru × 3 puan = 60 puan

**TOPLAM:** 160 puan

**BAŞARILAR DİLERİM!**

