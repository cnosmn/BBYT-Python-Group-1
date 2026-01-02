

# bir oyun karakteri sınıfı olucak 
# en az 3 attribute(özellik) olsun
# bir kahraman bir de dusman nesnesi olusturun bu sınıftan
# isim,seviye,can,guc bunlar haricinde ekleyebilrsiniz

# saldir() fonksiyonu olsun 
# dusman nesnesinin canından eksilicek (guc/10) kadar eksilicek
# hasar_al() fonksiyonu olsun
# dusman saldırdığında can eksilsin (guc/10) kadar eksilicek
# seviye_atla() fonksiyonu olsun
# özellikleri artsın (bunu siz yapın nasıl ne kadar artıcak belirleyin)




# Yusuf Özkan Ödev 

class Normalchar:
    def __init__(self,can,guc,isim):
        self.can = can
        self.guc = guc
        self.isim = isim

    def selamla(self):
        print("Merhabalar Benim Adım :",self.isim)

    def saldir(self,dusman_can):
        dusman_can = dusman_can - self.guc / 10
        self.guc = self.guc + 1
        return dusman_can

    def hasar_al(self,dusman_guc):
        self.can = self.can - dusman_guc / 10

    def seviye_atla(self):
        self.guc = self.guc + 10
        self.can = self.can + 20


kahraman = Normalchar(100,70,"Steve")
kahraman.selamla()

zombie = Normalchar(80,30,"Zombie Köylü")
zombie.selamla()

zombie.can = kahraman.saldir(zombie.can)

print(zombie.can)
print(kahraman.guc)


# Nisa Ödev

class Karakter:
    def __init__(self, isim, can, guc):
        self.isim = isim
        self.can = can
        self.guc = guc
        self.seviye = 1

    def saldir(self, dusman):
        hasar = self.guc / 10
        dusman.can -= hasar # dusman.can = dusman.can - hasar
        print(dusman.isim, "canı:", dusman.can)

    def hasar_al(self,dusman):
        hasar = dusman.guc / 10
        self.can -= hasar
        print(self.isim, "canı:", self.can)

    def seviye_atla(self):
        self.seviye += 1
        self.can += 20
        self.guc += 5
        print(self.isim, "seviye atladı!")



kahraman = Karakter("Selena", 100, 25)
dusman = Karakter("Hades", 95, 20)

"""
print("can:", kahraman.can)
print("gucu:" ,kahraman.guc)
print("ismi:" ,kahraman.isim)

kahraman.saldir(dusman)
dusman.saldir(kahraman)
dusman.seviye_atla()
kahraman.seviye_atla()

print("son canı:", kahraman.can)
print("son gucu:" ,kahraman.guc)
print("ismi:" ,kahraman.isim)

"""