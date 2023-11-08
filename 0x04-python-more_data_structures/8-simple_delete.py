#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # checking if a key exists
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
