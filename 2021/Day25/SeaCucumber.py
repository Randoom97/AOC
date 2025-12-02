import copy

from input import input

grid = []
for line in input:
    grid.append(list(line))
rowCount = len(grid)
colCount = len(grid[0])

iterCount = 0
while True:
    iterCount += 1
    move = False
    # east
    newGrid = copy.deepcopy(grid)
    for row in range(rowCount):
        for col in range(colCount):
            targetCol = col+1
            if col+1 == colCount:
                targetCol = 0
            if grid[row][col] == '>' and grid[row][targetCol] == '.':
                move = True
                newGrid[row][col] = '.'
                newGrid[row][targetCol] = '>'
    # south
    newGrid2 = copy.deepcopy(newGrid)
    for row in range(rowCount):
        for col in range(colCount):
            targetRow = row+1
            if row+1 == rowCount:
                targetRow = 0
            if newGrid[row][col] == 'v' and newGrid[targetRow][col] == '.':
                move = True
                newGrid2[row][col] = '.'
                newGrid2[targetRow][col] = 'v'

    grid = newGrid2

    if not move:
        break

for row in range(rowCount):
    for col in range(colCount):
        print(grid[row][col], end='')
    print('')
print(iterCount)