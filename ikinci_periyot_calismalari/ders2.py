# int
# float
# string
# bool

# list
# tuple
# set
# dict

liste = [1,2,3,4,5,6,5,7,8,9,10]

liste.count(5)
liste.insert(0,100)
print(liste)
liste.reverse()
print(liste)


tuple1 = (1,2,3,4,5,6,7,8,9,10)
print(tuple1.count(5))
print(tuple1.index(5))

print(len(tuple1))

tuple2 = ("a","b","c","d","e","f","g")
birlesmis_tuple = tuple1 + tuple2
print("birlestirilmis tuple : ",birlesmis_tuple)

carpilmis_tuple = tuple1 * 3
print("carpilmis tuple : ",carpilmis_tuple)

# setler - kümeler özel fonksiyonları
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}

set1.add(100)
print("set1 :", set1)

set1.remove(10)
print("set1 :", set1)
# set1.remove(200)  # hata verir

set1.discard(200)  # hata vermez
print("set1 :", set1)

union_set = set1.union(set2)
print("birleşim :", union_set)

difference_set = set1.difference(set2)
print("kesişim :", difference_set)

set2.clear()
print("set2 :", set2)

print(len(set1))


# dictionary - sözlüklerin özel fonksiyonları

sozluk = {"bir":1, "ikinci":2, "uc":3, "dort":4, "bes":5}
print("sozlugun bir anahtar kelimeli değeri",sozluk["bir"])

print(sozluk.get("alti","bu key sozluk verisinde yok"))  # hata vermez

print("keys : ",sozluk.keys())
print("values : ",sozluk.values())
print("items : ",sozluk.items())

sozluk.update({"bir":10})
print("guncellenmis sozluk :",sozluk)

sozluk.update({"alti":6})
print("guncellenmis sozluk :",sozluk)

sozluk.pop("alti")
print("pop sonrasi sozluk :",sozluk)


# canı -> integer
# hasar -> float
# boyut -> string
# ismi  -> string
# savunma -> integer

dusman1 ={
    "canı": 100,
    "hasar": 15.5,
    "boyut": "büyük",
    "ismi": "Zombi",
    "savunma": 5
}

dusman2 ={
    "canı": 80,
    "hasar": 10.0,
    "boyut": "küçük",  
    "ismi": "İskelet",
    "savunma": 3
}

class Dusman:
    def __init__(self, can, hasar, boyut, ismi, savunma):
        self.can = can
        self.hasar = hasar 
        self.boyut = boyut
        self.ismi = ismi
        self.savunma = savunma
        
    def selam_ver(self):
        print("Merhaba ben ", self.ismi)

    def selam():
        print("Merhaba ben bir düşman sınıfıyım.")

yusuf = Dusman(can=100,hasar=55,boyut="kucuk",ismi="Yusuf",savunma=33)

print("Dusman sınıfından nesne Yusuf : ",yusuf)
print("Yusuf ismi :",yusuf.ismi)
print("Yusuf canı :",yusuf.can)
print("Yusuf hasarı :",yusuf.hasar)
print("Yusuf boyutu :",yusuf.boyut)

hasan = Dusman(150,75.5,"buyuk","Hasan",50)

print("Dusman sınıfından nesne Hasan : ",type(hasan))
print("Hasan ismi :",hasan.ismi)
print("Hasan canı :",hasan.can)
print("Hasan hasarı :",hasan.hasar)

sozluk1 = {"numara" : 1, "renk" : "kirmizi", "sehir" : "Istanbul"}
sozluk2 = {"isim" : "Ahmet", "yas" : 30, "meslek" : "muhendis"}

yusuf.selam_ver()
hasan.selam_ver()
