from input import map

def printDebugPath(map, items):
    for row in range(len(map)):
        rowString = ""
        for col in range(len(map[0])):
            if (row, col) in items:
                rowString += "O"
            else:
                rowString += map[row][col]
        print(rowString)

def preprocess(map):
    guard = (-1,-1,0,0)
    obstructions = set()
    for row in range(len(map)):
        for col in range(len(map[0])):
            tile = map[row][col]
            if tile == '#':
                obstructions.add((row, col))
            if tile == '^':
                guard = (row, col, -1, 0)
            if tile == '>':
                guard = (row, col, 0, 1)
            if tile == '<':
                guard = (row, col, 0, -1)
            if tile == 'v':
                guard = (row, col, 1, 0)
    return (guard, obstructions)

def pathLength(guard, obstructions: set, addObstruction):
    guardStart = guard
    guardPath = set()
    pastGuard = set()
    loopObstructions = set()
    while True:
        guardPath.add((guard[0], guard[1]))
        if guard in pastGuard:
            return -1, loopObstructions # infinite loop
        pastGuard.add(guard)
        nrow = guard[0] + guard[2]
        ncol = guard[1] + guard[3]
        if nrow < 0 or nrow >= len(map) or ncol < 0 or ncol >= len(map[0]):
            return len(guardPath), loopObstructions
        if (nrow, ncol) in obstructions:
            guard = (guard[0], guard[1], guard[3], -guard[2])
        else:
            if addObstruction:
                obstructions.add((nrow, ncol))
                if pathLength(guardStart, obstructions, False)[0] == -1:
                    loopObstructions.add((nrow, ncol))
                obstructions.remove((nrow, ncol))
            guard = (nrow, ncol, guard[2], guard[3])
    

guard, obstructions = preprocess(map)
length, loopObstructions = pathLength(guard, obstructions, True)

if (guard[0], guard[1]) in loopObstructions:
    loopObstructions.remove((guard[0], guard[1]))
    
# part 1
print(length)
# part 2
print(len(loopObstructions))



