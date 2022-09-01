#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = 0
        best = ''
        for key, value in a_dictionary.items():
            if value > max:
                max = value
                best = key
        return best
