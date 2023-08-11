#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    for i, arg in enumerate(names):
        if arg[i] == '_':
            continue
        print(arg)
