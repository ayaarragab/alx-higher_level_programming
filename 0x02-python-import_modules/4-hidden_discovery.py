#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    for arg in names:
        for c in arg:
            if '__' in  arg:
                continue
        print('{}'.format(arg))
