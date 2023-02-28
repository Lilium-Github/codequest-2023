import sys

vals = [1,2,3]
print(vals[0:2])

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    val1, val2 = (float(val) for val in line.split(SEPARATOR))
    