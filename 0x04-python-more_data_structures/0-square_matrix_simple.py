#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map((lamda x: x ** 2), elm)) for elm in matrix])
