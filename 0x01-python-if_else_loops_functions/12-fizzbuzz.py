#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i == 100:
            print('Buzz')
            break
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz', end=" ")
            continue
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz', end=" ")
            continue
        elif i % 5 == 0 and i % 3 == 0:
            print('FizzBuz', end=" ")
            continue
        print(i, end=" ")
