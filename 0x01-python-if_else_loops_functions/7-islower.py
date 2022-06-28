#!/usr/bin/python3

'''
Checks for lowercase character
Returns True if c is lowercase
Returns False otherwise
'''
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
