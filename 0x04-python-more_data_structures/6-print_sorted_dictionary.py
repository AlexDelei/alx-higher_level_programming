#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_kys = sorted(a_dictionary.keys())
    for key in sorted_kys:
        value = a_dictionary[key]

        if isinstance(value, dict):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value}")
