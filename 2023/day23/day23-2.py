from input import input

def processInput():
    intersections = {}
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == '#':
                continue
            validDirections = []
            for drow, dcol in [(1,0), (-1,0), (0,1), (0,-1)]:
                if row+drow < 0 or row+drow >= len(input) or col+dcol < 0 or col+dcol >= len(input[0]):
                    continue
                if input[row+drow][col+dcol] != '#':
                    validDirections.append((row+drow, col+dcol))
            if len(validDirections) > 2:
                intersections[(row, col)] = validDirections
    intersections[(0,1)] = [(1,1)]
    intersections[(len(input)-1, len(input[0])-2)] = [(len(input)-2, len(input[0])-2)]
    return intersections

def convertIntersectionsToLenghts(intersections):
    lengths = {}
    for intersection in intersections:
        lengths[intersection] = {}
        for direction in intersections[intersection]:
            stack = []
            stack.append((direction, 1))
            visited = set()
            visited.add(intersection)
            while stack:
                node, length = stack.pop()
                if node in intersections:
                    lengths[intersection][node] = length
                    break
                if node in visited:
                    continue
                visited.add(node)
                row, col = node
                for drow, dcol in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if input[row+drow][col+dcol] == '#':
                        continue
                    if (row+drow, col+dcol) in visited:
                        continue
                    stack.append(((row+drow, col+dcol), length+1))
    return lengths



lengths = convertIntersectionsToLenghts(processInput())
for key in lengths:
    print(str(key) + ": " + str(lengths[key]))
print()

maxLength = 0
stack = []
stack.append(((0,1), {}))
while stack:
    node, history = stack.pop()
    if node == (len(input)-1, len(input[0])-2):
        maxLength = max(maxLength, sum([history[key] for key in history]))
        continue
    if node in history:
        continue
    for next in lengths[node]:
        historyCopy = history.copy()
        historyCopy[node] = lengths[node][next]
        stack.append((next, historyCopy))
print(maxLength)

