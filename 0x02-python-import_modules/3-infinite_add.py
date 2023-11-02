#!/usr/bin/python3
import sys
def adding_args(*args):
    ttl = 0
    for arg in args:
        ttl += int(arg)#convert to int
    return ttl
if __name__ == '__main__':
    argum = sys.argv[1:]#Excluding the first argument
    result = adding_args(*argum)
    print("{:d}".format(result))
