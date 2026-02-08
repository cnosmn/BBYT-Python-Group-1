from abc import ABC, abstractmethod
import math

class Sekil(ABC):
    @abstractmethod
    def alan_hesapla(self):
        pass

    @abstractmethod
    def cevre(self):
        pass

 
class Daire(Sekil):
    def __init__(self,yaricap):
        self.__yaricap = yaricap

    # override
    def alan_hesapla(self):
        alan = 3.14 * (self.__yaricap ** 2)
        print("Dairenin alanı: ", alan)
        return alan
    
    # override
    def cevre_hesapla(self):
        cevre = 2 * 3.14 * self.__yaricap
        print("Dairenin çevresi: ", cevre)
        return cevre


class Dikdörtgen(Sekil):
    def __init__(self,uzun_kenar,kisa_kenar):
        self.__uzun_kenar = uzun_kenar
        self.__kisa_kenar = kisa_kenar

    # override
    def alan_hesapla(self):
        alan = self.__uzun_kenar * self.__kisa_kenar
        print("Dikdörtgenin alanı: ", alan)
        return alan

    # override
    def cevre_hesapla(self):
        cevre = 2 * (self.__uzun_kenar + self.__kisa_kenar)
        print("Dikdörtgenin çevresi: ", cevre)
        return cevre
