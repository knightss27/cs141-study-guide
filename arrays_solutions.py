"""
arrays_solutions.py

Example implementations / solutions to the dictionary-related problems found
in the arrays.py file.
"""
from utils import random_odd_in_range

# 1 ---------------------------------------------------------------------------
def create_random_groupings(arr):
    """
    Example implementation
    """
    # instantiate the groups array to return
    groups = []
    # go through each item in given array
    for i, val in enumerate(arr):
        # instantiate the current group
        current_group = []
        # get the random size, and floor divide by two for each side's length
        size = random_odd_in_range(len(arr), val) // 2
        # loop through all possible positions in this randomly sized group
        # remember to add one here, as the top of range() is exclusive
        for j in range(i - size, i + size + 1):
            # check if this position is outside of the given array's length
            if j < 0 or j >= len(arr):
                current_group.append(0)
            else:
                current_group.append(arr[j])

        # append this group to the overall list
        groups.append(current_group)

    return groups

# Testing code for create_random_groupings
# arr = [10, 20, 30, 40, 50, 60, 70]
# groups = create_random_groupings(arr)
# print(groups)

# 2 ---------------------------------------------------------------------------
def flatten_diagonals(arr):
    """
    Example implementation
    """
    # initialize the variables
    top_diagonal = []
    bottom_diagonal = []

    # go through each row, keeping track of which row index we're on
    for i, row in enumerate(arr):
        # add the top diagonal to the end
        top_diagonal.append(row[i])
        # add the bottom diagonal to the front, to keep the left-right order
        bottom_diagonal.insert(0, row[-(i+1)])

    return [top_diagonal, bottom_diagonal]

# Testing code for flatten_diagonals
# arr = [
#     [10, 20, 30, 40, 55],
#     [10, 20, 30, 45, 50],
#     [10, 20, 35, 40, 50],
#     [10, 25, 30, 40, 50],
#     [15, 20, 30, 40, 50],
# ]
# diagonals = flatten_diagonals(arr)
# print(diagonals)

# 3 ---------------------------------------------------------------------------
def get_sub_arrays(arr):
    """
    Example implementation
    """
    # Base case
    if len(arr) == 1:
        return [arr]

    # add individual option to array
    subs = [[arr[0]]]
    # get all the sub arrays excluding the first element
    next_subs = get_sub_arrays(arr[1:])
    # add all these sub arrays with the first element of this array
    subs.extend([[arr[0]] + array for array in next_subs])
    # add all these sub arrays by themselves
    subs.extend(next_subs)

    return subs

# Testing code for get_sub_arrays
# arr = [10, 20, 30, 40]
# sub_arrays = get_sub_arrays(arr)
# print(sub_arrays)
