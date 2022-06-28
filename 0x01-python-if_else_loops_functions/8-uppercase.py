#!/usr/bin/python3

# Print a string in uppercase.
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    print("")