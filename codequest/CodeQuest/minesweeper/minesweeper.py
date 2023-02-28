import sys

def placeBomb(mine_map, bomb):
    mapH, mapW = len(mine_map), len(mine_map[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if (bomb[0] + i < mapH and bomb[0] + i >= 0) and (bomb[1] + j < mapW and bomb[1] + j >= 0):
                if type(mine_map[bomb[0] + i][bomb[1] + j]) == int:
                    mine_map[bomb[0] + i][bomb[1] + j] += 1

    mine_map[bomb[0]][bomb[1]] = "*"
            
SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    R, C, B = (int(val) for val in line.split(SEPARATOR))

    bombs = [] # list of tuples. each tuple has two values, the x and y coordinates of a bomb.

    for _ in range(B):
        line = sys.stdin.readline().rstrip()
        bomb = (line.split(SEPARATOR))
        bomb[0], bomb[1] = int(bomb[0]), int(bomb[1])
        bombs.append(bomb)

    mine_map = [] # list of lists. each list is a row. to find row 3, column 5, you would index it as mine_map[3][5]

    for x in range(R):
        row = []
        for y in range(C):
            row.append(0)
        mine_map.append(row)

    for i, val in enumerate(bombs):
        placeBomb(mine_map,val)

    for i in mine_map:
        for j in i:
            print(j, end="")
        print("")
