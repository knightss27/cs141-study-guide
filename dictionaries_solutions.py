"""
dictionaries_solutions.py

Example implementations / solutions to the dictionary-related problems found
in the dictionaries.py file.
"""

# 1 ---------------------------------------------------------------------------
def get_cross_class_grades(students, shared_classes):
    """
    Example implementation
    """
    # instantiate the dictionary to return
    avgs = {}

    # go through each student (keeping track of the index)
    for i, student in enumerate(students):
        # instantiate the student's entry in the dictionary to 0
        avgs[student] = 0.0
        # for each class, add the respective student's grade to the average
        for _, shared_class_grades in shared_classes.items():
            avgs[student] += shared_class_grades[i]

        # calculate the average by dividing over the number of classes
        avgs[student] /= len(shared_classes)

    return avgs

# Testing code for get_cross_class_grades
students = ["John", "Mary", "Jane", "Jack"]
shared_classes = {
    "CMSC 14100": [80.0, 90.0, 95.0, 89.0],
    "HUMA 12300": [91.0, 92.0, 70.0, 98.0],
    "SOSC 13200": [89.0, 95.0, 80.0, 91.0],
    "SPAN 10200": [90.0, 88.0, 85.0, 74.0],
}

cross_class_avgs = get_cross_class_grades(students, shared_classes)
print(cross_class_avgs)

# 2 ---------------------------------------------------------------------------
def get_student_late_days(students, days):
    """
    Example implementation
    """
    # instantiate the variables to return
    lates = {}
    best_student = students[0]

    # go through each student (keeping track of the index)
    for i, student in enumerate(students):
        # instantiate the student's entry in the dictionary to 0
        lates[student] = 0
        # for each day, tally up if it was a tardy
        for day in days[i]:
            if day:
                lates[student] += 1

        # if this is the new best student, remember it as such
        if lates[student] <= lates[best_student]:
            best_student = student

    # remove all tardies for students with < 2 in a week
    for student in students:
        if lates[student] < 2:
            lates[student] = 0

    return (lates, best_student)

# Testing code for get_student_late_days
students = ["John", "Mary", "Jane", "Jack"]
late_days = [
    [False, True, True, True, False],
    [True, False, True, False, True],
    [False, False, False, True, False],
    [False, False, True, True, False],
]

per_student_counts, best = get_student_late_days(students, late_days)
print(per_student_counts, best)
