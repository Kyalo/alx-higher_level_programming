#!/usr/bin/python3

"""
Print all possible different combinations of two digits in ascending order.
The two digits must be different - 01 and 10 are considered identical.
"""
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 8 and y == 9:
            print("{x}{y}".format(x, y))
        else:
            print("{x}{y}".format(x, y), end=", ")
