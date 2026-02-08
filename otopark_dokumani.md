Aşağıda **3. Akıllı Otopark Yönetim Otomasyonu** için **tamamen kodsuz**, ancak gerçek bir Python OOP projesi yazacakmış gibi **sınıfları, sorumluluklarını, niteliklerini (attribute)** ve **metotlarını (fonksiyonlarını)** ayrıntılı ve sistematik biçimde açıklıyorum.
Bu anlatım doğrudan **class diyagramı mantığına** karşılık gelir.

---

# AKILLI OTOPARK YÖNETİM OTOMASYONU

**(Nesneye Yönelimli – Kod Yazmadan Tasarım)**

---

## 1. `Arac` (Temel / Soyut Sınıf)

### Sorumluluk

Tüm araç türleri için ortak özellikleri ve davranışları tanımlar.

### Nitelikler (Attributes)

* plaka
* giris_zamani
* cikis_zamani
* park_suresi
* arac_tipi

### Fonksiyonlar (Metotlar)

* **giris_yap()**
  Aracın otoparka giriş zamanını kaydeder.

* **cikis_yap()**
  Aracın çıkış zamanını belirler.

* **park_suresini_hesapla()**
  Giriş ve çıkış zamanına göre park süresini hesaplar.

* **ucret_hesapla()** *(soyut)*
  Her araç türünün kendine göre hesaplayacağı ücret metodudur.

---

## 2. `Otomobil` (Arac → Otomobil)

### Sorumluluk

Standart binek araçları temsil eder.

### Ek Nitelikler

* saatlik_ucret

### Fonksiyonlar

* **ucret_hesapla()**
  Park süresine göre otomobil ücretini hesaplar.

---

## 3. `Motosiklet` (Arac → Motosiklet)

### Sorumluluk

Motosikletleri temsil eder.

### Ek Nitelikler

* indirim_orani

### Fonksiyonlar

* **ucret_hesapla()**
  Daha düşük tarifeye göre ücret hesaplar.

---

## 4. `ElektrikliArac` (Arac → ElektrikliArac)

### Sorumluluk

Elektrikli araçlar ve şarj sürecini yönetir.

### Ek Nitelikler

* sarj_suresi
* sarj_ucreti

### Fonksiyonlar

* **sarj_baslat()**
  Şarj sürecini başlatır.

* **sarj_bitir()**
  Şarj süresini kaydeder.

* **ucret_hesapla()**
  Park + şarj ücretini birlikte hesaplar.

---

## 5. `ParkAlani`

### Sorumluluk

Otoparktaki fiziksel park alanlarını yönetir.

### Nitelikler

* alan_no
* dolu_mu
* park_edilen_arac

### Fonksiyonlar

* **arac_yerlestir(arac)**
  Park alanını dolu olarak işaretler ve aracı atar.

* **arac_cikar()**
  Alanı boşaltır.

* **durum_bilgisi()**
  Alanın dolu/boş durumunu döndürür.

---

## 6. `Otopark`

### Sorumluluk

Tüm sistemi yöneten ana sınıftır.

### Nitelikler

* park_alanlari
* giris_yapan_araclar
* kapasite

### Fonksiyonlar

* **musait_alan_bul()**
  Boş park alanı arar.

* **arac_giris(arac)**
  Aracı sisteme alır ve uygun alana yönlendirir.

* **arac_cikis(plaka)**
  Aracı sistemden çıkarır.

* **doluluk_orani_hesapla()**
  Otopark doluluk oranını hesaplar.

* **otopark_durumu()**
  Genel durumu raporlar.

---

## 7. `Odeme` (Soyutlama / Servis Sınıfı)

### Sorumluluk

Ücretlendirme ve ödeme sürecini yönetir.

### Nitelikler

* toplam_tutar
* odeme_tipi

### Fonksiyonlar

* **ucret_olustur(arac)**
  Araçtan gelen ücreti alır.

* **odeme_al()**
  Ödeme işlemini gerçekleştirir.

* **fatura_olustur()**
  Ödeme sonrası fatura üretir.

---

## 8. `OdemeTipi` (Opsiyonel Genişleme)

### Alt Türler

* Nakit
* KrediKarti
* MobilOdeme

### Fonksiyonlar

* **odeme_yap(tutar)**
  Ödeme yöntemine göre işlem yapar.

---

## 9. `OtoparkRapor`

### Sorumluluk

İstatistik ve raporlama üretir.

### Fonksiyonlar

* **gunluk_gelir_hesapla()**
* **arac_turune_gore_dagilim()**
* **ortalama_park_suresi()**

---

## OOP KAVRAMLARININ NET KULLANIMI

| Kavram        | Nerede Kullanılıyor          |
| ------------- | ---------------------------- |
| Encapsulation | Araç süre ve ücret bilgileri |
| Inheritance   | Arac → Otomobil, Motosiklet  |
| Polymorphism  | ucret_hesapla()              |
| Abstraction   | Odeme, Arac                  |
| Composition   | Otopark → ParkAlani          |
| Aggregation   | Otopark → Arac               |

---

## PROJEYİ GENİŞLETME FİKİRLERİ

* Abonelikli araçlar
* Plaka tanıma entegrasyonu
* Doluluk ekranı
* Mobil uygulama bağlantısı
* Acil durum yönetimi

---

İstersen bir sonraki adımda:

* Bu sistemi **UML diyagramına dönüştürebiliriz**
* Öğrenciler için **adım adım ödevlendirme**
* Ya da bu senaryoya uygun **örnek test senaryoları** hazırlayabilirim
