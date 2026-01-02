def hesap_makinesi(sayi1,sayi2,islem_turu):
    if islem_turu == "+":
        return sayi1 + sayi2
    elif islem_turu == "-":
        return sayi1 - sayi2
    elif islem_turu == "*":
        return sayi1 * sayi2
    elif islem_turu == "/":
        if sayi2 != 0:
            return sayi1 / sayi2
        else:
            return "Hata: Bir sayı sıfıra bölünemez."
    else:
        return "Hata: Geçersiz işlem türü."
    
    
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem_turu = input("Yapmak istediğiniz işlemi girin (+, -, *, /): ")

sonuc = hesap_makinesi(sayi1, sayi2, islem_turu)
print("Sonuç: ", sonuc)
    
    
