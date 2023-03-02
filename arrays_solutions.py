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
