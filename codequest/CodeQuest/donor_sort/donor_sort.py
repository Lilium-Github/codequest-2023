import sys

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    lastYear = line.split(SEPARATOR)
    line = sys.stdin.readline().rstrip()
    thisYear = line.split(SEPARATOR)

    line1 = []
    line2 = []
    line3 = []

    allDonors = list(lastYear)

    for index, value in enumerate(thisYear):
        if value not in lastYear:
            allDonors.append(value)

    for index, value in enumerate(allDonors):
        if value in lastYear:
            if value in thisYear:
                line2.append(value)
            else:
                line1.append(value)
        elif value in thisYear:
            line3.append(value)

    line1.sort()
    line2.sort()
    line3.sort()

    for index, value in enumerate(line1):
        print(value, end="")
        if index < len(line1)-1:
            print(",", end="")
        else:
            print("\n", end="")

    for index, value in enumerate(line2):
        print(value, end="")
        if index < len(line2)-1:
            print(",", end="")
        else:
            print("\n", end="")

    for index, value in enumerate(line3):
        print(value, end="")
        if index < len(line3)-1:
            print(",", end="")
        else:
            print("\n", end="")