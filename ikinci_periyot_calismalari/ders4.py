
class Sut :
    
    def __init__(self,marka,fiyat,miktar,laktoz_orani,tett,yag_orani) :
        self.marka = marka
        self.fiyat = fiyat
        self.miktar = miktar
        self.laktoz_orani = laktoz_orani
        self.tett = tett
        self.yag_orani = yag_orani
    # tett -> "10/10/26" -> ['10','10','26']
    def tuketim_suresi_yaz(self,bugunun_tarihi):
        split_edilmis_tarih = [int(bugunun_tarihi.split('/')[0]),int(bugunun_tarihi.split('/')[1]),int(bugunun_tarihi.split('/')[2])]
        urun_tett = [int(self.tett.split('/')[0]),int(self.tett.split('/')[1]),int(self.tett.split('/')[2])]
        icilebilir_mi = False
        if urun_tett[2] > split_edilmis_tarih[2]:
            icilebilir_mi = True
        elif urun_tett[2] == split_edilmis_tarih[2]:
            if urun_tett[1] > split_edilmis_tarih[1]:
                icilebilir_mi = True
            elif urun_tett[1] == split_edilmis_tarih[1]:
                if urun_tett[0] >= split_edilmis_tarih[0]:
                    icilebilir_mi = True

        if icilebilir_mi :
            print("sut icilebilir")
        else : 
            print("sut icilemez")


sut = Sut(marka="pınar",fiyat=25,miktar="1L",laktoz_orani=2.5,tett="10/01/26",yag_orani=3.5)

sut.tuketim_suresi_yaz(bugunun_tarihi="10/01/26")