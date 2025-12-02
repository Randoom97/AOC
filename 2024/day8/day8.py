from input import input

nodeMap = {}

for row in range(len(input)):
    for col in range(len(input[0])):
        key = input[row][col]
        if key != '.':
            if key not in nodeMap:
                nodeMap[key] = []
            nodeMap[key].append((row, col))

antinodes = set()
for key in nodeMap:
    nodes = nodeMap[key]
    for i1 in range(len(nodes)):
        node1 = nodes[i1]
        for i2 in range(i1+1, len(nodes)):
            node2 = nodes[i2]
            distRow = node1[0] - node2[0]
            distCol = node1[1] - node2[1]
            for i in range(max(len(input), len(input[0]))):
                antinodes.add((node1[0]+distRow*i, node1[1]+distCol*i))
                antinodes.add((node2[0]-distRow*i, node2[1]-distCol*i))

def debugPrint():
    for row in range(len(input)):
        rowString = ""
        for col in range(len(input[0])):
            if input[row][col] != '.':
                rowString += input[row][col]
            elif (row, col) in antinodes:
                rowString += "#"
            else:
                rowString += '.'
        print(rowString)

antinodeCount = 0
for (row, col) in antinodes:
    if row < 0 or row >= len(input) or col < 0 or col >= len(input[0]):
        continue
    antinodeCount += 1
print(antinodeCount)