import sys
import string

SEPARATOR = "|"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    greeting,response = line.upper().split(SEPARATOR)

    valid = True

    for i, val in enumerate(response):
        if val.isalpha() and val not in greeting:
            valid = False
            break

    if valid: print("That's my secret contact!") 
    else: print("You're not a secret agent!")