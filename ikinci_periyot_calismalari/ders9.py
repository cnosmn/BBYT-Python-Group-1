
# abstract class
# dosya işlemleri

# büyük proje -> bir tane  (restoran yönetim sistemi)


class Sekil :
    # Abstract class yapısı
    def __init__(self):
        if type(self) is Sekil:
            raise Exception("Sekil abstract class'tan türetildiği için nesne oluşturulamaz.")

    def alan_hesapla(self):
        raise NotImplementedError("alan_hesapla metodu alt sınıflarda uygulanmalıdır.")

    def cevre_hesapla(self):
        raise NotImplementedError("cevre_hesapla metodu alt sınıflarda uygulanmalıdır.")
    
class Daire(Sekil):
    def __init__(self,yaricap):
        super().__init__()
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
        super().__init__()
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


daire1 = Daire(5)
daire1.alan_hesapla()
daire1.cevre_hesapla()

dikdortgen1 = Dikdörtgen(4,6)
dikdortgen1.alan_hesapla()
dikdortgen1.cevre_hesapla()