#!/usr/bin/python3
for i in range(97, 123):
    if '{}'.format(chr(i)) != 'q' and '{}'.format(chr(i)) != 'e':
        print("{}".format(chr(i)), end="")
