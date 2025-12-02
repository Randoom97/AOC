from input import input

def part1():
    count = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] != '0':
                continue
            stack = [(row, col)]
            endSet = set()
            while len(stack) != 0:
                (r, c) = stack.pop()
                target = str(int(input[r][c])+1)
                if input[r][c] == '9':
                    endSet.add((r, c))
                    continue
                if r-1 >= 0 and input[r-1][c] == target:
                    stack.append((r-1, c))
                if c-1 >= 0 and input[r][c-1] == target:
                    stack.append((r, c-1))
                if r+1 < len(input) and input[r+1][c] == target:
                    stack.append((r+1, c))
                if c+1 < len(input[0]) and input[r][c+1] == target:
                    stack.append((r, c+1))
            count += len(endSet)
    print(count)

def part2():
    count = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] != '0':
                continue
            stack = [(row, col)]
            pathCount = 0
            while len(stack) != 0:
                (r, c) = stack.pop()
                target = str(int(input[r][c])+1)
                if input[r][c] == '9':
                    pathCount += 1
                    continue
                if r-1 >= 0 and input[r-1][c] == target:
                    stack.append((r-1, c))
                if c-1 >= 0 and input[r][c-1] == target:
                    stack.append((r, c-1))
                if r+1 < len(input) and input[r+1][c] == target:
                    stack.append((r+1, c))
                if c+1 < len(input[0]) and input[r][c+1] == target:
                    stack.append((r, c+1))
            count += pathCount
    print(count)

# part1()
part2()