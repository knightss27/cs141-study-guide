import random
import arrays
import arrays_solutions

def test_create_random_groupings():
    arr = [random.randint(1,10) for _ in range(random.randrange(20))]
    groupings_user = arrays.create_random_groupings(arr)
    groupings_solution = arrays_solutions.create_random_groupings(arr)

    assert len(groupings_user) == len(groupings_solution)
    assert groupings_user == groupings_solution

def test_flatten_diagonals():
    n = random.randrange(20)
    arr = [[random.randint(1,10) for _ in range(n)]] * n

    diagonals_user = arrays.flatten_diagonals(arr)
    diagonals_solution = arrays_solutions.flatten_diagonals(arr)

    assert len(diagonals_user) == 2
    assert len(diagonals_user[0]) == n
    assert len(diagonals_user[1]) == n
    assert diagonals_user[0] == diagonals_solution[0]
    assert diagonals_user[1] == diagonals_solution[1]

def test_get_sub_arrays():
    arr = [random.randint(1,10) for _ in range(random.randrange(10))]
    subs_user = arrays.get_sub_arrays(arr)
    subs_solution = arrays_solutions.get_sub_arrays(arr)

    assert len(subs_user) == len(subs_solution)
    for i in subs_user:
        assert i in subs_solution

    assert subs_user == subs_solution