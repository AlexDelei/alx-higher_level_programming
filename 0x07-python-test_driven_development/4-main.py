#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square()
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square('3')
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
