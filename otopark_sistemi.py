from abc import ABC, abstractmethod
from datetime import datetime

class Arac(ABC):

    def __init__(self, 
                   plaka, 
                   marka,
                   model,
                   giris_zamani,
                   cikis_zamani,
                   park_suresi,
                   arac_tipi
                   ):
        self.__plaka = plaka
        self.__marka = marka
        self.__model = model
        self.__giris_zamani = None
        self.__cikis_zamani = None
        self.__park_suresi = park_suresi
        self.__arac_tipi = arac_tipi


    
    
    def bilgileri_goster(self):
        print("Plaka: ", self.__plaka)
        print("Marka: ", self.__marka)
        print("Model: ", self.__model)
        print("Giriş Zamanı: ", self.__giris_zamani)
        print("Çıkış Zamanı: ", self.__cikis_zamani)
        print("Park Süresi: ", self.__park_suresi, "saat")
        print("Araç Tipi: ", self.arac_tip())

    def giris_yap(self):
        self.__giris_zamani = datetime.now()

    def cikis_yap(self):
        self.__cikis_zamani = datetime.now()
    
    def park_suresini_hesapla(self):
        if self.__giris_zamani is not None and self.__cikis_zamani is not None:
            self.__park_suresi = (self.__cikis_zamani - self.__giris_zamani) // 3600
            return self.__park_suresi
        
    @abstractmethod
    def ucret_hesapla(self):
        pass

    @abstractmethod
    def arac_tip(self):
        """
        Arac tipini döndüren bir metot.
         - Bu metot, aracın tipini belirlemek için kullanılacak ve her araç tür
        """
        pass

class OtoparkYeri(ABC):

    # Otopark yeri için abstract sınıf
    def __init__(self, yer_numarasi):
        self.__dolu_mu = False
        self.__arac = None
        self.__yer_numarasi = yer_numarasi

    @abstractmethod
    def yer_tipi(self):
        # Otopark yerinin tipini döndüren bir metot.
        pass

    @abstractmethod
    def arac_uygun_mu(self, arac):
        # Verilen aracın bu otopark yerine uygun olup olmadığını kontrol eden bir metot.
        pass

    def park_et(self, arac):
        if self.__dolu_mu and self.arac_uygun_mu(arac):
            self.arac = arac
            self.__dolu_mu = True
            arac.giris_yap()
            print(arac.bilgileri_goster(), " otopark yerine park edildi.")
            return True
        else:
            print("Bu otopark yerine park edilemez.")
            return False

    def arac_cikar(self):
        if self.__dolu_mu:
            self.__dolu_mu = False
            # self.__arac.cikis_yap() yerine arac.cikis_yap() kullanılmalı, çünkü self.__arac zaten arac nesnesini tutuyor.
            arac = self.__arac
            self.__arac = None
            arac.cikis_yap()
            print(arac.bilgileri_goster(), " otopark yerinden çıkarıldı.")
            print("Park Ücreti: ", arac.ucret_hesapla(), " TL")
            return arac
        else:
            print("Bu otopark yeri zaten boş.")
            return None
        
class Otomobil(Arac):
    
    def arac_tip(self):
        return "Otomobil"
    
    def ucret_hesapla(self):
        park_suresi = self.park_suresini_hesapla()
        park_ucreti = 120
        if park_suresi is not None:
            park_ucreti += (park_suresi -1) * 15
        else:
            return 0
          
class Motorsiklet(Arac):
    
    def arac_tip(self):
        return "Motorsiklet"
    
    def ucret_hesapla(self):
        park_suresi = self.park_suresini_hesapla()
        park_ucreti = 80
        if park_suresi is not None:
            park_ucreti += (park_suresi -1) * 10
        else:
            return 0
        
class Kamyon(Arac):
    
    def arac_tip(self):
        return "Kamyon"
    
    def ucret_hesapla(self):
        park_suresi = self.park_suresini_hesapla()
        park_ucreti = 150
        if park_suresi is not None:
            park_ucreti += (park_suresi -1) * 30
        else:
            return 0
     
class Minibus(Arac):
    
    def arac_tip(self):
        return "Minibus"
    
    def ucret_hesapla(self):
        park_suresi = self.park_suresini_hesapla()
        park_ucreti = 140
        if park_suresi is not None:
            park_ucreti += (park_suresi -1) * 20
        else:
            return 0
        
class StandartOtoparkYeri(OtoparkYeri):
    
    def yer_tipi(self):
        return "Standart Otopark Yeri"
    
    def arac_uygun_mu(self, arac):
        return isinstance(arac, (Otomobil, Motorsiklet))

class BuyukAracYeri(OtoparkYeri):
    
    def yer_tipi(self):
        return "Standart Otopark Yeri"
    
    def arac_uygun_mu(self, arac):
        return isinstance(arac, (Otomobil, Motorsiklet))
