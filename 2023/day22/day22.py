from input import input

def processInput(input):
    bricks = []
    for line in input:
        brick = set()
        start, end = line.split('~')
        x1, y1, z1 = [int(coord) for coord in start.split(',')]
        x2, y2, z2 = [int(coord) for coord in end.split(',')]
        if x1 > x2:
            tmp = x1
            x1 = x2
            x2 = tmp
        if y1 > y2:
            tmp = y1
            y1 = y2
            y2 = tmp
        if z1 > z2:
            tmp = z1
            z1 = z2
            z2 = tmp
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    brick.add((x, y, z))
        bricks.append(brick)
    bricks.sort(key = lambda brick: min([tile[2] for tile in brick]))
    return bricks

bricks = processInput(input)
brickMap = {}
supported = {}
for brickIndex, brick in enumerate(bricks):
    dz = 0
    while not any((coord[0], coord[1], coord[2]-dz) in brickMap or coord[2]-dz == 0 for coord in brick):
        dz += 1
    dz = dz-1
    for tile in brick:
        if (tile[0], tile[1], tile[2]-dz-1) in brickMap:
            if brickIndex not in supported:
                supported[brickIndex] = set()
            supported[brickIndex].add(brickMap[(tile[0], tile[1], tile[2]-dz-1)])
    for tile in brick:
        brickMap[(tile[0], tile[1], tile[2]-dz)] = brickIndex
        
supporting = {}
for key in supported:
    values = supported[key]
    for value in values:
        if value not in supporting:
            supporting[value] = set()
        supporting[value].add(key)

def traverseRemove(nodes, indexToRemove):
    stack = []
    for i in range(len(nodes)):
        if i == indexToRemove:
            continue
        if len(nodes[i]['parents']) == 0:
            stack.append(i)
    visited = set()
    while stack:
        currentIdx = stack.pop()
        current = nodes[currentIdx]
        if currentIdx in visited or currentIdx == indexToRemove:
            continue
        visited.add(currentIdx)
        for childIndex in current['children']:
            stack.append(childIndex)
    return visited


nodes = []
for i in range(len(input)):
    node = {}
    node['parents'] = supported[i] if i in supported else set()
    node['children'] = supporting[i] if i in supporting else set()
    nodes.append(node)

total = 0
for i in range(0, len(bricks)):
    dropped = len(input)-1 - len(traverseRemove(nodes, i))
    # print(dropped)
    total += dropped
print(total)