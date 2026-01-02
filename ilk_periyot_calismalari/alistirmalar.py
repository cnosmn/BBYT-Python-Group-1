sayi = int(input("Bir sayı girin : "))

for i in range(2,sayi):
    if (sayi % i) == 0:
        print(sayi," asal sayı değildir.")
        break


# FİBONACCI SAYILARI 
# 0 1 1 2 3 5 8 13 21 34 55 89 ...

n = int(input("Bir sıra numarası girin : "))
sayi1 = 0
sayi2= 1

if n == 1:
    print(sayi1)

elif n == 2:
    print(sayi1," ",sayi2)

for i in range(n):
    temp = sayi1 
    sayi1= sayi2 
    sayi2 = temp + sayi2
    print(sayi2)
    

# şifre kontrolü
sifre = input("Şifrenizi girin : ")

dogru_sifre = "python123"
hak = 3

for i in range(1,3):
    if sifre == dogru_sifre:
        print("Şifre doğru, giriş yapıldı.")
        break
    else:
        hak -= 1
        print("Şifre yanlış. Kalan hakkınız : ",hak)
        if hak == 0:
            print("Hakkınız bitti, şifreniz bloke oldu.")
            break
        sifre = input("Şifrenizi girin : ")
        
        
        
# çarpım tablosu -iç içe döngüler

for i in range(1,11):
    for j in range(1,11):
        print(i," x ",j," = ",i*j)
    print("***********************")



# break, continue, pass
# if sayi < 10:
#     pass

# def fonksiyon():
#     pass

# Fonksiyonlar

# Fonksiyon türleri
"""
parametresiz, dönüşümsüz
parametreli, dönüşümsüz
parametresiz, dönüşümlü
parametreli, dönüşümlü

"""

# parametresiz dönüşümsüz fonksiyon
def parametresiz_fonksiyon():
    print("Parametresiz fonksiyon çağrıldı.")
    
# parametreli dönüşümsüz fonksiyon
def parametreli_fonksiyon(sayi):
    print("Parametreli fonksiyon çağrıldı.")
    print("Parametre değeri : ",sayi)
    
# parametresiz dönüşümlü fonksiyon
def parametresiz_donusumlu_fonksiyon():
    print("Parametresiz dönüşümlü fonksiyon çağrıldı.")
    return 10

# parametreli dönüşümlü fonksiyon
def parametreli_donusumlu_fonksiyon(sayi1,sayi2):
    print("Parametreli dönüşümlü fonksiyon çağrıldı.")
    return sayi1 + sayi2


parametresiz_fonksiyon()
parametreli_fonksiyon(5)


donusum1 = parametresiz_donusumlu_fonksiyon()
print("Dönüşüm değeri : ",donusum1)
donusum2 = parametreli_donusumlu_fonksiyon(10,20)
print("Dönüşüm değeri : ",donusum2)


# örnek fonsiyon uygulaması

def fibonacci_fonksiyonu(sira_no):
    sayi1 = 0
    sayi2= 1

    if sira_no == 1:
        print(sayi1)

    elif sira_no == 2:
        print(sayi1," ",sayi2)

    else:
        for i in range(sira_no):
            temp = sayi1 # 0 1 1
            sayi1= sayi2 # 1 1 2
            sayi2 = temp + sayi2 # 1 2 3
        print(sayi2)
        
kullanici_sayisi = int(input("kullanıcı sayısını girin : "))
fibonacci_fonksiyonu(kullanici_sayisi)

