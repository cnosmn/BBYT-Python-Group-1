
def kelime_sayisi(cumle):
    sayac = 1
    for i in cumle:
        if i == " ":
            sayac += 1
    return sayac


cumle = input("Bir cümle giriniz: ")

kelime_sayisi_sonuc = kelime_sayisi(cumle)
print("Cümledeki kelime sayısı:", kelime_sayisi_sonuc)

"""
merhaba dünya

"""
