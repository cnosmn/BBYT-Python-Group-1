# veri türleri
# yorum satırı
# değişkenler
# operatörler
# kullanıcıdan veri alma
# if-elif-else koşulları
# ileri veri yapıları (listeler, demetler, sözlükler)
# döngüler (for, while)
# fonksiyonlar


# fonksiyonlar da args ve kwargs kullanımı

import time

def fonksiyon(a,b):
    return a + b

def fonksiyon2(*args):
    print(args)

fonksiyon2(1,2,3,4,5,6,7,8,9,10)

def fonksiyon3(**kwargs):
    print(kwargs)

fonksiyon3(a=1, b=2, c=3, d=4)

def fonksiyon4(*args, **kwargs):
    print(args)
    toplam = 0
    for i in args:
        toplam = toplam + i
    print("Toplam:", toplam)
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

fonksiyon4(1,2,3, a=4, b=5, c=6,d=8,e=9)

def topla(*args):
    sonuc = 0
    for sayi in args : 
        sonuc += sayi
    return sonuc

print(topla(1,2,3,4))


# recursive fonksiyonlar

start_time = time.time()   # başlangıç zamanı

for i in range(1,11):
    print("süre : ",i," saniye")

finish_time = time.time()  # bitiş zamanı

print("For Dongusu Toplam süre:", finish_time - start_time, "saniye")
print("==========================")

def timer(saniye):
    if saniye > 10 :
        print("süre doldu")
        return
    print("süre : ",saniye," saniye")
    #time.sleep(1)  # 1 saniye bekletir

    return timer(saniye + 1)

# Çalışma süresini ölçme
start_time = time.time()   # başlangıç zamanı
timer(1)
finish_time = time.time()  # bitiş zamanı

print("Recursive Toplam süre:", finish_time - start_time, "saniye")

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

# .pop() dizinin en sonundan eleman çıkarır
# .pop(index) belirtilen indexteki elemanı çıkarır
# verilen sayı dizisinin toplamını yazan fonksiyon

def dizi_toplam(dizi):
    if dizi == []:
        return 0
    eleman = dizi[-1]
    dizi.pop()
    return eleman + dizi_toplam(dizi)

print("dizinin toplamı : ",dizi_toplam([3,5,3,2,6,8,5,6,7,8]))  # 120
