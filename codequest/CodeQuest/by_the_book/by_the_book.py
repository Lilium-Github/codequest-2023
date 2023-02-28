import sys

def eleven_diff(n):
    multiple = 0
    while multiple < n:
        multiple += 11
    
    output = multiple - n

    if output == 10:
        return 'X'
    else:
        return output

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    num = sys.stdin.readline().rstrip()

    check = num[-1]

    weight_sum = 0

    for i in range(9):
        int_weight = 10 - i
        to_add = int(num[i]) * int_weight

        weight_sum += to_add

    if str(eleven_diff(weight_sum)) == check:
        print("VALID")
    else:
        print("INVALID")