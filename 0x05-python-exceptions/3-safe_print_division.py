#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))
        return result
    except:
        print("Inside result: None")
        return None
