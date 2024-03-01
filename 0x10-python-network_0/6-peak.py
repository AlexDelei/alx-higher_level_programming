#!/usr/bin/python3
"""
Finding peak in a list of randome integers
"""


def find_peak(list_of_integers):
    """
    Finding a peak in a list of unsorted integers

    Args:
    - list_of_integers: List of integers

    Returns:
    - The peak elemet(s)
    """
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1

    mid = high // 2
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        high = mid
    else:
        low = mid + 1
    return list_of_integers[low]
