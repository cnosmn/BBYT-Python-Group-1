ilk_program = "ilk program"
print(ilk_program)
print(type("merhaba"))
# python da ekrana yazı yazdırma kodu

tam_sayi = 10  
print(tam_sayi)
print("tam_sayı değeri : ",tam_sayi)
print(type(tam_sayi))

ondalikli_sayi = 10.5
print("ondalikli_sayi değeri : ",ondalikli_sayi)
print(type(ondalikli_sayi))

dogru = True
print("dogru değeri : ",dogru)
print(type(dogru))

# Değişken isimlendirme kuralları
# 1. Değişken isimleri harf veya _ ile başlamalıdır.
# 2. Değişken isimleri sayısal karakter ile başlayamaz.
# 3. Değişken isimleri boşluk içeremez.
# 4. Değişken isimleri özel karakter içeremez. ( _ hariç )
# 5. Değişken isimleri büyük/küçük harf duyarlıdır.
# 6. Değişken isimleri python anahtar kelimeleri ile aynı olamaz.

# ileri veri türleri

# liste
ogrenciler = ["osman","yusuf","mehmet"]

# liste özellikleri
# 1. Sıralıdır. 
# 2. Değiştirilebilir.
# 3. Farklı veri türlerini içerebilir.
# 4. Yinelenen elemanları içerebilir.

print("0 index değeri : ",ogrenciler[0])
print(type(ogrenciler))

yusuf = ["yusuf",20,True,[10,5]]

print(yusuf[3][0])

# demet (tuple)
demet = ("osman","yusuf","mehmet","yusuf")

# demet özellikleri
# 1. Sıralıdır.
# 2. Değiştirilemez.
# 3. Farklı veri türlerini içerebilir.
# 4. Yinelenen elemanları içerebilir.

print(demet)
print("0 index değeri : ",demet[0])
print(type(demet))

# kümeler (set)
kume = {"osman","yusuf","mehmet","yusuf"}
print(kume)
print(type(kume))

# küme özellikleri
# 1. Sırasızdır.
# 2. Değiştirilebilir.
# 3. Farklı veri türlerini içerebilir.  
# 4. Yinelenen elemanları içermez.

# sözlük (dictionary)
sozluk = { "ad":"osman", "yas":20, "bekar_mi":True , "arkadaslar":["yusuf","mehmet"] }
print(sozluk)
print(type(sozluk))
print(sozluk["arkadaslar"][0])


