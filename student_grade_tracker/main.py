import storage
import roster
import grades
import analytics

students = []
courses = []
notbooklet = {}
settings = {}

''' # __pycache__ klasörünün oluşmasını engellemek için:
import sys
sys.dont_write_bytecode = True 
veya
@echo off
python '-B' main.py
pause'''

print("\n                  { Student Grade Tracker }")

def main():
    global students, courses, notbooklet, settings
    results = storage.load_state() 
    if results:
        students, courses, notbooklet, settings = results
    while True:
        print("\n{ Student Grade Tracker }")
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
            storage.save_state(students, courses, notbooklet, settings)
            print("Bilgiler kaydedildİ!")
            break
        else:
            print("Yanlış tuşladın.")

def menu_roster():
    while True:
        print("\n[ Öğrenci & Ders Yönetimi ]")
        print("1. Öğrenci Ekle")
        print("2. Ders Ekle")
        print("e. Geri")
        choice = input("Seçim: ").strip().lower()
        if choice == "1":
            stu_num = input("Numara: ")
            stu_name = input("Ad: ")
            roster.add_student(students, {"number": stu_num, "name": stu_name})
        elif choice == "2":
            crs_code = input("Kod: ")
            crs_title = input("Ders Adı: ")
            roster.add_course(courses, {"code": crs_code, "title": crs_title})
        elif choice == "e":
            break
        else:
            print("Yanlış tuşladın.")

def menu_grades():
    while True:
        print("\n{ Not İşlemleri }")
        print("1. Ders Notu Ağırlığını Ayarla")
        print("2. Öğrenci Notu Gir")
        print("e. Ana Menüye Dön")
        choice = input("Seçiminiz: ").strip()
        if choice == '1':
            c_id = input("Ders Kodu: ")
            print("Not ağırlıklarını girin (örn: Ödevler %40, Sınavlar %60)")
            weights_input = input("Ağırlıklar: %")
            try:
                weights = {}
                total_weight = 0
                items = weights_input.split(',')
                index = 0
                list_length = len(items)
                while index < list_length:
                    item = items[index]
                    parts = item.split('%')
                    if len(parts) == 2:
                        val = float(parts[1].strip())
                        weights[parts[0].strip()] = parts[1].strip()
                        total_weight += val
                    index += 1
                if total_weight > 100 or total_weight <= 0:
                    print(f"Hata: Toplam ağırlık 0-100 arasında olmalıdır! (Hesaplanan: %{total_weight})")
                    continue
                scale = {"AA": 90.0, "BB": 80.0, "CC": 70.0, "DD": 60.0, "EE": 50.0, "FF": 0.0}
                weights2_data = {"weights": weights, "scale": scale}
                grades.weights2(settings, c_id, weights2_data)
            except:
                print("Hata: Ağırlık formatı geçersiz.")
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
                grades.rec(notbooklet, c_id, s_num, assessment)
            except ValueError:
                print("Hata: Puan sayısal bir değer olmalıdır.")
        elif choice == 'e':
            break
        else:
            print("Yanlış tuşladın.")

def menu_analytics():
    c_id = input("Ders Kodu: ")
    s_num = input("Öğrenci No: ")
    avg = analytics.calculate_average(notbooklet, settings, c_id, s_num)
    epistle1 = analytics.get_epistle_grade(avg, settings, c_id)
    print(f"Sonuç: Öğrencinin ortalaması {avg:.2f}'dur, harf notu {epistle1}'dur.")

main()

'''main()
except KeyboardInterrupt:
    print("\nProgram kullanıcı tarafından kapatıldı.") '''