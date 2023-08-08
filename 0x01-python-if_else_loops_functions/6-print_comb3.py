#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 9):
        if i == 9 and j == 8:
            print('{}'.format(str(i)) + '{}'.format(str(j)))
            break
        print('{}'.format(str(i)) + '{}'.format(str(j)), end=", ")
