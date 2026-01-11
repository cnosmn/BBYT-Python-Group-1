

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
        print("ad : ",self.__ad)
        print("soyad : ",self.__soyad)
        print("yas : ",self.__yas)
    
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


    