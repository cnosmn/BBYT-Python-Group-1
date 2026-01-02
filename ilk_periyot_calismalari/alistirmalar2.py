

def not_ortalamasi(not1,not2,not3):
    ortalama = (not1 + not2 + not3) / 3
    return ortalama

def ogrenci_durumu(dizi):
    toplam = 0
    for puan in dizi:
        toplam += puan
    ortalama = toplam / len(dizi)
    
    return ortalama

def durum_analizi(ortalama):
    if ortalama >= 85:
        return "Pekiyi"
    elif ortalama >= 70:
        return "İyi"
    elif ortalama >= 50:
        return "Orta"
    else:
        return "Kötü"
    
notlar = [85, 90, 78, 92, 88]
ortalama = ogrenci_durumu(notlar)

durum = durum_analizi(ortalama)
print("Öğrenci not ortalaması: ", ortalama)
print("Öğrenci durumu: ", durum)


if ortalama >= 50:
    print("Öğrenci durumu: iyi")
else:
    print("Öğrenci durumu: kötü")
    


    