n = int(input("Bir sıra numarası girin : "))

sayi1 = 0
sayi2= 1

if n == 1:
    print(sayi1)

elif n == 2:
    print(sayi1," ",sayi2)

else:
    for i in range(n):
        temp = sayi1 # 0 1 1
        sayi1= sayi2 # 1 1 2
        sayi2 = temp + sayi2 # 1 2 3
        print(sayi2)
        
""" 
--döngü yok--
sayi1 = 0
sayi2 = 1   

i = 0
sayi1 = 1
sayi2 = 1

i = 1
sayi1 = 1
sayi2 = 2

i = 2
sayi1 = 2
sayi2 = 3
"""

