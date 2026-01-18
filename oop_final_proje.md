# Restoran Sipariş Yönetim Sistemi - Proje Senaryosu

## Genel Bakış
bir restoranın günlük operasyonlarını yöneten kapsamlı bir sistem geliştirilecek. Bu sistem menü yönetimi, masa takibi, sipariş alma, personel yönetimi ve hesap hesaplama modüllerini içerecek.

---

## Proje Senaryosu

### Arka Plan Hikayesi
"Lezzet Durağı" adında orta ölçekli bir restoran, tüm operasyonlarını dijitalleştirmek istiyor. Restoran sahibi Bay Mehmet, siparişlerin karışmasından, hesap hatalarından ve stok takibindeki zorluklardan şikayetçi. Sizden restoranın tüm süreçlerini yönetecek bir sistem geliştirmenizi istiyor.

### Sistem Gereksinimleri

#### 1. Menü Yönetimi
- Restoranda farklı kategorilerde ürünler bulunuyor:
  - **Ana Yemekler**: Et yemekleri, tavuk yemekleri, deniz ürünleri
  - **Başlangıçlar**: Çorbalar, salatalar, mezeler
  - **İçecekler**: Soğuk içecekler, sıcak içecekler, alkollü içecekler
  - **Tatlılar**: Sıcak tatlılar, soğuk tatlılar
  
- Her ürünün özellikleri:
  - Ürün adı
  - Fiyat
  - Hazırlanma süresi (dakika)
  - Kalori bilgisi
  - İçerik/malzemeler listesi
  - Mevcut durumu (stokta var/yok)

#### 2. Masa Yönetimi
- Restoranda 20 masa var
- Her masanın özellikleri:
  - Masa numarası
  - Kapasite (2, 4, 6, 8 kişilik)
  - Durum (boş, dolu, rezerve, temizleniyor)
  - Şu anki müşteri sayısı
  - Açılış zamanı (masa ne zaman doldu)

#### 3. Sipariş Sistemi
- Garson bir masaya sipariş alır
- Sipariş özellikleri:
  - Sipariş numarası (otomatik artan)
  - Masa numarası
  - Sipariş tarihi ve saati
  - Sipariş kalemleri (ürünler ve adetleri)
  - Sipariş durumu (hazırlanıyor, hazır, servise çıktı, tamamlandı)
  - Özel notlar (örn: "Az tuzlu olsun", "Alerjisi var")
  - Sorumlu garson

#### 4. Personel Yönetimi
Restoranda üç tip personel var:

- **Garson**:
  - Sipariş alır
  - Servis yapar
  - Sorumlu olduğu masa sayısı takibi
  - Aldığı toplam sipariş sayısı
  - Bahşiş tutarı
  
- **Aşçı**:
  - Siparişleri hazırlar
  - Uzmanlık alanı (Ana yemek, tatlı, başlangıç)
  - Hazırladığı yemek sayısı
  - Aktif sipariş sayısı
  
- **Kasa Görevlisi**:
  - Hesap keser
  - Ödeme alır (Nakit, Kredi Kartı, Yemek Kartı)
  - Günlük kasa raporu
  - İskonto/indirim uygulama yetkisi

Tüm personelin ortak özellikleri:
- Personel ID
- Ad Soyad
- Çalışma saatleri
- Maaş bilgisi (private)
- İletişim bilgileri

#### 5. Hesap Hesaplama Sistemi
Bir masa hesabı kesilirken:
- Tüm sipariş kalemleri toplanır
- KDV hesaplanır (%20)
- Servis ücreti eklenir (%10)
- İndirim/kupon varsa uygulanır
- Toplam tutar hesaplanır
- Ödeme şekline göre işlem yapılır

İndirim tipleri:
- Yüzde bazlı indirim (örn: %15)
- Sabit tutar indirimi (örn: 50 TL)
- "2 al 1 öde" kampanyaları
- Öğrenci indirimi
- Sadakat kartı indirimi

---

## Sınıf Diyagramı

