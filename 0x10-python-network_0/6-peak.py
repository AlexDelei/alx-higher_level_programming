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
    if list_of_integers:
        small = list_of_integers[0]
        for j in range(1, len(list_of_integers)):
            if list_of_integers[j] > small:
                small = list_of_integers[j]
        return small
    else:
        return None
