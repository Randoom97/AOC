from input import input

rowDim = len(input)
colDim = len(input[0])

def leftHigher(row, col):
    return row - 1 < 0 or input[row-1][col] > input[row][col]
def rightHigher(row, col):
    return row + 1 >= rowDim or input[row+1][col] > input[row][col]
def upHigher(row, col):
    return col - 1 < 0 or input[row][col-1] > input[row][col]
def downHigher(row, col):
    return col +1 >= colDim or input[row][col+1] > input[row][col]

def calcBasinSize(row, col, visited: set):
    posKey = str(row)+":"+str(col)
    if row < 0 or row >= rowDim or col < 0 or col >= colDim or input[row][col] == 9 or visited.__contains__(posKey):
        return 0
    visited.add(posKey)
    return 1 + calcBasinSize(row-1, col, visited) + calcBasinSize(row+1, col, visited) + calcBasinSize(row, col-1, visited) + calcBasinSize(row, col+1, visited)

lowPoints = []
for row in range(rowDim):
    for col in range(colDim):
        height = input[row][col]
        if leftHigher(row, col) and rightHigher(row, col) and upHigher(row, col) and downHigher(row, col):
            lowPoints.append((row, col))

basinSizes = []
for lowPoint in lowPoints:
    visited = set()
    basinSizes.append(calcBasinSize(lowPoint[0], lowPoint[1], visited))

basinSizes.sort(reverse=True)
print(basinSizes[0]*basinSizes[1]*basinSizes[2])