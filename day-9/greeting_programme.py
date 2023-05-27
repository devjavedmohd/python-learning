student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        print(f"{student} Outstanding")
        student_grades[student] = "Outstanding"
    elif score > 80:
        print(f"{student} Exceed Expectations")
        student_grades[student] = "Exceed Expectations"
    elif score > 70:
        print(f"{student} Acceptable")
        student_grades[student] = "Acceptable"
    else:
        print(f"{student} Fail")
        student_grades[student] = "Fail"
print(student_grades)
