#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        element = 0
        try:
            element = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print("out of range")
        finally:
            newList.append(element)
    return newList
