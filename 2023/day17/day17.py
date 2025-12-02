import heapq

from input import input

def processInput():
    map = []
    for line in input:
        mapRow = []
        for char in line:
            mapRow.append(int(char))
        map.append(mapRow)
    return map

map = processInput()
def inBounds(row, col):
    return row >= 0 and row < len(map) and col >= 0 and col < len(map[0])

def reverseDirection(direction):
    row, col = direction
    return (-1*row, -1*col)

# heat loss, coordinate, distance in a line, direction
queue = []
heapq.heappush(queue, (0, (0,0), 0, (0,0), []))
visited = set()
path = None
totalLoss = 0
while queue:
    current = heapq.heappop(queue)
    loss, coordinate, lineDistance, direction, past = current
    if (coordinate, lineDistance, direction) in visited:
        continue
    if coordinate == (len(map)-1, len(map[0])-1) and lineDistance >= 4:
        totalLoss = loss
        path = past
        break
    visited.add((coordinate, lineDistance, direction))
    for newDirection in [(1,0), (0,1), (-1, 0), (0, -1)]:
        if lineDistance < 4 and direction != (0,0) and newDirection != direction:
            continue
        # can't reverse direction
        if newDirection == reverseDirection(direction):
            continue
        newRow = coordinate[0]+newDirection[0]
        newCol = coordinate[1]+newDirection[1]
        # can't go out of bounds
        if not inBounds(newRow, newCol):
            continue
        # can't go in a straight line for more than 3 tiles
        if direction == newDirection:
            if lineDistance >= 10:
                continue
            heapq.heappush(queue, (loss+map[newRow][newCol], (newRow, newCol), lineDistance+1, direction, [*past, coordinate]))
            continue
        heapq.heappush(queue, (loss+map[newRow][newCol], (newRow, newCol), 1, newDirection, [*past, coordinate]))

print(totalLoss)
print(path)