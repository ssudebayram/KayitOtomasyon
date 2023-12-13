class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

class OgrenciKayit:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        print(f"{ogrenci.ad} {ogrenci.soyad} adlı öğrenci kaydedildi.")

    def ogrenci_listele(self):
        if not self.ogrenciler:
            print("Kayıtlı öğrenci bulunmamaktadır.")
        else:
            print("Kayıtlı Öğrenciler:")
            for ogrenci in self.ogrenciler:
                print(f"{ogrenci.ad} {ogrenci.soyad} - Numara: {ogrenci.numara}")

ogrenci_kayit_sistemi = OgrenciKayit()

while True:
    print("\n1. Öğrenci Ekle")
    print("2. Kayıtlı Öğrencileri Listele")

    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3): ")

    if secim == "1":
        ad = input("Öğrenci adını girin: ")
        soyad = input("Öğrenci soyadını girin: ")
        numara = input("Öğrenci numarasını girin: ")

        ogrenci = Ogrenci(ad, soyad, numara)
        ogrenci_kayit_sistemi.ogrenci_ekle(ogrenci)

    elif secim == "2":
        ogrenci_kayit_sistemi.ogrenci_listele()

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
