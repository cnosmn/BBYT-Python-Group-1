#Bir String'i Tersine Çevirme recursive fonksiyon ile

# merhaba  [-1] = a
def ters_cevir(s):
    if len(s) == 0:
        return ""
    return s[-1] + ters_cevir(s[:-1]) 

# a + ters_cevir("merhab") 
# a + b + ters_cevir("merha")
# a + b + h + ters_cevir("merh")
# a + b + h + r + ters_cevir("mer")
# a + b + h + r + e + ters_cevir("me")
# a + b + h + r + e + m + ters_cevir("m")
# "a" + "b" + "h" + "r" + "e" + "m" + ""  -> "ahbrem"

print(ters_cevir("python"))
