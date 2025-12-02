from input import input

North = 0b1
East = 0b10
South = 0b100
West = 0b1000

def processMap(map):
    newMap = []
    start = None
    for row, line in enumerate(map):
        newLine = []
        for col, char in enumerate(line):
            if char == '|':
                newLine.append(North | South)
            if char == '-':
                newLine.append(East | West)
            if char == 'L':
                newLine.append(North | East)
            if char == 'J':
                newLine.append(North | West)
            if char == '7':
                newLine.append(South | West)
            if char == 'F':
                newLine.append(South | East)
            if char == '.':
                newLine.append(0)
            if char == 'S':
                newLine.append(North | South | East | West)
                start = (row, col)
        newMap.append(newLine)
    return newMap, start

def inBounds(map, node: tuple[int, int]):
    row, col = node
    return row >= 0 and col >= 0 and row < len(map) and col < len(map[0])

def search(start, map):
    visited = set()
    next = []
    row, col = start
    if inBounds(map, (row-1, col)) and map[row-1][col] & South:
        next.append((row-1, col, 0, start))
    if inBounds(map, (row, col+1)) and map[row][col+1] & West:
        next.append((row, col+1, 0, start))
    if inBounds(map, (row+1, col)) and map[row+1][col] & North:
        next.append((row+1, col, 0, start))
    if inBounds(map, (row, col-1)) and map[row][col-1] & East:
        next.append((row, col-1, 0, start))
    while next:
        previous = next.pop()
        row, col, length, _ = previous
        node = (row, col)
        if node == start and length > 2:
            return previous
        if node in visited:
            continue
        visited.add(node)
        if map[row][col] & North and inBounds(map, (row-1, col)) and map[row-1][col] & South:
            next.append((row-1, col, length+1, previous))
        if map[row][col] & East and inBounds(map, (row, col+1)) and map[row][col+1] & West:
            next.append((row, col+1, length+1, previous))
        if map[row][col] & South and inBounds(map, (row+1, col)) and map[row+1][col] & North:
            next.append((row+1, col, length+1, previous))
        if map[row][col] & West and inBounds(map, (row, col-1)) and map[row][col-1] & East:
            next.append((row, col-1, length+1, previous))
    return None

def fillCount(loop, map):
    visited = set()
    newLoop = set()
    for node in loop:
        newLoop.add(node)
        row, col = node
        tile = map[row][col]
        if tile & North:
            newLoop.add((row-0.5, col))
        if tile & East:
            newLoop.add((row, col+0.5))
        if tile & South:
            newLoop.add((row+0.5, col))
        if tile & West:
            newLoop.add((row, col-0.5))
    next = []
    next.append((0,0))
    while next:
        node = next.pop()
        if node in visited or node in newLoop:
            continue
        visited.add(node)
        row, col = node
        if inBounds(input, (row-0.5, col)):
            next.append((row-0.5, col))
        if inBounds(input, (row+0.5, col)):
            next.append((row+0.5, col))
        if inBounds(input, (row, col-0.5)):
            next.append((row, col-0.5))
        if inBounds(input, (row, col+0.5)):
            next.append((row, col+0.5))
    return len(list(filter(lambda x: x[0] % 1 == 0 and x[1]%1 == 0, visited)))


map, start = processMap(input)
if start != None:
    node = search(start, map)
    if node != None:
        loop = set()
        while len(node) == 4:
            row, col, _, node = node
            loop.add((row, col))
        print(len(input)*len(input[0]) - fillCount(loop, map) - len(loop))
