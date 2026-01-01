def weights2(settings, course_id, policy):
    settings[course_id] = policy
    print("Dersin ağırlıkları kaydedildi.")

def rec(notbooklet, course_id, student_id, assessment):
    if course_id not in notbooklet:
        notbooklet[course_id] = {}
    if student_id not in notbooklet[course_id]:
        notbooklet[course_id][student_id] = []
    notbooklet[course_id][student_id].append(assessment)
    print(f"Not kaydedildi: {assessment['name']}")