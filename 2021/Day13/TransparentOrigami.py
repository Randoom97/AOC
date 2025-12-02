from input import input

points = set(input[0])

instruction = input[1][0]
for instruction in input[1]:
    parts = instruction.split("=")
    axis = 1 if parts[0][-1] == 'y' else 0
    pos = int(parts[1])
    newPoints = set()
    for point in points:
        if point[axis] > pos:
            newPos = pos - (point[axis] - pos)
            if axis == 1:
                point = (point[0], newPos)
            else:
                point = (newPos, point[1])
        newPoints.add(point)
    points = newPoints

maxy = 0
maxx = 0
for point in points:
    if point[0] > maxx:
        maxx = point[0]
    if point[1] > maxy:
        maxy = point[1]

grid = []
for y in range(maxy+1):
    grid.append([' ']*(maxx+1))

for point in points:
    grid[point[1]][point[0]] = '█'

for y in range(maxy+1):
    for x in range(maxx+1):
        print(grid[y][x], end='')
    print()