
Python’da erişim seviyeleri **isimlendirme ile belirtilir**:

| Yazım        | Anlam                   |
| ------------ | ----------------------- |
| `degisken`   | public                  |
| `_degisken`  | protected (konvansiyon) |
| `__degisken` | private (isim gizleme)  |

---

## 4.3 `_` ve `__` Kullanımı

### Örnek: Öğrenci Notu (Private Attribute)

```python
class Ogrenci:
    def __init__(self, ad, notu):
        self.ad = ad              # public
        self._okul = "Atatürk Lisesi"  # protected
        self.__notu = notu        # private
```

> `__notu` dışarıdan **doğrudan erişilemez**.

```python
ogrenci = Ogrenci("Ahmet", 75)
# print(ogrenci.__notu)  # HATA
```

---

## 4.4 Getter ve Setter Metodları

### Mantık

* **Getter:** Veriyi okumak
* **Setter:** Kurallı şekilde değiştirmek

```python
class Ogrenci:
    def __init__(self, ad, notu):
        self.ad = ad
        self.__notu = notu

    def notu_getir(self):
        return self.__notu

    def notu_degistir(self, yeni_not):
        if 0 <= yeni_not <= 100:
            self.__notu = yeni_not
        else:
            print("Geçersiz not!")
```

Kullanım:

```python
ogrenci = Ogrenci("Zeynep", 85)

print(ogrenci.notu_getir())
ogrenci.notu_degistir(95)
print(ogrenci.notu_getir())
```

---

## 4.5 `@property` Dekoratörü

Getter/Setter’ın **daha Pythonic** hali.

```python
class Ogrenci:
    def __init__(self, ad, notu):
        self.ad = ad
        self.__notu = notu

    @property
    def notu(self):
        return self.__notu

    @notu.setter
    def notu(self, yeni_not):
        if 0 <= yeni_not <= 100:
            self.__notu = yeni_not
        else:
            print("Geçersiz not!")
```

Kullanım:

```python
ogrenci = Ogrenci("Mehmet", 70)

print(ogrenci.notu)
ogrenci.notu = 90
print(ogrenci.notu)
```

> Öğrencilere şunu vurgulayın:
> **Değişken gibi görünüyor ama arka planda method çalışıyor.**

---

# 5. MİRAS (Inheritance)

## 5.1 Üst Sınıf – Alt Sınıf İlişkisi

### “is-a” Mantığı

* Öğrenci **bir kişidir**
* Öğretmen **bir kişidir**

---

## 5.2 Üst Sınıf: Kisi

```python
class Kisi:
    def __init__(self, ad):
        self.ad = ad

    def bilgi(self):
        print("Ad:", self.ad)
```

---

## 5.3 Alt Sınıf: Ogrenci

```python
class Ogrenci(Kisi):
    def __init__(self, ad, numara):
        super().__init__(ad)
        self.numara = numara

    def bilgi(self):
        print("Öğrenci:", self.ad, "- Numara:", self.numara)
```

---

## 5.4 Alt Sınıf: Ogretmen

```python
class Ogretmen(Kisi):
    def __init__(self, ad, brans):
        super().__init__(ad)
        self.brans = brans

    def bilgi(self):
        print("Öğretmen:", self.ad, "- Branş:", self.brans)
```

---

## 5.5 Metod Override (Ezme)

Aynı method adı, farklı davranış:

```python
ogrenci = Ogrenci("Elif", 123)
ogretmen = Ogretmen("Ali", "Matematik")

ogrenci.bilgi()
ogretmen.bilgi()
```

---

## 5.6 `isinstance` Kullanımı

```python
print(isinstance(ogrenci, Ogrenci))   # True
print(isinstance(ogrenci, Kisi))      # True
print(isinstance(ogrenci, Ogretmen))  # False
```

---

## 5.7 `issubclass` Kullanımı

```python
print(issubclass(Ogrenci, Kisi))     # True
print(issubclass(Ogretmen, Kisi))    # True
print(issubclass(Kisi, Ogrenci))     # False
```

---

# Derste Akış Önerisi (Önemli)

1. **Problemi anlat** (notu herkes değiştirebilir mi?)
2. Kapsülleme ile çöz
3. Aynı sistemde kişi–öğrenci ilişkisini kur
4. En sonda `isinstance` ile nesne türü kontrolü

---

İstersen bir sonraki adımda:

* Bu konulara özel **uygulama ödevi**
* **Çoktan seçmeli + kod okuma soruları**
* **Mini proje (Okul otomasyonu)**
* **Slayt anlatım metni**

hazırlayabilirim. Hangisini istediğini söylemen yeterli.
