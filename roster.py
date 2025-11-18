from typing import List, Dict

'''
. from typing import
typing: Bu, Python'ın standart kütüphanesinde bulunan bir modüldür. Amacı, Python'a dinamik olarak yazılmış bir dil olmasına rağmen, 
değişkenlere ve fonksiyonlara beklenen veri türlerini belirtme yeteneği eklemektir.

. import List, Dict:
def add_student(students, student_data):
    # Fonksiyonun ne beklediği belirsiz.

from typing import List, Dict
def add_student(STUDENTS: List[Dict], student_data: Dict) -> Dict:
    # STUDENTS: Listenin içinde Sözlükler (öğrenci objeleri) bekliyoruz.
    # student_data: Tek bir Sözlük (yeni öğrenci verisi) bekliyoruz.
    # -> Dict: Fonksiyonun bir Sözlük (eklenen öğrenci) döndüreceğini belirtiyoruz.
'''

def add_student(STUDENTS: List[Dict], student_data: Dict) -> Dict:
    if not student_data.get("numara"):
        print("Hata: Öğrenci 'numara' alanı zorunludur.")
        return None

    index = 0
    list_len = len(STUDENTS)
    while index < list_len:
        if STUDENTS[index]["numara"] == student_data["numara"]:
            print(f"Hata: {student_data['numara']} numara'lı öğrenci zaten mevcut.") #Benzersizliğini betimler.
            return None
        index += 1
            
    STUDENTS.append(student_data)
    print(f"Öğrenci eklendi: {student_data['name']}")
    return student_data

def delete_student(STUDENTS: List[Dict], student_numara: str) -> Dict | None:
    index = 0
    list_len = len(STUDENTS)
    
    while index < list_len:
        student = STUDENTS[index]
        
        if student.get("numara") == student_numara:
            deleted_student = STUDENTS.pop(index)

            '''
            . STUDENTS adlı listeden index numarasındaki elemanı çıkarır (siler).
            . Silinen bu elemanı geri döndürür.
            . Dönen değer de deleted_student değişkenine atanır.
            '''
            
            print(f" Başarılı: {student_numara} numara'lı öğrenci ({deleted_student.get('name')}) silindi.")
            return deleted_student
        index += 1

    print(f" Hata: {student_numara} numara'lı öğrenci bulunamadı.")
    return None

def changed_student(COURSES: List[Dict], student_numara: str, course_numara: str) -> bool: #Sadece iki olası değeri temsil eder: True (Doğru) veya False (Yanlış).
    index = 0
    list_len = len(COURSES)
    while index < list_len:
        course = COURSES[index]
        if course["numara"] == course_numara:
            if "students" not in course: #Bir öğrenciyi bir derse kaydetme.
                course["students"] = []

            s_index = 0
            is_changed = False
            s_list_len = len(course["students"]) #Öğrencinin zaten kayıtlı olup olmadığını kontrol etme.
            while s_index < s_list_len:
                if course["students"][s_index] == student_numara:
                    is_changed = True
                    break
                s_index += 1
                
            if not is_changed:
                course["students"].append(student_numara)
                print(f"Öğrenci {student_numara}, {course_numara} dersine kaydedildi.")
                return True
            else:
                print("Öğrenci zaten bu derse kayıtlı.")
                return False
        index += 1
                
    print(f"Hata: {course_numara} numara'lı ders bulunamadı.")
    return False

def add_course(COURSES: List[Dict], course_data: Dict) -> Dict:
    if not course_data.get("numara"):
        print("Hata: Ders 'numara' alanı zorunludur.")
        return None
        
    index = 0
    list_len = len(COURSES)
    while index < list_len:
        if COURSES[index]["numara"] == course_data["numara"]:
            print(f"Hata: {course_data['numara']} numara'lı ders zaten mevcut.")
            return None
        index += 1

    COURSES.append(course_data)
    print(f"Ders eklendi: {course_data['baslık']}")
    return course_data