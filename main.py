import storage
import grades
import analytics
import pprint
import roster

# Global değişkenler
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
Geri Değer Döndüren,Bir hesaplama yapar ve sonucu dışarıya verir. (Örn: grades.calculate_student_average)
Geri Değer Döndürmeyen (Prosedür),Bir görevi yerine getirir ancak bir sonuç üretmez. (Örn: roster.add_student gibi bir şeyi ekrana yazdıran fonksiyonlar)

def karesini_al(sayi):
    """Verilen sayının karesini hesaplar ve döndürür."""
    karesi = sayi * sayi
    return karesi
sonuc = karesini_al(5)
print(sonuc) # Çıktı: 25
'''

def _menu_grades():
    while True:
        print("   { Not İşlemleri }")
        print("1. Ders Not Politikasını Ayarla (Ağırlık/Skala)")
        print("2. Öğrenci Notu Gir")
        print("e. Ana Menüye Dön")
        choice = input("Seçiminiz: ").strip()

        if choice == '1':
            c_id = input("Ders Kodu: % ")
            print("Not ağırlıklarını girin (örn: Ödevler %40, Sınavlar %60)")
            weights_input = input("Ağırlıklar: ")
            
            try: #if: yazılmıyor.
                weights = {}
                items = weights_input.split(',')
                
                index = 0
                list_length = len(items)
                while index < list_length:
                    item = items[index]
                    parts = item.split('%')
                    
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = float(parts[1].strip()) / 100.0
                        weights[key] = value
                    else:
                        raise ("Format hatası")
                    
                    index += 1
                scale = {
                    "AA": 90.0, 
                    "BB": 80.0, 
                    "CC": 70.0, 
                    "DD": 60.0, 
                    "EE": 50.0, 
                    "FF": 0.0
                }
                policy = {"weights": weights, "scale": scale}
                
                grades.set_grade_policy(SETTINGS, c_id, policy)
            except (ValueError, IndexError):
                print("Hata: Ağırlık formatı geçersiz. Lütfen 'Kategori %Sayı, Kategori2 %Sayı2' formatını kullanın.")
#c_di, s_num, a_name, a_category
        elif choice == '2':
            c_id = input("Ders Kodu: ")
            s_num = input("Öğrenci Numarası: ")
            a_name = input("Değerlendirme Adı (örn: Ödev 1): ")
            a_category = input("Kategori (örn: Ödevler): ")
            try:
                a_score = float(input("Puan (0-100): "))
                if not 0 <= a_score <= 100:
                    print("Hata: Puan 0-100 arasında olmalıdır.")
                    continue 
                    
                assessment = {"name": a_name, "category": a_category, "score": a_score}
                grades.record_grade(NOTBOOKLET, c_id, s_num, assessment)
            except ValueError:
                print("Hata: Puan sayısal olmalıdır.")

        elif choice == 'e': #else choice de yazılmıyor.
            break
'''
. data/ klasörünün mantığı: Uygulama kapansa bile girilen tüm öğrenci listelerini,
ders tanımlamalarını, not politikalarını ve en önemlisi notları diskte saklamaktır.
Program her başladığında, storage.load_state() bu JSON dosyalarını okur ve verileri tekrar Python sözlüklerine ve listelerine yükler.
Program her kapandığında, storage.save_state() bu bellek içi (in-memory) verileri diske kaydeder.

Dosya Adı,Sakladığı Veri,Formatı (Mantığı)
students.json,Tüm öğrenci profilleri.,"Liste (List): Her öğe bir öğrenciyi temsil eden bir Sözlüktür (Dict). 
(Örn: [{""num"": ""101"", ""name"": ""Ali Yılmaz"", ""email"": ""a@mail.com""}, ...])"

courses.json,Tüm ders tanımlamaları.,"Liste (List): Her öğe dersi ve ona kayıtlı öğrencileri temsil eden bir Sözlüktür. 
(Örn: [{""num"": ""CS101"", ""baslık"": ""Giriş"", ""students"": [""101"", ""102""]}, ...])"

settings.json,Not politikaları ve ayarlar.,"Sözlük (Dict): Anahtarlar ders kodlarıdır. Değerler o derse ait ağırlık ve harf notu skalasını içerir. 
(Örn: {""CS101"": {""weights"": {""Odevler"": %40 ...}, ""scale"": {""AA"": 90.0, ...}}})"

gradebook.json,Tüm notların kaydı.,"İç İçe Sözlük (Nested Dict): Bu, en karmaşık yapıdır. Ders kodu ile başlar, ardından öğrenci numarası gelir 
ve en içte o öğrencinin o dersteki notlarının listesi bulunur. 
(Örn: {""CS101"": {""101"": [{""name"": ""Sınav 1"", ""score"": 85.0, ...}, ...]}})"
'''

def _menu_analytics():
    while True:
        print("   { Analiz & Raporlama }")
        print("1. En Başarılı Öğrenciler (Top Performers)")
        print("2. Not Dağılımı")
        print("e. Ana Menüye Dön")
        choice = input("Seçiminiz: ").strip()

        if choice == '1':
            c_id = input("Ders Kodu: ")
            limit_input = input("Kaç öğrenci gösterilsin? (örn: 5): ").strip()
            limit = int(limit_input) if limit_input else 5
            report = analytics.top_performers(NOTBOOKLET, SETTINGS, c_id, limit)
            print(f"*** {c_id} En Başarılı {limit} Öğrenci ***")
            pprint.pprint(report)
            
        elif choice == '2':
            c_id = input("Ders Kodu: ")
            report = analytics.grade_distribution(NOTBOOKLET, SETTINGS, c_id)
            print(f"*** {c_id} Not Dağılımı ***")
            pprint.pprint(report)
            
        elif choice == 'e':
            break

def main():
    
    '''
    STUDENTS, COURSES, NOTBOOKLET, SETTINGS = storage.load_state()
    
    print("="*40)
    print("Öğrenci Not Takip Sistemi 1.0")
    '''

    while True:
        print("   { ANA MENÜ }")
        print("1. Öğrenci & Ders Yönetimi")
        print("2. Not İşlemleri (Notlar)")
        print("3. Analiz & Raporlama")
        print("e. Çıkış")
        
        choice = input("Seçiminiz: ").strip().lower()
        
        if choice == '1':
            _menu_roster()
        elif choice == '2':
            _menu_grades()
        elif choice == '3':
            _menu_analytics()
        elif choice == 'e':
            storage.save_state("data", STUDENTS, COURSES, NOTBOOKLET, SETTINGS)
            print("Tüm bilgiler kaydedildi. Tekrar görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()