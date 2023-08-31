#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as exx:
        sys.stderr.write(f"Exception: {exx}\n")
        return None
