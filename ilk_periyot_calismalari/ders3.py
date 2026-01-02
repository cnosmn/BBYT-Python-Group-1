# palindrom sayı bulma algoritması 

# 12321

# kullancıdan sayı al
# basamak sayısı 5 olsun
# birler,onlar,binler,onbinler basamaklarındaki değerleri bul ve değişkenlere ata
# sayının birler basamağındaki değer ile onbinler basamağındaki değeri karşılaştır
# sayının onlar basamağındaki değer ile binler basamağındaki değeri karşılaştır
# eğer her iki karşılaştırma da doğru ise sayı palindromdur değilse palindrom değildir.


# Döngüler 

# for döngüsü
# başlangıç,bitis,artış

sayac = 5
for sayac in range(1,11,1):
    print(sayac)
    
print("ortadaki sayac : ",sayac)

for sayac in range(10,0,-1):
    print(sayac)
    
# while döngüsü
parametre = 1
while parametre <= 10:
    print(parametre)
    parametre += 1  # parametre = parametre + 1
    

# for ve while döngüsü örnekleri
# 1 den 100 e kadar olan sayıların toplamını bulun

toplam = 0
for i in range(1,101):
    toplam += i
    
print("Toplam : ",toplam)

toplam2 = 0 
baslangic = 1
while baslangic <= 100:
    toplam2 = toplam2 + baslangic
    baslangic += 1
    
    
dizi = [10,20,30,40,50]

for eleman in dizi:
    print(eleman)
    
for i in dizi:
    if i>20 :
        print(i)


