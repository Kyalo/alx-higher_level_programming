#!/usr/bin/python3

# Print the alphabet in lowercase, not followed by a new line,
# except q and e.
for l in range(97, 123):
    if chr(l) is not 'q' and chr(l) is not 'e':
        print(f"{chr(l)}", end="")
