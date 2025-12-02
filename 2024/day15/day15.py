from input import map, inputs

robotPos = (-1,-1)
boxes = set()
walls = set()

# for row in range(len(map)):
#     for col in range(len(map[0])):
#         token = map[row][col]
#         if token == '@':
#             robotPos = (row, col)
#             boxes.add((row, col))
#         if token == 'O':
#             boxes.add((row, col))
#         if token == '#':
#             walls.add((row, col))

for row in range(len(map)):
    for col in range(len(map[0])):
        token = map[row][col]
        if token == '@':
            robotPos = (row, col*2)
        if token == 'O':
            boxes.add((row, col*2))
        if token == '#':
            walls.add((row, col*2))
            walls.add((row, col*2+1))

def move(item, direction):
    global robotPos

    isRobot = item == robotPos
    scan = (0,0)
    if direction == '<':
        scan = (0,-1)
    if direction == '>':
        scan = (0,1)
    if direction == '^':
        scan = (-1,0)
    if direction == 'v':
        scan = (1,0)

    canMove = True
    newPosition = (item[0]+scan[0], item[1]+scan[1])
    if newPosition in walls:
        return False
    if newPosition in boxes:
        canMove = move(newPosition, direction)
    if canMove:
        if item in boxes:
            boxes.remove(item)
            boxes.add(newPosition)
        if isRobot:
            robotPos = newPosition
    return canMove

def part2move(direction):
    global robotPos
    scan = (0,0)
    if direction == '<':
        scan = (0,-1)
    if direction == '>':
        scan = (0,1)
    if direction == '^':
        scan = (-1,0)
    if direction == 'v':
        scan = (1,0)

    canMove = True
    toMove = []
    moveCheckStack = [robotPos]
    while len(moveCheckStack) > 0:
        item = moveCheckStack.pop()
        toMove.append(item)
        newPos = (item[0]+scan[0], item[1]+scan[1])
        newPosLeft = (newPos[0], newPos[1]-1)
        newPosRight = (newPos[0], newPos[1]+1)
        isRobot = item == robotPos
        if newPos in walls:
            canMove = False
            break
        if not isRobot and newPosRight in walls:
            canMove = False
            break
        if newPos in boxes:
            moveCheckStack.append(newPos)
        if newPosLeft != item and newPosLeft in boxes:
            moveCheckStack.append(newPosLeft)
        if not isRobot and newPosRight != item and newPosRight in boxes:
            moveCheckStack.append(newPosRight)
    if canMove:
        processedSet = set() # something weird going on to have duplicates, but it worked
        toMove.reverse() # make sure we move the last items first
        for item in toMove:
            if item in processedSet:
                continue
            processedSet.add(item)
            if item == robotPos:
                robotPos = (item[0]+scan[0], item[1]+scan[1])
            else:
                boxes.remove(item)
                boxes.add((item[0]+scan[0], item[1]+scan[1]))


            

def debugPrint(part2 = False):
    for row in range(len(map)):
        rowString = ""
        prevBox = False
        for col in range(len(map[0])* (2 if part2 else 1)):
            if (row,col) in walls:
                rowString += "#"
            elif (row,col) == robotPos:
                rowString += "@"
            elif (row,col) in boxes:
                rowString += "[]" if part2 else "O"
                prevBox = True
            elif prevBox:
                prevBox = False
            else:
                rowString += "."
        print(rowString)

for direction in inputs:
    # move(robotPos, direction)
    part2move(direction)
# debugPrint(True)

part1 = 0
for box in boxes:
    part1 += 100*box[0] + box[1]
print(part1)

