#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_ = len(my_list)
    for i in range(len_ - 1, -1, -1):
        print("{:d}".format(my_list[i]))
