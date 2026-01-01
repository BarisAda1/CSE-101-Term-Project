import json

def load_state():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        students = data.get("students", [])
        courses = data.get("courses", [])
        notbooklet = data.get("gradebook", data.get("grades", {}))
        settings = data.get("settings", {})
        return students, courses, notbooklet, settings
    except (FileNotFoundError, json.JSONDecodeError): #If you receive a "file not found" error, it will return empty data.
        return [], [], {}, {}

''' import os #Python'un senin bilgisayarının İşletim Sistemi (Operating System) ile konuşmasını sağlar.
def load_state():
    if not os.path.exists("data.json"): #Check if the file exists or not.
        return [], [], {}, {}
    with open("data.json", "r") as f:
        data = json.load(f)
    return data.get("students", []), data.get("courses", []), data.get("gradebook", {}), data.get("settings", {}) '''

def save_state(students, courses, notbooklet, settings):
    data = {
        "students": students,
        "courses": courses,
        "gradebook": notbooklet,
        "settings": settings}
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
#'f' = Yazma modunda ("w") açılmış dosya nesnesidir.
#'indent=4' = JSON çıktısını daha okunabilir yapar ve her seviye için 4 boşluk ekler.
#'ensure_ascii=False' = Türkçe karakterlerin bozulmadan yazılmasını sağlar.
    print("Veriler data.json'a kaydedildi.")