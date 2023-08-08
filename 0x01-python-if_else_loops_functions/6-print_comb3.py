#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i < j:
            if i == 8 and j == 9:
                print('{}'.format(str(i)) + '{}'.format(str(j)))
                break
            print('{}'.format(str(i)) + '{}'.format(str(j)), end=", ")
        elif i == j:
            continue
