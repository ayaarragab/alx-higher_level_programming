#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    result = 0
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        result += int(arg)
    print(result)