```
┌─────────────────────────────────────────────────────────────┐
│                    <<abstract>>                              │
│                      MenuUrun                                │
├─────────────────────────────────────────────────────────────┤
│ - urun_id: int                                              │
│ - ad: str                                                   │
│ - fiyat: float (private)                                    │
│ - hazirlanma_suresi: int                                    │
│ - kalori: int                                               │
│ - malzemeler: list                                          │
│ - stokta_var: bool                                          │
├─────────────────────────────────────────────────────────────┤
│ + __init__(ad, fiyat, hazirlanma_suresi, kalori)          │
│ + get_fiyat(): float                                        │
│ + set_fiyat(yeni_fiyat): void                              │
│ + bilgileri_goster(): str                                   │
│ + <<abstract>> hazirlanma_mesaji(): str                     │
│ + stok_durumunu_guncelle(durum): void                      │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
         ┌──────────────────┼──────────────────┬──────────────┐
         │                  │                  │              │
┌────────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   AnaYemek     │  │  Baslangic   │  │   Icecek     │  │    Tatli     │
├────────────────┤  ├──────────────┤  ├──────────────┤  ├──────────────┤
│ - et_turu: str │  │ - tip: str   │  │ - sicaklik:  │  │ - tatli_turu:│
│ - pisirme:str  │  │              │  │   str        │  │   str        │
│ - porsiyon:str │  │              │  │ - hacim: int │  │ - porsiyon:  │
│                │  │              │  │              │  │   str        │
├────────────────┤  ├──────────────┤  ├──────────────┤  ├──────────────┤
│ + hazirlanma_  │  │ + hazirlanma_│  │ + hazirlanma_│  │ + hazirlanma_│
│   mesaji():str │  │   mesaji():  │  │   mesaji():  │  │   mesaji():  │
│                │  │   str        │  │   str        │  │   str        │
└────────────────┘  └──────────────┘  └──────────────┘  └──────────────┘


┌─────────────────────────────────────────────────────────────┐
│                         Masa                                 │
├─────────────────────────────────────────────────────────────┤
│ - masa_no: int                                              │
│ - kapasite: int                                             │
│ - durum: str                                                │
│ - musteri_sayisi: int                                       │
│ - acilis_zamani: datetime                                   │
├─────────────────────────────────────────────────────────────┤
│ + __init__(masa_no, kapasite)                              │
│ + masa_ac(musteri_sayisi): void                            │
│ + masa_kapat(): void                                        │
│ + durum_degistir(yeni_durum): void                         │
│ + masa_bilgisi(): str                                       │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                      SiparisKalemi                           │
├─────────────────────────────────────────────────────────────┤
│ - urun: MenuUrun                                            │
│ - adet: int                                                 │
│ - ozel_not: str                                             │
├─────────────────────────────────────────────────────────────┤
│ + __init__(urun, adet, ozel_not)                           │
│ + toplam_fiyat(): float                                     │
│ + kalemi_goster(): str                                      │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                        Siparis                               │
├─────────────────────────────────────────────────────────────┤
│ - siparis_no: int (static counter)                         │
│ - masa_no: int                                              │
│ - siparis_zamani: datetime                                  │
│ - kalemler: list<SiparisKalemi>                            │
│ - durum: str                                                │
│ - sorumlu_garson: Garson                                    │
├─────────────────────────────────────────────────────────────┤
│ + __init__(masa_no, garson)                                │
│ + kalem_ekle(urun, adet, not): void                        │
│ + kalem_cikar(urun): void                                   │
│ + siparis_toplami(): float                                  │
│ + durum_guncelle(yeni_durum): void                         │
│ + siparis_detayi(): str                                     │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                    <<abstract>>                              │
│                      Personel                                │
├─────────────────────────────────────────────────────────────┤
│ - personel_id: int                                          │
│ - ad_soyad: str                                             │
│ - telefon: str                                              │
│ - maas: float (private)                                     │
│ - calisma_saatleri: str                                     │
├─────────────────────────────────────────────────────────────┤
│ + __init__(ad_soyad, telefon, maas)                        │
│ + get_maas(): float                                         │
│ + bilgileri_goster(): str                                   │
│ + <<abstract>> gorev_yap(): str                            │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
┌────────────────┐  ┌──────────────┐  ┌──────────────────┐
│    Garson      │  │     Asci     │  │  KasaGorevlisi   │
├────────────────┤  ├──────────────┤  ├──────────────────┤
│ - sorumlu_masa │  │ - uzmanlik:  │  │ - gunluk_kasa:   │
│   _sayisi: int │  │   str        │  │   float          │
│ - toplam_      │  │ - hazirlanan │  │ - kesilen_       │
│   siparis: int │  │   _yemek:int │  │   hesap_sayisi:  │
│ - bahsis:float │  │ - aktif_     │  │   int            │
│                │  │   siparis:int│  │                  │
├────────────────┤  ├──────────────┤  ├──────────────────┤
│ + siparis_al   │  │ + siparis_   │  │ + hesap_kes      │
│   (masa,       │  │   hazirla    │  │   (siparis):     │
│   siparis):    │  │   (siparis): │  │   Hesap          │
│   void         │  │   void       │  │ + odeme_al       │
│ + servis_yap   │  │ + yemek_     │  │   (tutar,tip):   │
│   (): void     │  │   tamamla(): │  │   void           │
│ + bahsis_ekle  │  │   void       │  │ + indirim_       │
│   (tutar):void │  │              │  │   uygula(tip,    │
│ + gorev_yap(): │  │ + gorev_yap()│  │   miktar): float │
│   str          │  │   : str      │  │ + gorev_yap():   │
│                │  │              │  │   str            │
└────────────────┘  └──────────────┘  └──────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                    <<abstract>>                              │
│                      Indirim                                 │
├─────────────────────────────────────────────────────────────┤
│ - aciklama: str                                             │
├─────────────────────────────────────────────────────────────┤
│ + <<abstract>> indirim_hesapla(tutar): float               │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
┌────────────────┐  ┌──────────────┐  ┌──────────────────┐
│YuzdeIndirim    │  │SabitIndirim  │  │ KampanyaIndirim  │
├────────────────┤  ├──────────────┤  ├──────────────────┤
│ - yuzde: int   │  │ - tutar:     │  │ - al: int        │
│                │  │   float      │  │ - ode: int       │
├────────────────┤  ├──────────────┤  ├──────────────────┤
│ + indirim_     │  │ + indirim_   │  │ + indirim_       │
│   hesapla      │  │   hesapla    │  │   hesapla        │
│   (tutar):     │  │   (tutar):   │  │   (tutar):       │
│   float        │  │   float      │  │   float          │
└────────────────┘  └──────────────┘  └──────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                         Hesap                                │
├─────────────────────────────────────────────────────────────┤
│ - siparis: Siparis                                          │
│ - ara_toplam: float                                         │
│ - kdv_orani: float                                          │
│ - servis_ucreti_orani: float                               │
│ - indirim: Indirim                                          │
│ - genel_toplam: float                                       │
│ - odeme_sekli: str                                          │
├─────────────────────────────────────────────────────────────┤
│ + __init__(siparis)                                         │
│ + hesapla(): void                                           │
│ + indirim_uygula(indirim): void                            │
│ + kdv_hesapla(): float                                      │
│ + servis_ucreti_hesapla(): float                           │
│ + odeme_yap(sekil): void                                    │
│ + hesap_detayi(): str                                       │
│ + fis_yazdir(): str                                         │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                      Restoran                                │
├─────────────────────────────────────────────────────────────┤
│ - ad: str                                                   │
│ - masalar: list<Masa>                                       │
│ - menu: list<MenuUrun>                                      │
│ - personeller: list<Personel>                               │
│ - aktif_siparisler: list<Siparis>                          │
│ - gunluk_ciro: float                                        │
├─────────────────────────────────────────────────────────────┤
│ + __init__(ad)                                              │
│ + masa_ekle(masa): void                                     │
│ + menu_urun_ekle(urun): void                               │
│ + personel_ekle(personel): void                            │
│ + masa_durumu_goster(): str                                 │
│ + menu_goster(): str                                        │
│ + siparis_olustur(masa_no, garson): Siparis                │
│ + gunluk_rapor(): str                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## İlişkiler (Relationships)

### Inheritance (Kalıtım)
- `AnaYemek`, `Baslangic`, `Icecek`, `Tatli` → `MenuUrun` sınıfından türer
- `Garson`, `Asci`, `KasaGorevlisi` → `Personel` sınıfından türer
- `YuzdeIndirim`, `SabitIndirim`, `KampanyaIndirim` → `Indirim` sınıfından türer

### Composition (Bileşim - Has-A)
- `Siparis` **has-a** `SiparisKalemi` listesi
- `SiparisKalemi` **has-a** `MenuUrun`
- `Hesap` **has-a** `Siparis`
- `Hesap` **has-a** `Indirim`
- `Restoran` **has-a** `Masa`, `MenuUrun`, `Personel`, `Siparis` listeleri

### Association (İlişki)
- `Siparis` **associated with** `Garson` (sorumlu garson)
- `Siparis` **associated with** `Masa` (masa numarası ile)

---

## Projenin Aşamalı Geliştirilmesi

### Hafta 1: Temel Sınıflar ve Inheritance
- `MenuUrun` abstract sınıfı ve alt sınıfları
- `Personel` abstract sınıfı ve alt sınıfları
- Basit test senaryoları

### Hafta 2: Sipariş Sistemi
- `Masa`, `SiparisKalemi`, `Siparis` sınıfları
- Sipariş oluşturma ve yönetme
- Garson-sipariş ilişkisi

### Hafta 3: Hesap ve İndirim Sistemi
- `Indirim` abstract sınıfı ve alt sınıfları
- `Hesap` sınıfı ve hesaplama mantığı
- Farklı ödeme şekilleri

### Hafta 4: Ana Sistem ve Raporlama
- `Restoran` ana sınıfı
- Tüm sistemin entegrasyonu
- Raporlama ve istatistikler
- Kullanıcı arayüzü (konsol tabanlı menü sistemi)

---

## Örnek Kullanım Senaryoları

### Senaryo 1: Yeni Müşteri Gelişi
1. Garson boş masa kontrol eder
2. 4 kişilik müşteri için 5 numaralı masayı açar
3. Sipariş alır (2 ana yemek, 4 içecek, 1 başlangıç)
4. Sipariş mutfağa gönderilir

### Senaryo 2: Sipariş Hazırlama
1. Aşçı aktif siparişleri görüntüler
2. Uzmanlık alanına göre sipariş hazırlar
3. Sipariş durumunu "hazır" olarak işaretler
4. Garson servise çıkarır

### Senaryo 3: Hesap Kesme
1. Müşteri hesap ister
2. Kasa görevlisi sipariş toplamını hesaplar
3. KDV ve servis ücreti ekler
4. %15 sadakat indirimi uygular
5. Kredi kartı ile ödeme alır
6. Fiş yazdırır
7. Masa temizleniyor durumuna geçer

---

## Değerlendirme Kriterleri

### Teknik Kriterler (60%)
- ✓ Abstract sınıflar doğru tanımlanmış mı?
- ✓ Inheritance doğru kullanılmış mı?
- ✓ Encapsulation uygulanmış mı? (private değişkenler, getter/setter)
- ✓ Polymorphism örnekleri var mı?
- ✓ Kod düzgün yorumlanmış mı?

### Fonksiyonellik (30%)
- ✓ Sistem çalışıyor mu?
- ✓ Hata yönetimi var mı?
- ✓ Tüm özellikler implement edilmiş mi?

### Yaratıcılık ve Ekstralar (10%)
- ✓ Ekstra özellikler eklenmiş mi?
- ✓ Kullanıcı dostu arayüz var mı?
- ✓ Raporlama sistemi geliştirilmiş mi?

---

## Bonus Özellik Önerileri

Öğrenciler temel sistemi bitirdikten sonra ekleyebilecekleri:
- 📊 Günlük/haftalık satış grafikleri
- 🎯 En çok satan ürün analizi
- 👨‍🍳 Personel performans değerlendirmesi
- 📱 Masa QR kod sistemi
- ⭐ Müşteri puanlama sistemi
- 🍕 Ürün kombinasyon önerileri
- 💾 Dosyaya kaydetme/yükleme (pickle veya JSON)