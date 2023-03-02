"""
dictionaries.py

Practice problems for using dictionaries.
"""

# 1 ---------------------------------------------------------------------------
def get_cross_class_grades(students, shared_classes):
    """ Return cross-class grade averages for students

    A school is trying to calculate average grades across classes for a set of 
    students. Given two inputs, one a list representing the names of each 
    student, and the other a dictionary representing classes and the grades for
    the respective students, calculate the average grade across classes for each
    student, returning a dictionary where the keys are students and the values
    are their cross-class grade averages. The index of the each student in the 
    students array is the same index as their respective grades in each class.

    For example:
    students = ["John", "Mary", "Jane", "Jack"]
    shared_classes = {
        "CMSC 14100": [80.0, 90.0, 95.0, 89.0],
        "HUMA 12300": [91.0, 92.0, 70.0, 98.0],
        "SOSC 13200": [89.0, 95.0, 80.0, 91.0],
        "SPAN 10200": [90.0, 88.0, 85.0, 74.0],
    }

    cross_class_avgs = get_cross_class_grades(students, shared_classes)
    
    Then:
    cross_class_avgs: {'John': 87.5, 'Mary': 91.25, 'Jane': 82.5, 'Jack': 88.0}

    Args:
        students (list[str]): The list of students with shared classes
        shared_classes (dict[str, list[float]]): The classes and students' grades
    """

    raise NotImplementedError

# 2 ---------------------------------------------------------------------------
def get_student_late_days(students, days):
    """ Return students' late day counts and the best attending student.

    This very same school also wants to be able to calculate the number of 
    tardies (late days) for each student's weekly report, as well as find out
    which student had the fewest late days that week. Given two inputs, one an
    array of student names, and the other a 2d array consisting of each student's
    late record for the previous week (as an array of booleans, where True is
    late), calculate the number of days each student came late, as well as the
    name of the student who had the least tardies.

    Importantly, the school wants any student whose number of tardies in a given
    week is < 2 to be *marked* as 0, since disciplinary action is taken on a
    cumulative, semesterly basis only for those with 2 or more tardies each week.
    This should not affect the name of the student with the least tardies.

    The function should return a tuple, where the first item is the dict containing
    students names and their number of tardies for the week, and the second item
    is the name of the student with the least tardies that week.

    In cases of a tie for best student, the best student name should be
    whichever student's name comes last in the given array.

    For example:
    students = ["John", "Mary", "Jane", "Jack"]
    late_days = [
        [False, True, True, True, False],
        [True, False, True, False, True],
        [False, False, False, True, False],
        [False, False, True, True, False],
    ]

    per_student_counts, best_student = get_student_late_days(students, late_days)

    Then:
    per_student_counts: {'John': 3, 'Mary': 3, 'Jane': 0, 'Jack': 2}
    best_student: 'Jane'

    Args:
        students (list[str]): The list of students to calculate late days for
        days (list[list[bool]]): 2d array consisting of lists of length 5 corresponding
            to each school day, where True is if they came late, False otherwise
    """
    raise NotImplementedError

# 3 ---------------------------------------------------------------------------
def create_student_reports(students, shared_classes, weeks):
    """ Return students report cards.

    Last but not least, this school wants to take in all of the info for the
    whole semester, and generate a report card for each student. You are given 
    three inputs, one an array of student names, second a dictionary representing
    shared classes among these students and their respective grades (in the same 
    format as used above), and lastly a 3d array of weeks, where each week
    consists of a 2d, boolean array of late days for each student (also in the
    same format as used above). Return a dictionary where the keys are students,
    and the values represent a report card for each student.

    Each report card should be a dictionary with three entries: 
        name: the name of the student
        avg_grade: the cross-class average grade for the student
        late_days: the total number of late days (exluding weeks with < 2 tardies) 

    students = ["John", "Mary", "Jane", "Jack"]
    shared_classes = {
        "CMSC 14100": [80.0, 90.0, 95.0, 89.0],
        "HUMA 12300": [91.0, 92.0, 70.0, 98.0],
        "SOSC 13200": [89.0, 95.0, 80.0, 91.0],
        "SPAN 10200": [90.0, 88.0, 85.0, 74.0],
    }
    late_days = [
        [
            [False, True,  True, True, False],
            [True, False, True, False, True],
            [False, False, False, True, False],
            [False, False, True, True, False],
        ],
        [
            [False, True, True, True, False],
            [True, False, True, False, True],
            [False, True, False, True, False],
            [False, False, True, True, False],
        ],
        [
            [False, True, False, True, False],
            [True, False, True, False, False],
            [False, False, False, True, False],
            [False, False, True, False, False],
        ],
    ]
    
    reports = create_student_reports(students, shared_classes, late_days)
    
    Then:
    {
        'John': {'name': 'John', 'avg_grade': 87.5, 'late_days': 8},
        'Mary': {'name': 'Mary', 'avg_grade': 91.25, 'late_days': 8},
        'Jane': {'name': 'Jane', 'avg_grade': 82.5, 'late_days': 2},
        'Jack': {'name': 'Jack', 'avg_grade': 88.0, 'late_days': 4}
    }

    Args:
        students (list[str]): _description_
        shared_classes (dict[str, list[float]]): _description_
        weeks (list[list[list[bool]]]): _description_
    """
    raise NotImplementedError
