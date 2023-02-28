import sys

UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
NUMBERS = ['1','2','3','4','5','6','7','8','9','0']

def areRepeats(word):
    for i in range(2, len(word)):
        if word[i] == word[i-1] and word[i] == word[i-2]:
            return True

    return False

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    password = sys.stdin.readline().rstrip()

    isValid = True

    if areRepeats(password):
        isValid = False

    if len(password) < 8:
        isValid = False

    groupNum = 0

    for i in password:
        if i in UPPERCASE:
            groupNum += 1
            break

    for i in password:
        if i in LOWERCASE:
            groupNum += 1
            break

    for i in password:
        if i in NUMBERS:
            groupNum += 1
            break

    for i in password:
        if i not in UPPERCASE and i not in LOWERCASE and i not in NUMBERS:
            groupNum += 1
            break

    if groupNum < 3:
        isValid = False

    if isValid:
        print("VALID")
    else:
        print("INVALID")