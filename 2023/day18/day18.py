from input import input

row = 0
col = 0
corners = []
for line in input:
    _, _, color = line.split()
    distance = int(color[2:7], 16)
    direction = color[7:8]
    if direction == '3': row -= distance
    if direction == '1': row += distance
    if direction == '2': col -= distance
    if direction == '0': col += distance
    corners.append((row, col))

def fillCount(corners):
    total = 1
    cornersLen = len(corners)
    for i in range(cornersLen):
        p1 = corners[i]
        p2 = corners[(i+1)%cornersLen]
        total += ((p1[0]+p2[0]) * (p1[1] - p2[1]))/2
        total += (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) / 2
    return total


print(fillCount(corners))
    
