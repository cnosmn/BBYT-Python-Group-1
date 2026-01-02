
# fonksiyon türleri
# parametresiz, dönüşümsüz
# parametreli, dönüşümsüz
# parametresiz, dönüşümlü
# parametreli, dönüşümlü

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
print(parametreli_donusumlu_fonksiyon(10,20))


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

print("kullanıcı sayısı : ",kullanici_sayisi)

fibonacci_fonksiyonu(kullanici_sayisi)

