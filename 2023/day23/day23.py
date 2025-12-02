from input import input

start = (0, 1)
end = (len(input)-1, len(input[0])-2)

longestPath = 0
stack = []
stack.append((start, set()))
while stack:
    coordinate, history = stack.pop()
    if coordinate == end:
        longestPath = max(longestPath, len(history))
        continue
    if coordinate in history:
        continue
    history.add(coordinate)
    row, col = coordinate
    validDirections = []
    for drow, dcol in [(1,0),(-1,0),(0,1),(0,-1)]:
        if row+drow < 0 or row+drow >= len(input) or col+dcol < 0 or col+dcol >= len(input[0]):
            continue
        if input[row+drow][col+dcol] == '#':
            continue
        if (row+drow, col+dcol) in history:
            continue
        validDirections.append((row+drow, col+dcol))
    if len(validDirections) == 1:
        stack.append((validDirections[0], history))
    else:
        for direction in validDirections:
            stack.append((direction, history.copy()))
print(longestPath)

