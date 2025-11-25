#
from ast import Dict
from typing import List

def add_student(STUDENTS: List[Dict], student_data: Dict):
    if not student_data.get("numara"):
        print("Hata: Öğrenci 'numara' alanı zorunludur.")
        return None

    index = 0
    listl = len(STUDENTS)
    while index < listl:
        if STUDENTS[index]["numara"] == student_data["numara"]:
            print(f"Hata: {student_data['numara']} numara'lı öğrenci zaten mevcut.") #Benzersizliğini betimler.
            return None
        index += 1
            
    STUDENTS.append(student_data)
    print(f"Öğrenci eklendi: {student_data['name']}")
    return student_data

'''
        index < list_len:
        student = STUDENTS[index]
        deleted_student = STUDENTS.pop(index)

            . STUDENTS adlı listeden index numarasındaki elemanı çıkarır (siler).
            . Silinen bu elemanı geri döndürür.
            . Dönen değer de deleted_student değişkenine atanır.

        print(f" Başarılı: {student_numara} numara'lı öğrenci ({deleted_student.get('name')}) silindi.")
        index += 1
'''

def new_func():
    return

new_func()