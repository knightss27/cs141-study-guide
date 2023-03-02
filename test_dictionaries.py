import random
import dictionaries
import dictionaries_solutions

def test_cross_class_grades():
    n = random.randrange(10)
    students = [f"Name{i}" for i in range(n)]
    shared_classes = {
        "CMSC 14100": [random.randrange(80, 90) for _ in range(n)],
        "HUMA 12300": [random.randrange(80, 90) for _ in range(n)],
        "SOSC 13200": [random.randrange(80, 90) for _ in range(n)],
        "SPAN 10200": [random.randrange(80, 90) for _ in range(n)],
    }

    grades_user = dictionaries.get_cross_class_grades(students, shared_classes)
    grades_solution = dictionaries_solutions.get_cross_class_grades(students, shared_classes)

    for key in grades_solution:
        assert key in grades_user
        assert grades_user[key] == grades_solution[key]

def test_student_late_days():
    n = random.randrange(10)
    students = [f"Name{i}" for i in range(n)]
    late_days = [[random.random() > 0.5 for _ in range(5)] for i in range(n)]

    lates_user = dictionaries.get_student_late_days(students, late_days)
    lates_solution = dictionaries_solutions.get_student_late_days(students, late_days)

    for key in lates_solution[0]:
        assert key in lates_user[0]
        assert lates_user[0][key] == lates_solution[0][key]

    assert lates_user[1] == lates_solution[1]

def test_student_reports():
    n = random.randrange(10)
    students = [f"Name{i}" for i in range(n)]
    shared_classes = {
        "CMSC 14100": [random.randrange(80, 90) for _ in range(n)],
        "HUMA 12300": [random.randrange(80, 90) for _ in range(n)],
        "SOSC 13200": [random.randrange(80, 90) for _ in range(n)],
        "SPAN 10200": [random.randrange(80, 90) for _ in range(n)],
    }
    late_days = [[[random.random() > 0.5 for _ in range(5)] for i in range(n)] for j in range(5)]

    reports_user = dictionaries.create_student_reports(students, shared_classes, late_days)
    reports_solution = dictionaries_solutions.create_student_reports(students, shared_classes, late_days)

    for key in reports_solution:
        assert key in reports_user
        assert reports_user[key]["name"] == reports_solution[key]["name"]
        assert reports_user[key]["avg_grade"] == reports_solution[key]["avg_grade"]
        assert reports_user[key]["late_days"] == reports_solution[key]["late_days"]
    
