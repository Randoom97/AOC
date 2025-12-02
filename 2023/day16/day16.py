from input import input

Up = 0b1
Right = 0b10
Down = 0b100
Left = 0b1000
height = len(input)
width = len(input[0])

def inBounds(row, col):
    return row >= 0 and row < height and col >= 0 and col < width

def energize(energized, row, col, inDirection):
    energizeStack = [(row, col, inDirection)]
    while energizeStack:
        row, col, inDirection = energizeStack.pop()
        if not inBounds(row, col) or energized[row][col] & inDirection:
            continue
        energized[row][col] ^= inDirection
        symbol = input[row][col]
        if symbol == '.':
            if inDirection == Up: energizeStack.append((row+1, col, inDirection))
            if inDirection == Right: energizeStack.append((row, col-1, inDirection))
            if inDirection == Down: energizeStack.append((row-1, col, inDirection))
            if inDirection == Left: energizeStack.append((row, col+1, inDirection))
        elif symbol == '/':
            if inDirection == Up: energizeStack.append((row, col-1, Right))
            if inDirection == Right: energizeStack.append((row+1, col, Up))
            if inDirection == Down: energizeStack.append((row, col+1, Left))
            if inDirection == Left: energizeStack.append((row-1, col, Down))
        elif symbol == 's': # \
            if inDirection == Up: energizeStack.append((row, col+1, Left))
            if inDirection == Right: energizeStack.append((row-1, col, Down))
            if inDirection == Down: energizeStack.append((row, col-1, Right))
            if inDirection == Left: energizeStack.append((row+1, col, Up))
        elif symbol == '|':
            if inDirection == Left or inDirection == Right:
                energizeStack.append((row+1, col, Up))
                energizeStack.append((row-1, col, Down))
            if inDirection == Up: energizeStack.append((row+1, col, inDirection))
            if inDirection == Down: energizeStack.append((row-1, col, inDirection))
        elif symbol == '-':
            if inDirection == Up or inDirection == Down:
                energizeStack.append((row, col-1, Right))
                energizeStack.append((row, col+1, Left))
            if inDirection == Left: energizeStack.append((row, col+1, inDirection))
            if inDirection == Right: energizeStack.append((row, col-1, inDirection))

def printEnergized(energized):
    print()
    for line in energized:
        strLine = ""
        for tile in line:
            strLine += '#' if tile else '.'
        print(strLine)

maxEnergizedAmmount = 0
maxEnergized = None
# all left edges
for i in range(height):
    energized = [len(line)*[0] for line in input]
    energize(energized, i, 0, Left)
    totalEnergized = 0
    for line in energized:
        for tile in line:
            if tile:
                totalEnergized += 1
    if totalEnergized > maxEnergizedAmmount:
        maxEnergizedAmmount = totalEnergized
        maxEnergized = energized
# all right edges
for i in range(height):
    energized = [len(line)*[0] for line in input]
    energize(energized, i, width-1, Right)
    totalEnergized = 0
    for line in energized:
        for tile in line:
            if tile:
                totalEnergized += 1
    if totalEnergized > maxEnergizedAmmount:
        maxEnergizedAmmount = totalEnergized
        maxEnergized = energized
# all top edges
for i in range(height):
    energized = [len(line)*[0] for line in input]
    energize(energized, 0, i, Up)
    totalEnergized = 0
    for line in energized:
        for tile in line:
            if tile:
                totalEnergized += 1
    if totalEnergized > maxEnergizedAmmount:
        maxEnergizedAmmount = totalEnergized
        maxEnergized = energized
# all bottom edges
for i in range(height):
    energized = [len(line)*[0] for line in input]
    energize(energized, height-1, i, Down)
    totalEnergized = 0
    for line in energized:
        for tile in line:
            if tile:
                totalEnergized += 1
    if totalEnergized > maxEnergizedAmmount:
        maxEnergizedAmmount = totalEnergized
        maxEnergized = energized
printEnergized(maxEnergized)
print(maxEnergizedAmmount)