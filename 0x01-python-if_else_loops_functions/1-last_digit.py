#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ldt1 = number % 10000
    ldt2 = ldt1 % 1000
    ldt3 = ldt2 % 100
    last = number % 10

    if last == 0:
        print("Last digit of %d is %d and is 0" % (number, last))
    elif last > 5:
        print("Last digit of %d is %d and is greater than 5" % (number, last))
    elif last < 6 & last != 0:
        print("Last digit of %d is %d and is less than 6 and not 0" % (number, last))
else:
    ldt1 = number % -10000
    ldt2 = ldt1 % -1000
    ldt3 = ldt2 % -100
    last = ldt3 % -10

    if last == 0:
        print("Last digit of %d is %d and is 0" % (number, last))
    else:
        print("Last digit of %d is %d and is less than 6 and not 0" % (number, last))
