from input import map

def getPosition(char, map):
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == char:
                return (row,col)
    return (-1,-1)

def computeDistMap(end, map):
    queue = [(end, 0)]
    distMap = {}
    while len(queue) > 0:
        pos, dist = queue.pop(0)
        row, col = pos
        if map[row][col] == '#':
            continue
        if pos in distMap:
            continue
        distMap[pos] = dist
        queue.append(((row-1,col), dist+1))
        queue.append(((row+1,col), dist+1))
        queue.append(((row,col-1), dist+1))
        queue.append(((row,col+1), dist+1))
    return distMap

def findShortcuts(distMap, map, cheatLength):
    shortcutCount = {}
    for startPos in distMap:
        queue = [(startPos, cheatLength)]
        visited = set()
        while len(queue) > 0:
            pos, cheatAmmount = queue.pop(0)
            if pos in visited:
                continue
            visited.add(pos)
            if pos in distMap:
                saved = distMap[startPos] - (distMap[pos]+cheatLength-cheatAmmount)
                if saved > 0:
                    if saved not in shortcutCount:
                        shortcutCount[saved] = set()
                    shortcutCount[saved].add((startPos, pos))
            if cheatAmmount == 0:
                continue
            row, col = pos
            if row-1 >= 0:
                queue.append(((row-1,col), cheatAmmount-1))
            if row+1 < len(map):
                queue.append(((row+1,col), cheatAmmount-1))
            if col-1 >= 0:
                queue.append(((row,col-1), cheatAmmount-1))
            if col+1 < len(map[0]):
                queue.append(((row,col+1), cheatAmmount-1))
    return shortcutCount

end = getPosition('E', map)
distMap = computeDistMap(end, map)
shortcutCounts = findShortcuts(distMap, map, 20)
atLeast100 = 0
# savedPairs = []
for saved in shortcutCounts:
    # savedPairs.append((saved, shortcutCounts[saved]))
    if saved >= 100:
        atLeast100 += len(shortcutCounts[saved])
# savedPairs.sort()
# for (saved, paths) in savedPairs:
#     print("There are "+str(len(paths))+" cheats that save "+str(saved)+" picoseconds.")
print(atLeast100)