#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    for arg in names:
        for c in arg:
            if c == '__':
                continue
        print('{}'.format(arg))
