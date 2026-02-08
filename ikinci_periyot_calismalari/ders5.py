# Banka Otomasyonu

import random

# 15 basamaklı sayı için alt ve üst sınırlar
alt_sinir = 10**14      # 100000000000000
ust_sinir = 10**15 - 1 # 999999999999999

"""
Müşteri sınıfı olsun
Özellikler : 
isim ,                   -> string
soyisim ,                -> string
tc_kimlik ,              -> string           
dogum_tarihi ,           -> string / Date
bakiye ,                 -> float
iban ,                   -> string
banka_uyelikleri ,       -> list[string]
uyelik(aktif,pasif) ,    -> Bool
borc_miktari             -> float
kalan_kredi_suresi(ay)   -> int 
kredi_limiti             -> float


Fonksiyonlar : 
bilgileri_getir(), 
para_cek() , 
para_yukle() , 
para_aktar() , 
uyelik_sonlandirma() , 
uye_ol() , 
kredi_cek() ,
kredi_odeme(),
bakiye_sorgula(),

"""

class Musteri:

    def __init__(
            self,
            isim,
            soyisim,
            tc_no,
            dogum_tarihi,
            bakiye,
            banka_uyelikleri,
            uyelik,
            borc_miktari,
            kalan_kredi_suresi,
            kredi_limiti,
            musteri_listesi
            ):
        self.isim = isim
        self.soyisim = soyisim
        self.tc_no = tc_no
        self.dogum_tarihi = dogum_tarihi
        self.bakiye = bakiye

        mevcut_ibanlar = {musteri.iban for musteri in musteri_listesi}
        while True :
            iban = random.randint(alt_sinir, ust_sinir)
            if iban not in mevcut_ibanlar :
                self.iban = iban
                break

        self.iban = iban
        self.banka_uyelikleri = banka_uyelikleri
        self.uyelik = uyelik
        self.borc_miktari = borc_miktari
        self.kalan_kredi_suresi = kalan_kredi_suresi
        self.kredi_limiti = kredi_limiti
    
    def bilgileri_getir(self):

        musteri_bilgisi = {
            "isim" : self.isim ,
            "soyisim" : self.soyisim ,
            "tc" : self.tc_no ,
            "dogum_tarihi" : self.dogum_tarihi ,
            "uyelik_durumu" : "aktif" if self.uyelik else "pasif" ,
            "bakiye" : self.bakiye ,
            "iban" : self.iban
        }

        return musteri_bilgisi

    def para_cek(self,miktar):
        if miktar > self.bakiye :
            print("Bakiye Yeterli Değil")
        else :
            self.bakiye = self.bakiye - miktar
            print("İstenilen Miktar çekildi. Güncel Bakiyeniz : ",self.bakiye)
        
    def para_yukle(self,yatirilacak_miktar):
        if yatirilacak_miktar < 0 :
            print("lütfen geçerli bir miktar giriniz!")
        elif yatirilacak_miktar > 20000 :
            print("lütfen azami para yatırma miktarini aşmayınız")
        else : 
            self.bakiye = self.bakiye + yatirilacak_miktar
            print("İstenilen Miktar hesaba aktarıldı. Güncel Bakiyeniz : ",self.bakiye)

    def para_aktar(self,aktarilacak_miktar,iban,isim,soyisim,musteri_dizisi):
        if aktarilacak_miktar < 0 and self.bakiye < aktarilacak_miktar :
            print("lütfen geçerli bir miktar giriniz!")
        else : 
            for musteri in musteri_dizisi:
                if musteri.iban == iban and musteri.isim == isim and musteri.soyisim == soyisim :
                    musteri.bakiye = musteri.bakiye + aktarilacak_miktar 
                    self.bakiye = self.bakiye - aktarilacak_miktar
                    print("Miktar başarılı bir şekilde şu Müşteriye aktarıldı : ", musteri.isim," ",musteri.soyisim)
                    print("Güncel Bakiyeniz : ", self.bakiye)
                    break

    def uyelik_sonlandirma(self):
        if self.uyelik == False : 
            print("Musterinin zaten aktif bir üyeliği bulunmamaktadır")
        else :
            self.uyelik = False
    
    def banka_uyeligi_silme(self,kaldirilacak_banka_ismi):

        if kaldirilacak_banka_ismi in self.banka_uyelikleri :
            self.banka_uyelikleri.remove(kaldirilacak_banka_ismi)
            print("Musterinin Banka uyeliklerinden girilen banka uyeliği başarılı bir şekilde kaldırıldı")
        else :
            print("Girilen banka Müşterinin Uye oldugu bankalarda mevcut değil!")

    def uye_ol(self,banka_ismi):
        if banka_ismi in self.banka_uyelikleri :
            print("Musteri zaten bu girilen bankaya uyedir")
        else :
            self.banka_uyelikleri.append(banka_ismi)
            print("Musterinin bankalar listesine şu banka eklendi : ",banka_ismi)

# Ödev
    def kredi_cek(self,cekilen_miktar,ay,faiz):
        # kredi miktarı
        # ay sayısı
        # faiz 
        # borc_miktari = cekilen_miktar * faiz + cekilen_miktar
        # kalan_kredi_süresi 

        if cekilen_miktar > self.kredi_limiti:
            print("kredi limitinize uygun kredi miktarı giriniz")

        else:
            self.borc_miktari = self.borc_miktari + cekilen_miktar * faiz + cekilen_miktar 
            self.kalan_kredi_suresi = self.kalan_kredi_suresi + ay

            print("Kredi başarıyla çekildi, çekilen miktar : ",cekilen_miktar)
            print("güncellenmiş kalan kredi süresi : ",self.kalan_kredi_suresi, " Ay")

    def borc_odeme(self,miktar,dusulecek_ay):
        # miktar
        # dusulecek_ay
        # kredi_limiti = kredi_limiti + kredi_limiti * 0.03
        if type(miktar) == 'int':
            if miktar > 0  :
                self.borc_miktari = self.borc_miktari - miktar
                self.kalan_kredi_suresi = self.kalan_kredi_suresi - dusulecek_ay
                print("kredi ödemesi başarılı bir şekilde gerçekleşti. ")
                print("güncel borcunuz : ",self.borc_miktari)
                print("kalan ay sayısı : ",self.kalan_kredi_suresi)            
            else:
                print("lütfen geçerli bir miktar giriniz! ")
        else : 
            print("lütfen geçerli bir miktar türü giriniz! ")

    def bakiye_sorgulama(self):
        return self.bakiye
    
    def sinif_fonksiyonu():
        print("bu sınıfın fonksiyonu ve çalışıyor")


musteri1 = Musteri("osman","can","12321312321","03/10/2000",0,["a bankası","b bankası"],True,30000,0,5000,[])
musteri2 = Musteri("yusuf","özkan","12321312321","03/10/2000",2000,["a bankası","b bankası"],True,30000,0,5000,[musteri1])
print("Müsteri 1 in bilgileri : " , musteri1.bilgileri_getir())

musteri_listesi = [musteri1,musteri2]

musteri2.para_aktar(500,"12312312","osman","can",musteri_listesi)
print(musteri1.bakiye)


# ödev 
# aynı ibana sahip başka bir müşteri varsa kayıt olan müşteri için tekrar iban üretilsin