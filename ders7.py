

class Ogrenci :
    def __init__(self,isim,okul,numarasi):
        self.__isim = isim # private
        self._okul = okul # protected -> bir kere değer verilir başka değiştirilemez
        self.__numarasi = numarasi # private

    def get_isim(self):
        return self.__isim
    
    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim

    def get_okul(self):
        return self._okul

    def get_numarasi(self):
        return self.__numarasi
    
    def set_numarasi(self,yeni_numara):
        self.__numarasi = yeni_numara

    def bilgileri_goster(self):
        print("Öğrenci Adı: ",self.__isim)
        print("Okul: ",self._okul)
        print("Numara: ",self.__numarasi)

ogrenci1 = Ogrenci("Ahmet","İstanbul Üniversitesi",12345)
ogrenci2 = Ogrenci("Mehmet","Ankara Üniversitesi",54321)
print(ogrenci1.get_isim())
ogrenci1.set_isim("Ali")
ogrenci1.bilgileri_goster()


class Insan:
    def __init__(self,cinsiyet,yas):
        self.__cinsiyet = cinsiyet
        self.__yas = yas

    @property
    def cinsiyet(self):
        return self.__cinsiyet

    @cinsiyet.setter
    def cinsiyet(self, yeni_cinsiyet):
        self.__cinsiyet = yeni_cinsiyet

    @property
    def yas(self):
        return self.__yas

    @yas.setter
    def yas(self, yeni_yas):
        if yeni_yas <= 0 :
            print("Yaş negatif olamaz!")
        else :
            self.__yas = yeni_yas

insan1 = Insan("Erkek", 25)
insan2 = Insan("Kadın", 30)

insan1.yas = -5
print("insan1.yas:", insan1.yas)


class Human:
    def __init__(self,yas):
        self.yas = yas

human1 = Human(30)

human1.yas = -5
print("human1.yas:", human1.yas)