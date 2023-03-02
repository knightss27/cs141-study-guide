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


# 3 ---------------------------------------------------------------------------

