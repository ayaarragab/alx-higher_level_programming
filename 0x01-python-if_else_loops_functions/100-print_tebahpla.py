#!/usr/bin/python3
count = 1
i = 122
while (i >= 97):
    if count % 2 != 0:
        print('{}'.format(chr(i)), end="")
        count += 1
        i -= 1
    else:
        print(chr(i - 32), end="")
        count += 1
        i -= 1
