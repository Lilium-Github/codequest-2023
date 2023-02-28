import sys

cases = int(sys.stdin.readline().rstrip())

def checkFive(hand):
    for i in range(4, len(hand)):
        if hand[i] == hand[i-1] and hand[i] == hand[i-2] and hand[i] == hand[i-3] and hand[i] == hand[i-4]:
            return True

    return False
def checkFour(hand):
    for i in range(3, len(hand)):
        if hand[i] == hand[i-1] and hand[i] == hand[i-2] and hand[i] == hand[i-3]:
            return True

    return False

def checkFullHouse(hand):
    foundThree = False
    foundPair = False
    triplet = "placeholder"

    for i in range(2, len(hand)):
        if hand[i] == hand[i-1] and hand[i] == hand[i-2]:
            triplet = hand[i]
            foundThree = True
            break

    for i in range(1, len(hand)):
        if hand[i] == hand[i-1] and hand[i] != triplet:
            foundPair = True
            break

    if foundThree and foundPair:
        return True
    return False

def checkStraight(in_hand):
    hand = list(in_hand)

    done = False
    changeMade = False

    while not done:
        for i in range(1, len(hand)):
            changeMade = False
            if hand[i] == hand[i-1]:
                hand.remove(hand[i-1])
                changeMade = True
                break

        if not changeMade:
            done = True

    for i in range(4, len(hand)):
        if hand[i] == hand[i-1] + 1 and hand[i] == hand[i-2] + 2 and hand[i] == hand[i-3] + 3 and hand[i] == hand[i-4] + 4:
            return True
        
    return False

def checkThree(hand):
    for i in range(2, len(hand)):
        if hand[i] == hand[i-1] and hand[i] == hand[i-2]:
            return True

    return False

def checkTwoPair(hand):
    foundPair = False
    pair = "placeholder"

    for i in range(1, len(hand)):
        if hand[i] == hand[i-1]:
            pair = hand[i]
            foundPair = True
            break

    if not foundPair:
        return False

    for i in range(1, len(hand)):
        if hand[i] == hand[i-1] and hand[i] != pair:
            return True
               
    return False

def checkPair(hand):
    for i in range(1 , len(hand)):
        if hand[i] == hand[i-1]:
            return True

    return False

for caseNum in range(cases):
    hand = sys.stdin.readline().rstrip()

    sortedHand = list(hand)
    sortedHand.sort()

    for i, val in enumerate(sortedHand):
        sortedHand[i] = int(sortedHand[i])

    while 0 in sortedHand:
        sortedHand.remove(0)

    if checkFive(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = FIVE OF A KIND")
    elif checkFour(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = FOUR OF A KIND")
    elif checkFullHouse(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = FULL HOUSE")
    elif checkStraight(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = STRAIGHT")
    elif checkThree(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = THREE OF A KIND")
    elif checkTwoPair(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = TWO PAIR")
    elif checkPair(sortedHand):
        for i in hand:
            print(i, end="")
        print(" = PAIR")
    else:
        for i in hand:
            print(i, end="")
        print(" =", sortedHand[-1])