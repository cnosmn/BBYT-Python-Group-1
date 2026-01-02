Aşağıda lise seviyesinde Python dersinde rahatlıkla kullanılabilecek **recursive (özyinelemeli) fonksiyon örnekleri**, **adım adım açıklamaları**, ve **senaryo tabanlı kullanım fikirleri** yer almaktadır. İçerik hem öğretici anlatım hem de sınıfta uygulama yapılabilir nitelikte hazırlanmıştır.

---

# 1. Temel Recursive Yapısı (Giriş Örneği)

Öğrencilerin anlaması için önce **durdurma koşulu (base case)** + **tekrar çağrı (recursive case)** mantığını göstermek gerekir.

### Örnek 1: Bir sayıyı geri saydırma

```python
def geri_say(n):
    if n == 0:
        print("Bitti")
        return
    print(n)
    geri_say(n - 1)

geri_say(5)
```

**Açıklama:**

* `n == 0` durdurma koşulu.
* Her adımda fonksiyon kendisini `n-1` ile çağırıyor.

Kullanım amacı: Recursive yapıyı en basit haliyle kavratmak.

---

# 2. Matematiksel Recursive Örnekler

## Örnek 2: Faktöriyel Hesaplama

```python
def faktoriyel(n):
    if n == 1:
        return 1
    return n * faktoriyel(n - 1)

print(faktoriyel(5))  # 120
```

**Açıklama:**

* 5! = 5 × 4 × 3 × 2 × 1
* Recursive düşünme pratiği için ideal.

---

## Örnek 3: Fibonacci Serisi

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(10):
    print(fib(i))
```

**Açıklama:**

* Her çağrı iki yeni çağrı üretir → ağaç yapısı oluşur.
* Performans konusu tartışılabilir: memoization, dynamic programming.

---

# 3. Veri Yapıları ile Recursive Örnekleri

## Örnek 4: Liste İçinde Toplam Bulma

```python
def liste_toplam(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + liste_toplam(liste[1:])

print(liste_toplam([1, 2, 3, 4, 5]))
```

**Açıklama:**

* Listeyi her adımda küçültme.
* “Diziyi parçalara ayırma” mantığını öğretir.

---

## Örnek 5: İç İçe Listelerin Elemanlarını Yazdırma

```python
def yazdir(l):
    for eleman in l:
        if isinstance(eleman, list):
            yazdir(eleman)
        else:
            print(eleman)

yazdir([1, [2, 3], [4, [5, 6]]])
```

**Açıklama:**

* Dosya sistemi, JSON yapıları gibi iç içe yapılarda kullanılır.
* “Nested structure traversal” kavramını öğretir.

---

# 4. Karar Yapılarıyla Recursive Örnekleri

## Örnek 6: Binary Search (Recursive)

```python
def binary_search(liste, hedef, sol, sag):
    if sol > sag:
        return -1

    orta = (sol + sag) // 2

    if liste[orta] == hedef:
        return orta
    elif hedef < liste[orta]:
        return binary_search(liste, hedef, sol, orta - 1)
    else:
        return binary_search(liste, hedef, orta + 1, sag)

liste = [1,3,5,7,9,11]
print(binary_search(liste, 7, 0, len(liste)-1))
```

**Açıklama:**

* Aramayı yarıya bölme mantığını çok iyi açıklar.

---

# 5. String İşlemleri ile Recursive Örnekleri

## Örnek 7: Bir String'i Tersine Çevirme

```python
def ters_cevir(s):
    if len(s) == 0:
        return ""
    return s[-1] + ters_cevir(s[:-1])

print(ters_cevir("python"))
```

**Açıklama:**

* String slicing + recursion kombinasyonu.

---

# 6. Uygulamalı Senaryolar

Bu kısım, öğrencilere “gerçek hayatta nerede kullanılır?” sorusuna yanıt verir.

---

## Senaryo 1: Dosya Sistemi Tarayıcı

Durum:

* Öğrenciler bir klasörün altındaki tüm dosyaları göstermek istiyor.
  Recursive yapı olmazsa klasör içindeki alt klasörler için sınırsız döngü gerekir.

Sadeleştirilmiş örnek:

```python
import os

def tara(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            tara(full_path)
        else:
            print(full_path)

tara("C:/Users")
```

---

## Senaryo 2: Bir Oyunda Bölüm İçindeki Alt Görevleri Tamamlama

Durum:

* Oyun tasarımında bir görevin alt görevleri vardır, alt görevlerin de kendi alt görevleri olabilir.

Kurgu örneği:

```python
gorevler = {
    "Görev": ["Alt Görev 1", "Alt Görev 2"],
    "Alt Görev 2": ["Alt Görev 2.1", "Alt Görev 2.2"],
    "Alt Görev 2.2": ["Alt Görev 2.2.1"]
}

def gorev_yap(g):
    print("Yapılıyor:", g)
    if g in gorevler:
        for alt in gorevler[g]:
            gorev_yap(alt)

gorev_yap("Görev")
```

---

## Senaryo 3: Menü Sistemi Oluşturma

Durum:

* Çok seviyeli bir menü tasarımı (website, mobil app).

```python
menu = {
    "Ana": ["Ayarlar", "Profil"],
    "Ayarlar": ["Gizlilik", "Bildirimler"],
    "Profil": ["Bilgi", "Fotoğraf"]
}

def menu_goster(secenek):
    print(secenek)
    if secenek in menu:
        for alt in menu[secenek]:
            menu_goster(alt)

menu_goster("Ana")
```

---

## Senaryo 4: Fraktal Çizimi (Turtle ile)

Durum:

* Matematiksel fraktalları recursive fonksiyonlarla çizebilirsiniz.

```python
import turtle

def ciz(uzunluk, seviye):
    if seviye == 0:
        turtle.forward(uzunluk)
        return

    ciz(uzunluk/3, seviye-1)
    turtle.left(60)
    ciz(uzunluk/3, seviye-1)
    turtle.right(120)
    ciz(uzunluk/3, seviye-1)
    turtle.left(60)
    ciz(uzunluk/3, seviye-1)

turtle.speed(0)
ciz(200, 3)
turtle.done()
```

---

# 7. Sınıf İçin Kullanılabilir Uygulama Soruları

### Soru 1

Bir sayının rakamları toplamını recursive hesaplayan fonksiyon yazın.
Örnek: `rakam_toplam(456) → 15`

### Soru 2

Bir listedeki en büyük elemanı recursive bulan fonksiyon yazın.

### Soru 3

Bir string içinde belirli bir karakterin kaç kez geçtiğini recursive bulan fonksiyon yazın.

### Soru 4

İç içe listelerdeki toplam eleman sayısını recursive hesaplayın.

---

# İsterseniz

Bu içeriği:

* Ders planı formatına çevirebilir,
* Sunuma dönüştürebilir (HTML, PowerPoint),
* Çalışma kağıdı hazırlayabilirim.
