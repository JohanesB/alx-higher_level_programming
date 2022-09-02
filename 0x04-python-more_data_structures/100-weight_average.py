#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        x = 0
        y = 0
        for j in my_list:
            x += (j[0] * j[1])
            y += j[1]
        return (x / y)
    return 0
