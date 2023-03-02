"""
utils.py

Utility functions for use with the practice problems.
"""
import random


def random_odd_in_range(n, seed):
    """ Returns an ODD random number from 1 to N (inclusive). Predictable for use 
    with testing.

    Args:
        n (int): inclusive end of range
        seed (int): the seed for the random number

    Returns:
        int: random number in range
    """
    random.seed(seed)
    num = random.randint(1, n)
    if num % 2 == 0:
        num += 1
    return num
