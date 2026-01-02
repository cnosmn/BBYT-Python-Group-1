# Operatörler

# atama operatörü
sayi = 10 

# matematiksel operatörler
print("Toplama : ",sayi + 5)
print("Çıkarma : ",sayi - 5)
print("Çarpma : ",sayi * 5)
print("Bölme : ",sayi / 5)
print("Tam Bölme : ",sayi // 3)
print("Üs Alma : ",sayi ** 2)

print("Mod Alma : ",sayi % 3)


# mantıksal operatörler
dogru = True 
yanlis = False

# == eşit mi
# != eşit değil mi

print(dogru == yanlis)
print(dogru != yanlis)

# kucuktur <
# kucuk_esittir <=
# buyuktur >
# buyuk_esittir >=

print(5 < 10)
print(5 <= 10)
print(5 > 10)
print(5 >= 10)

# and (ve)   ve or (ya da)  ve not (değil)
print("and çıktısı : ", dogru and yanlis)
print("or çıktısı : ",dogru or yanlis)

kosul = input("Bir sayı giriniz : ")  # "5"
kosul = int(kosul)  # "5" -> 5

print(kosul >10 and kosul <20)
degisken = 5
# değişken isimlendirme kuralları
# 1. Değişken isimleri harf veya _ ile başlamalıdır.
# 2. türkçe karakter kullanılmaz.
# 3. boşluk içeremez.
# 4. özel karakter içeremez. ( _ hariç )
# 5 python özel kelimeleri ile aynı olamaz.

ondaliklisayi = 10.5
ondalikliSayi = 10.5

