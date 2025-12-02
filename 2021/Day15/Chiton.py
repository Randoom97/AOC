import heapq

from input import input

height = len(input)
width = len(input[0])
start = (0,0)
target = (height*5-1, width*5-1)

queue = []
heapq.heappush(queue, (0, start))
visited = set()

def getWeight(pos):
    leftTile = pos[1] // width
    downTile = pos[0] // height
    tilePos = (pos[0] % height, pos[1] % width)
    return (input[tilePos[0]][tilePos[1]] + leftTile + downTile - 1) % 9 + 1


def queueNeighbor(pos, weightSoFar):
    if pos[0] < 0 or pos[0] > target[0] or pos[1] < 0 or pos[1] > target[1] or pos in visited:
        return
    heapq.heappush(queue, (weightSoFar + getWeight(pos), pos))
    

while True:
    (weight, node) = heapq.heappop(queue)
    if node == target:
        break
    if node in visited:
        continue
    visited.add(node)
    queueNeighbor((node[0]-1, node[1]), weight)
    queueNeighbor((node[0]+1, node[1]), weight)
    queueNeighbor((node[0], node[1]-1), weight)
    queueNeighbor((node[0], node[1]+1), weight)

print(weight)