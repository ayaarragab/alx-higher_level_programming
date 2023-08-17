#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_score = 0
        total_weights = 0
        for tup in my_list:
            total_score += tup[0] * tup[1]
            total_weights += tup[1]
        return (total_score / total_weights)
    else:
        return 0
