#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cnt = 0
        for i in my_list:
            cnt += 1
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return x
    except:
        print()
        return cnt
