import storage
import grades
import analytics
import roster 

#Global Değişkenler
STUDENTS = []
COURSES = []
NOTBOOKLET = {}
SETTINGS = {}

'''
def: Tanımlamaya başladığımızı belirtir.
fonksiyon_adi: Fonksiyona verdiğiniz addır.
(...): Fonksiyonun çalışması için gereken bilgileri (argümanlar/parametreler) içeren yerdir. Hiçbir girdi gerekmeyen fonksiyonlar için boş bırakılabilir.
: (İki nokta üst üste): Fonksiyon başlığının bittiğini ve kod bloğunun başladığını belirtir.
Girinti (Indentation): Fonksiyona ait tüm kod satırları girintili olmalıdır.

Fonksiyon Türü,Açıklama
Geri Değer Döndüren,Bir hesaplama yapar ve sonucu dışarıya verir.
Geri Değer Döndürmeyen (Prosedür),Bir görevi yerine getirir ancak bir sonuç üretmez.

def karesini_al(sayi):
    """Verilen sayının karesini hesaplar ve döndürür."""
    karesi = sayi * sayi
    return karesi
sonuc = karesini_al(5)
print(sonuc) # Çıktı: 25
'''
print("      { Student Grade Tracker }")

def main():
    while True:
        print("   { ANA MENÜ }")
        print("1. Öğrenci & Ders Yönetimi")
        print("2. Not İşlemleri")
        print("3. Analiz & Rapor")
        print("e. Çıkış")
        
        choice = input("Seçiminiz: ").strip().lower()
        
        if choice == '1':
            menu_roster()
        elif choice == '2':
            menu_grades()
        elif choice == '3':
            menu_analytics()
        elif choice == 'e':
            storage.save("data", STUDENTS, COURSES, NOTBOOKLET, SETTINGS)
            print("Tüm bilgiler kaydedildi. Tekrar görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim lütfen tekrar deneyin.")

def menu_grades():
    while True:
        print("   { Not İşlemleri }")
        print("1. Ders Notu Ağırlığını Ayarla")
        print("2. Öğrenci Notu Gir")
        print("e. Ana Menüye Dön")
        choice = input("Seçiminiz: ").strip 

        if choice == '1':
            c_id = input("Ders Kodu: % ")
            print("Not ağırlıklarını girin (örn: Ödevler %40, Sınavlar %60)")
            weights_input = input("Ağırlıklar: ")
            
            try: #if: yazılmıyor.
                weights = {}
                items = weights_input(',')
                
                index = 0
                list_length = len(items)
                while index < list_length:
                    item = items[index]
                    parts = item('%') # pyright: ignore[reportUndefinedVariable]
                    
                    index += 1
                scale = {
                    "AA": 90.0, 
                    "BB": 80.0, 
                    "CC": 70.0, 
                    "DD": 60.0, 
                    "EE": 50.0, 
                    "FF": 0.0
                }
                weights2 = {"weights": weights, "scale": scale}
                
                grades.weights2(SETTINGS, c_id, weights2)
            except:
                print("Hata: Ağırlık kodu geçersiz. Lütfen 'Kategori %Sayı, Kategori2 %Sayı2' şeklinde kullanın.")
#c_di, s_num, a_name, a_category
        elif choice == '2':
            c_id = input("Ders Kodu: ")
            s_num = input("Öğrenci Numarası: ")
            a_name = input("Değerlendirme İsmi (örn: Ödev 1): ")
            a_category = input("Kategori (örn: Ödevler): ")
            try:
                a_score = float(input("Puan (0-100): "))
                if not 0 <= a_score <= 100:
                    print("Hata: Puan 0-100 arasında olmalıdır.")
                    continue 
                    
                assessment = {"name": a_name, "category": a_category, "score": a_score}
                grades.rec(NOTBOOKLET, c_id, s_num, assessment)
            except ValueError:
                print("Hata: Puan sayısal bir değer olmalıdır.")

        elif choice == 'e': #else choice yazılmıyor.
            break
'''
. data/ klasörünün mantığı: Uygulama kapansa bile girilen tüm öğrenci listelerini,
ders tanımlamalarını, not politikalarını ve en önemlisi notları diskte saklamaktır.
Program her başladığında, storage.load_state() bu JSON dosyalarını okur ve verileri tekrar Python sözlüklerine ve listelerine yükler.
Program her kapandığında, storage.save_state() bu bellek içi (in-memory) verileri diske kaydeder.
'''

def menu_analytics():
    return
menu_analytics()

def menu_storage():
    return
menu_storage()

def menu_roster():
    return
menu_roster()