"""
arrays.py

Practice problems for using arrays.
"""
from utils import random_odd_in_range

# 1 ---------------------------------------------------------------------------
def create_random_groupings(arr):
    """ Return the groupings of random lengths.

        There is no story to this problem (ha!). Your task is to take an input
        array of integers and return neighborhoods of random (odd) lengths,
        centered around each element of the array. Edge cases should be padded
        with 0's in the places where there the neighborhood is too large.

        1. The largest neighborhood should be the size of the given array. i.e.
        no returned array should be larger than the length of the given array.

        2. You should use the imported `random_odd_in_range` function for this
        problem. The seed should be the value that this grouping is centered at.

        For example:
        arr = [10, 20, 30, 40, 50, 60, 70]
        groups = create_random_groupings(arr)

        Then:
        groups: [
            [0, 0, 10, 20, 30],
            [0, 0, 10, 20, 30, 40, 50],
            [10, 20, 30, 40, 50],
            [20, 30, 40, 50, 60],
            [30, 40, 50, 60, 70],
            [50, 60, 70],
            [70]
        ]

    """
    raise NotImplementedError

# 2 ---------------------------------------------------------------------------
def flatten_diagonals(arr):
    """ Return flattened diagonals.

        Another problem with no story (how sad!). Your task is to take a 2d
        array of any SQUARE size (that is, the same # of rows and columns), and
        return lists of the two diagonals, from left to right, were you to write
        out the array.

        For example:
        arr = [
            [10, 20, 30, 40, 55],
            [10, 20, 30, 45, 50],
            [10, 20, 35, 40, 50],
            [10, 25, 30, 40, 50],
            [15, 20, 30, 40, 50],
        ]
        diagonals = flatten_diagonals(arr)

        Then:
        diagonals: [
            [10, 20, 35, 40, 50],
            [15, 25, 35, 45, 55]
        ]
    """
    raise NotImplementedError

# 3 ---------------------------------------------------------------------------
def get_sub_arrays(arr):
    """ Return an array of all sub arrays.

        As a classic array problem, your job is to return all possible sub arrays
        of the given array. Elements that come first in the given array should
        be in the same order in sub arrays. DO NOT include the original array,
        or any empty arrays. Sub arrays do not need to be continuous.

        For example:
        arr = [10, 20, 30]
        sub_arrays = get_sub_arrays(arr)

        Then:
        sub_arrays: [
            [10],
            [10, 20],
            [10, 20, 30],
            [10, 30],
            [20],
            [20, 30],
            [30]
        ]
    """
    raise NotImplementedError
