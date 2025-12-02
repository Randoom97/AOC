from input import input

def transformInput(input):
    map = {
        'rocks': set(),
        'blocks': set(),
        'width': len(input[0]),
        'height': len(input)
    }
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            if char == 'O':
                map['rocks'].add((row,col))
            if char == '#':
                map['blocks'].add((row,col))
    return map

def inBounds(row, col, width, height):
    return row >= 0 and row < height and col >= 0 and col < width

def roll(map, direction):
    width = map['width']
    height = map['height']
    northSouth, eastWest = direction
    oldRocks = list(map['rocks'])
    oldRocks.sort(key=lambda x: x[0] if northSouth else x[1], reverse=northSouth == 1 or eastWest == 1)
    map['rocks'] = set()
    for oldRock in oldRocks:
        row, col = oldRock
        while inBounds(row+northSouth, col+eastWest, width, height) and (row + northSouth, col + eastWest) not in map['blocks'] and (row + northSouth, col + eastWest) not in map['rocks']:
            row += northSouth
            col += eastWest
        map['rocks'].add((row, col))

def printMap(map):
    print()
    for row in range(map['height']):
        line = ""
        for col in range(map['width']):
            if (row, col) in map['blocks']:
                line += '#'
            elif (row, col) in map['rocks']:
                line += 'O'
            else:
                line += '.'
        print(line)
            

def computeLoad(rocks, height):
    load = 0
    for rock in rocks:
        load += height-rock[0]
    return load

def spin(map):
    roll(map, (-1, 0))
    roll(map, (0, -1))
    roll(map, (1, 0))
    roll(map, (0, 1))

map = transformInput(input)
previousRocks = []
loopCount = 1000000000
loopStart = None
loopEnd = None
for i in range(loopCount):
    spin(map)
    for prevIdx, prev in enumerate(previousRocks):
        if map['rocks'] == prev:
            loopStart = prevIdx
            loopEnd = i
            break
    previousRocks.append(map['rocks'])
    if loopEnd:
        break

print("loop started on " + str(loopStart) + " ended on " + str(loopEnd))
if loopStart != None and loopEnd != None:
    rockIndex = (loopCount - loopStart) % (loopEnd-loopStart)
    print(computeLoad(previousRocks[rockIndex + loopStart-1], map['height']))
# print()
# for prev in previousRocks:
#     print(computeLoad(prev, map['height']))
# print(computeLoad(map['rocks'], map['height']))


