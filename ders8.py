

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
