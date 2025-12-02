from input import input

def processMap(mapString):
    start = None
    map = {}
    map['height'] = len(mapString)
    map['width'] = len(mapString[0])
    map['rocks'] = set()
    for row in range(len(mapString)):
        for col in range(len(mapString[0])):
            if mapString[row][col] == 'S':
                start = (row, col)
            if mapString[row][col] == '#':
                map['rocks'].add((row, col))
    return start, map

def possibleReach(start, map, maxSteps):
    total = 0
    width = map['width']
    height = map['height']
    visited = set()
    stack = []
    stack.append((start[0],start[1],0))
    while stack:
        row, col, steps = stack.pop(0)
        if steps > maxSteps or (row, col) in visited:
            continue
        visited.add((row, col))
        if steps%2 == maxSteps%2:
            total+=1
        directions = [(0,-1), (-1,0), (0,1), (1,0)]
        for direction in directions:
            rowDelta, colDelta = direction
            if ((row+rowDelta)%height, (col+colDelta)%width) in map['rocks']:
                continue
            stack.append((row+rowDelta, col+colDelta, steps+1))
    return total

steps = 26501365%131
print(steps)
start, map = processMap(input)
reachableTiles = possibleReach(start, map, steps)
for i in range(5):
    print(possibleReach(start, map, steps+(131*i)))

# magic numbers computed as quadratic formula from above data
# steps = 26501365//131
# print(15427*(steps**2) + 15560*steps + 3921)
