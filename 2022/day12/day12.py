from input import input

rowCount = len(input)
colCount = len(input[0])


col = None
for row in range(len(input)):
    rowData = input[row]
    try:
        col = rowData.index('E')
    finally:
        if col != None:
            break
        continue

visited = set()
checkQueue = [(row, col, [])]

def visit(loc):
    global visited, input, checkQueue
    row = loc[0]
    col = loc[1]
    if input[row][col] == 'a' or input[row][col] == 'S':
        return True
    if (row, col) in visited: 
        return False
    visited.add((row, col))
    queue(loc, (row-1, col, loc[2]+[(row, col)]))
    queue(loc, (row+1, col, loc[2]+[(row, col)]))
    queue(loc, (row, col-1, loc[2]+[(row, col)]))
    queue(loc, (row, col+1, loc[2]+[(row, col)]))
    return False

def queue(fromLoc, loc):
    global rowCount, colCount, visited, input, checkQueue
    row = loc[0]
    col = loc[1]
    if (row, col) in visited or row < 0 or row >= rowCount or col < 0 or col >= colCount:
        return
    fromHeight = ord(input[fromLoc[0]][fromLoc[1]]) if input[fromLoc[0]][fromLoc[1]] != 'E' else ord('z')
    height = ord(input[row][col]) if input[row][col] != 'S' else ord('a')
    if fromHeight - height > 1:
        return
    checkQueue.append(loc)

def printVisited():
    global visited
    outputStr = ''
    for row in range(rowCount):
        for col in range(colCount):
            if (row, col) in visited:
                outputStr += '#'
            else:
                outputStr += '.'
        outputStr += "\r\n"
    print(outputStr)

while len(checkQueue) > 0:
    checking = checkQueue.pop(0)
    if visit(checking):
        print(len(checking[2]))
        # print(checking[2])
        break

