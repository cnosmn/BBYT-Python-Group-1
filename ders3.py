hiz = 0

def gaza_bas():
    global hiz
    hiz += 10

def fren_yap():
    global hiz
    hiz -= 5

print("başlangıç hiz degeri : ",hiz)
gaza_bas()
print("hiz degeri : ",hiz)
fren_yap()
print("hiz degeri : ",hiz)



# Nesneye Yönelimli Programlama

class Ogrenci :
    adi = "mehmet"
    numarasi = "031525"

ogrenci = Ogrenci()

print(ogrenci.adi)
print(ogrenci.numarasi)

ogrenci1 = Ogrenci()
ogrenci2 = Ogrenci()
ogrenci3 = Ogrenci()
ogrenci4 = Ogrenci()

ogrenci1.adi = "ahmet"
print(ogrenci1.adi)
# ogrenci1 nesnesinin ad verisini değiştirdim diğer nesnelere dokunmadan
print(ogrenci2.adi)

Ogrenci.adi = "degistirildi"
print("ogrenci1 adı : ",ogrenci1.adi)
print("ogrenci2 adı : ",ogrenci2.adi)


class Araba:

    def __init__(self):
        self.hiz = 0
        self.marka = "ford"
        self.model = "focus"

araba1 = Araba()
araba2 = Araba()
araba3 = Araba()
araba4 = Araba()


araba1.marka = "bmw"
print(araba1.marka)
print(araba2.marka)


class Insan:

    def __init__(self,isim,soyisim,tc_no):
        self.name = isim
        self.surname = soyisim
        self.id = tc_no 
    

insan1 = Insan("yusuf","ozkan","1111111")
insan2 = Insan("osman","can","1111111")
insan3 = Insan("nisa","er","1111111")
insan4 = Insan("mehmet","taka","1111111")

insan1.id = 12313123
print(insan1.id)
