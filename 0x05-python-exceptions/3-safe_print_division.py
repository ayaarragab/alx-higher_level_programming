#!/usr/bin/python3
def safe_print_division(a, b):
    result = 1
    try:
        a / b
    except ZeroDivisionError:
        pass
    finally:
        if a / b:
            print('{}'.format(a / b))
        else:
            print('{}'.format(None))
