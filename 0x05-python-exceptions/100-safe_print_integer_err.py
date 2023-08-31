#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as exx:
        if ValueError:
            sys.stderr.write(f"Exception: {exx}\n")
        elif TypeError:
            sys.stderr.write(f"Exception: {exx}\n")
        return False
