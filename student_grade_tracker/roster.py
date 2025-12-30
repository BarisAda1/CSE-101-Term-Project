def add_student(student_list, student_data):
    if "number" not in student_data or len(student_data["number"]) == 0:
        print("Öğrenci numarası zorunludur! Numarayı doğru bir şekilde girerek tekrar dene.")
        return
    found = False
    for s in student_list:
        if s["number"] == student_data["number"]:
            found = True
            break
    if found:
        print("Bu numaraya sahip bir öğrenci zaten var.")
    else:
        student_list.append(student_data)
        print("Öğrenci eklendi.")

def add_course(course_list, course_data):
    found = False
    for c in course_list:
        if c["code"] == course_data["code"]:
            found = True
            break     
    if found:
        print("Bu koda sahip bir ders zaten var.")
    else:
        course_list.append(course_data)
        print("Ders eklendi.")