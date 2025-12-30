def calculate_average(gradebook, settings, course_id, student_id):
    if course_id not in gradebook or student_id not in gradebook[course_id]:
        return 0.0 #starting grade value
    student_grades = gradebook[course_id][student_id]
    course_settings = settings.get(course_id, {})
    weights = course_settings.get("weights", {})
    total_score = 0.0
    for grade in student_grades:
        category = grade["category"]
        weight_val = weights.get(category, 0)
        weight = float(weight_val) / 100
        total_score += grade["score"] * weight
    return total_score

def get_epistle_grade(score, settings, course_id):
    scale = settings.get(course_id, {}).get("scale", {
        "AA": 90.0, "BB": 80.0, "CC": 70.0, "DD": 60.0, "EE": 50.0, "FF": 0.0 })
    grade_list = []
    for k in scale:
        val = scale[k]
        grade_list.append([val, k])
    grade_list.sort(reverse=True)
    for item in grade_list:
        verge = item[0]
        grade = item[1]
        if score >= verge:
            return grade
    return "FF"