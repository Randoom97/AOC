from heapq import heappush
from heapq import heappop

from input import maze

def debugPrint(maze, tiles):
    for row in range(len(maze)):
        rowString = ""
        for col in range(len(maze[0])):
            if (row,col) in tiles:
                rowString += "O"
            else:
                if maze[row][col] == '.':
                    rowString += ' '
                else:
                    rowString += "█"
        print(rowString)

def minPath(maze):
    pos = (len(maze)-2, 1)
    heap = []
    visited = {}
    heappush(heap, (0, pos, (0,1), set())) # (score, position, direction)
    minScore = None
    minPath = set()
    checkLater = []
    while len(heap) > 0:
        (score, pos, dir, path) = heappop(heap)
        if (pos,dir) in visited:
            if maze[pos[0]][pos[1]] == 'E' and visited[(pos,dir)] < score:
                break
            if visited[(pos,dir)] == score:
                checkLater.append((pos,dir,path))
            continue
        visited[(pos,dir)] = score
        if maze[pos[0]][pos[1]] == 'E' and minScore != None and score == minScore:
            pathCopy = path.copy()
            pathCopy.add((pos,dir))
            minPath = minPath.union(pathCopy)
            continue
        if maze[pos[0]][pos[1]] == 'E' and minScore == None:
            minScore = score
            pathCopy = path.copy()
            pathCopy.add((pos,dir))
            minPath = pathCopy
            continue
        newPath = path.copy()
        newPath.add((pos,dir))
        if maze[pos[0]+dir[0]][pos[1]+dir[1]] != '#':
            heappush(heap, (score+1, (pos[0]+dir[0], pos[1]+dir[1]), dir, newPath))
        heappush(heap, (score+1000, pos, (-dir[1], dir[0]), newPath)) # counter clock
        heappush(heap, (score+1000, pos, (dir[1], -dir[0]), newPath))

    # check if any of these terminated paths ended up being alternates for the best path
    # warning alternates that attach to alternates exist, so keep checking them until none have been added in a full loop
    hasAdded = True
    checkAgain = []
    while hasAdded:
        hasAdded = False
        for (pos, dir, path) in checkLater:
            if (pos,dir) in minPath:
                hasAdded = True
                minPath = minPath.union(path)
            else:
                checkAgain.append((pos,dir,path))
        checkLater = checkAgain
        checkAgain = []
    
    onlyPositions = set()
    for (pos,dir) in minPath:
        onlyPositions.add(pos)
    debugPrint(maze, onlyPositions)
    return minScore, onlyPositions

(score, path) = minPath(maze)
print(score)
print(len(path))

