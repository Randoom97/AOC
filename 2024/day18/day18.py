from input import data, gridSize, corruptedAmmount

def getObstructions(count):
    obstruction = set()
    for i in range(count):
        obstruction.add((data[i][1], data[i][0]))
    return obstruction

def bfs(obstructions):
    shortestPath = set()
    queue = [((0,0),set())]
    visited = set()
    while len(queue) > 0:
        (loc, path) = queue.pop(0)
        if loc in visited:
            continue
        if loc in obstructions:
            continue
        if loc == (gridSize, gridSize):
            shortestPath = path.copy()
            shortestPath.add(loc)
            break
        visited.add(loc)
        newPath = path.copy()
        newPath.add(loc)
        (row,col) = loc
        if row-1 >= 0:
            queue.append(((row-1, col), newPath))
        if row+1 <= gridSize:
            queue.append(((row+1,col), newPath))
        if col-1 >= 0:
            queue.append(((row,col-1), newPath))
        if col+1 <= gridSize:
            queue.append(((row,col+1), newPath))
    return shortestPath

def debugPrint(path, obstructions):
    for row in range(gridSize+1):
        rowString = ""
        for col in range(gridSize+1):
            if (row,col) in path:
                rowString += "O"
            elif (row,col) in obstructions:
                rowString += "█"
            else:
                rowString += '.'
        print(rowString)

# obstructions = getObstructions(corruptedAmmount)
# path = bfs(getObstructions(corruptedAmmount))
# debugPrint(path, obstructions)
# print(len(path)-1)

low = 0
high = len(data)
while low < high:
    mid = (low+high)//2
    obst = getObstructions(mid)
    path = bfs(obst)
    if len(path) > 0:
        low = mid+1
    else:
        high = mid
print(low)
print(data[low-1])
print(high)
print(data[high-1])
