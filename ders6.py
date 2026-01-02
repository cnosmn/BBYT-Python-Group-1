
# nesneye yönelimli programlama (OOP)
# encapsulation (kapsülleme) , 
# inheritance (kalıtım) , 
# polymorphism (çok biçimlilik),
# abstraction (soyutlama)


# encapsulation : verilerin ve fonksiyonların bir arada tutulmasıdır.

class Insan : 

    def __init__(self,name,soyisim,tc,cinsiyet):
        self.isim = name
        self.soyisim = soyisim
        self.__tc = tc
        self.cinsiyet = cinsiyet
    
    def get_tc(self):
        return self.__tc
    
    def set_tc(self,yeni_tc):
        self.__tc = yeni_tc
        return "Başarılı"
    
    def bilgileri_yaz(self):
        print("isim : ",self.isim)
        print("soyisim : ",self.soyisim)
        print("tc no : ",self.__tc)
        print("cinsiyet : ",self.cinsiyet)
    

insan = Insan("osman","can","12321312312","erkek")

insan.bilgileri_yaz()
insan.isim = "Osman"
insan.bilgileri_yaz()

print("tc no : ",insan.get_tc())

print(insan.set_tc("437678678"))
print("tc no : ",insan.get_tc())


class Ogrenci :

    def __init__(self,
        isim,
        soyisim,
        numara,
        sinif,
        cinsiyet,
        notlar
        ):

    self.__isim = isim
    self.__soyisim = soyisim
    self.__numara = numara
    self.__sinif = sinif
    self.__cinsiyet = cinsiyet
    self.__notlar = notlar

    @property
    def isim(self):
        return self.__isim
    
    @isim.setter
    def isim(self,yeni_isim):
        self.__isim = yeni_isim

    @property
    def soyisim(self):
        return self.__soyisim
    
    @soyisim.setter
    def soyisim(self,yeni_soyisim):
        self.__soyisim = yeni_soyisim

    def not_ekle(self,yeni_not):
        if yeni_not >= 0 and yeni_not <= 100 :
            self.__notlar.append(yeni_not)
            print("yeni notlar başarılı bir şekilde eklendi")
        else :
            print("not 0 ile 100 arasında olmalıdır")
    
    def ortalama_hesapla(self):
        if len(self.__notlar) == 0 :
            print("Ogrencinin notları yok")
        else :
            ortalama = sum(self.__notlar) / len(self.__notlar)
            print("Ogrencinin Not Ortalaması : ", ortalama)
        

    