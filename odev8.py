
#Yeni Alt Sınıf: Memur (Kalıtım)

"""
İstenilenler

Kisi sınıfından türeyen yeni bir sınıf yazınız:

class Memur(Kisi):
Özellikler

-birim
-calisma_saati

Metotlar

-bilgileri_yaz() → override edilecek
-gorev_yap() → override edilecek

Örnek Çıktı
Ad: Hasan Soyad: Çelik, Yaş: 45 Birim: Yazı İşleri Çalışma Saati: 8
Hasan görevini yapıyor. Memur olarak çalışıyor.

"""



class Kisi:
    def __init__(self, ad,soyad,yas):
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas

    @property
    def ad(self):
        return self.__ad
    
    @ad.setter
    def ad(self,yeni_ad):
        self.__ad = yeni_ad
    
    @property
    def soyad(self):
        return self.__soyad
    
    @soyad.setter
    def soyad(self,yeni_soyad):
        self.__soyad = yeni_soyad

    @property
    def yas(self):
        return self.__yas

    @yas.setter
    def yas(self,yeni_yas):
        self.__yas = yeni_yas

    def bilgileri_yaz(self):
        return "Ad :" +self.__ad + " Soyad: " + self.__soyad + ", Yaş: " + str(self.__yas)
    
    def gorev_yap(self):
        return self.__ad +" görevini yapıyor."
    

class Ogrenci(Kisi):
    def __init__(self, ad, soyad, yas, ogrenci_no,sinif):
        super().__init__(ad,soyad,yas)
        self.__ogrenci_no = ogrenci_no
        self.__sinif = sinif

    @property
    def ogrenci_no(self):
        return self.__ogrenci_no

    @ogrenci_no.setter
    def ogrenci_no(self,yeni_ogrenci_no):
        self.__ogrenci_no = yeni_ogrenci_no

    @property
    def sinif(self):
        return self.__sinif

    @sinif.setter
    def sinif(self,yeni_sinif):
        self.__sinif = yeni_sinif

    # override()
    def bilgileri_yaz(self):
        temel_bilgiler = super().bilgileri_yaz()
        return temel_bilgiler + " Öğrenci No: " + str(self.__ogrenci_no) + " Sınıf: " + self.__sinif
    
    # override()
    def gorev_yap(self):
        kisi_gorev = super().gorev_yap()
        return kisi_gorev + "Öğrenci "+ self.__sinif + " sınıfında derse gidiyor."

class Ogretmen(Kisi):
    def __init__(self, ad, soyad, yas, bolum,maas):
        super().__init__(ad,soyad,yas)
        self.__bolum = bolum
        self.__maas = maas

    @property
    def bolum(self):
        return self.__bolum

    @bolum.setter
    def bolum(self,yeni_bolum):
        self.__bolum = yeni_bolum

    @property
    def maas(self):
        return self.__maas

    @maas.setter
    def maas(self,yeni_maas):
        self.__maas = yeni_maas
    # override()
    def bilgileri_yaz(self):
        temel_bilgiler = super().bilgileri_yaz()
        return temel_bilgiler + " Bölüm: " + self.__bolum + " Maaş: " + str(self.__maas)

     # override()
    def gorev_yap(self):
        return "Öğretmen "+ self.__bolum + " uzmanlığında derse giriyor."


class Memur(Kisi):
    def __init__(self, ad, soyad, yas, birim, calisma_saati):
        super().__init__(ad,soyad,yas)
        self.__birim = birim
        self.__calisma_saati = calisma_saati

    @property
    def birim(self):
        return self.__birim

    @birim.setter
    def birim(self,yeni_birim):
        self.__birim = yeni_birim

    @property
    def calisma_saati(self):
        return self.__calisma_saati

    @calisma_saati.setter
    def calisma_saati(self,calisma_saati):
        self.__calisma_saati = calisma_saati
    
    def bilgileri_yaz(self):
        temel_bilgiler = super().bilgileri_yaz()
        return temel_bilgiler + " Birim: " + self.__birim + " Çalışma Saati: " + str(self.__calisma_saati)
    
    def gorev_yap(self):
        return self.ad + " görevini yapıyor. Memur olarak çalışıyor"
    
memur1 = Memur("Ahmet", "Yılmaz", 35, "Birim",8)
    
print(memur1.bilgileri_yaz())
print(memur1.gorev_yap())

kisi1 = Kisi("Ali", "Veli", 30)
print(kisi1.bilgileri_yaz())
print(kisi1.gorev_yap())

ogrenci1 = Ogrenci("Ahmet", "Yılmaz", 15, "12345", "10A")
ogrenci2 = Ogrenci("Mehmet", "Demir", 16, "12346", "10B")

print(ogrenci1.bilgileri_yaz())
print(ogrenci2.gorev_yap())
print(ogrenci2.bilgileri_yaz())


ogretmen1 = Ogretmen("Ayşe", "Kaya", 40, "Bilgisayar Mühendisliği", 50000)
ogretmen2 = Ogretmen("Mehmet", "Yılmaz", 35, "İngilizce", 45000)

print(ogretmen1.bilgileri_yaz())
print(ogretmen2.gorev_yap())

print("ogretmen1.ad : ",ogretmen1.ad)


# Encapsulation  -> get ve set metotları 
# sınıfın verilerini veya attributeleri fonksiyonlarla sarmaladığımız yapı

# Kalıtım - Inheritance -> üst sınıf - alt sınıf ilişkisi
# alt sınıf üst sınıfın attributelerine sahip ve üst sınıfın fonksiyonlarını kullanabilir

# Polimorfizm -> Çok biçimlilik  
# Aynı metod(fonksiyon) adının farklı sınıflarda farklı davranışlar sergilemesi

# override -> üst sınıftan miras alınan bir fonksiyonun alt sınıfta yeniden yazılması



## 5.6 `isinstance` Kullanımı


print(isinstance(ogrenci1, Ogrenci))   # True
print(isinstance(ogrenci2, Kisi))      # True
print(isinstance(ogrenci1, Ogretmen))  # False

## 5.7 `issubclass` Kullanımı

print(issubclass(Ogrenci, Kisi))     # True
print(issubclass(Ogretmen, Kisi))    # True
print(issubclass(Kisi, Ogrenci))     # False
print(issubclass(Memur,Kisi))





