import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    dividend, divisor = (val for val in line.split(SEPARATOR))

    err = False

    try:
        dividend = float(dividend)
    except:
        print("Invalid Dividend")
        err = True
    
    try:
        divisor = float(divisor)
    except:
        if not err:
            print("Invalid Divisor")
            err = True

    
    if divisor == 0 and not err:
        print("Divide By Zero")
        err = True

    if not err:
        answer = dividend / divisor
        round(answer, "1")

        if int(answer) == answer:
            print(int(answer))
        else: print(answer)