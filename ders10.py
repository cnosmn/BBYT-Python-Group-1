
import json
# PYTHON DOSYA İŞLEMLERİ

# Dosya açma modları
# 'r' : Okuma modu (varsayılan)
# 'w' : Yazma modu (varsa üzerine yazar, yoksa oluşturur)
# 'a' : Ekleme modu (varsa sonuna ekler, yoksa oluşturur)
# 'x' : özel oluşturma modu (dosya zaten varsa hata verir)
# 'r+' : Okuma ve yazma modu
# 'b' : İkili (binary) modu


# en basit dosya okuma örneği

dosya = open("database.txt", "r", encoding="utf-8")  # Dosyayı okuma modunda aç
icerik = dosya.read()  # Dosyanın tüm içeriğini oku
print(icerik)  # İçeriği ekrana yazdır
print(type(icerik))  # İçeriğin türünü yazdır
dosya.close()  # Dosyayı kapat


# güvenli dosya işlemi (with kullanımı)
with open("database.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)
    # buradan sonra dosya otomatik kapanacaktır.

# dosyaya yazma işlemi
with open("yeni_dosya.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba Dünya!\n")
    dosya.write("Python dosya işlemleri öğreniyorum.\n")
    dosya.write("Dosyaya yazma işlemi başarılı.\n")


with open("yeni_dosya.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Bu satır ekleme modunda eklendi.\n")


# dosya var mı yok mu kontrol eden fonksiyon

def dosya_var_mi(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            return True
    except FileNotFoundError:
        return False
    
print(dosya_var_mi("database.txt"))  # True
print(dosya_var_mi("olmayan_dosya.txt"))  # False




# JSON dosya işlemleri
veri = [
    {
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "beceriler": ["Python", "Java", "C++"]
},
{
    "ad": "Ayşe",
    "soyad": "Kara",
    "beceriler": ["JavaScript", "HTML", "CSS"]
},
{
    "ad": "Mehmet",
    "soyad": "Demir",
    "beceriler": ["Java", "Spring", "Hibernate"]
}
]
# JSON dosyasına yazma
# with open("database.json", "w", encoding="utf-8") as json_dosya:
#     json.dump(veri, json_dosya, ensure_ascii=False, indent=4)

def veri_kaydet(dosya_adi, veri, mode="w"):
    with open(dosya_adi, mode, encoding="utf-8") as json_dosya:
        json.dump(veri, json_dosya, ensure_ascii=False, indent=4)

def veri_oku(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as json_dosya:
        veri = json.load(json_dosya)
        return veri

veri_kaydet("database.json", veri, mode="w")
okunan_veri = veri_oku("database.json")
print(okunan_veri)
print(type(okunan_veri))