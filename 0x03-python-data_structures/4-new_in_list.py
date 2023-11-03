#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_ = my_list[:]
    len_ = len(my_list)

    if idx < 0 or idx > len_:
        return my_list
    else:
        my_list_.insert(idx, element)
        my_list_.pop(idx + 1)
        return my_list_
