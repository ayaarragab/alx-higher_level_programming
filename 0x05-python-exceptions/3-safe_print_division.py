#!/usr/bin/python3
def safe_print_division(a, b):
    result = 1
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('{}'.format(result))
        return (result)
