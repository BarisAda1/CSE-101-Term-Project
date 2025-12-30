def weights2(settings, course_id, policy):
    settings[course_id] = policy
    print("Dersin ağırlıkları kaydedildi.")

def rec(gradebook, course_id, student_id, assessment):
    if course_id not in gradebook:
        gradebook[course_id] = {}
    if student_id not in gradebook[course_id]:
        gradebook[course_id][student_id] = []
    gradebook[course_id][student_id].append(assessment)
    print(f"Not kaydedildi: {assessment['name']}")