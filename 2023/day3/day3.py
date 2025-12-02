from input import input

height = len(input)
width = len(input[0])

def isDigit(char: str):
    return char >= '0' and char <= '9'

def extractNumberStarts(input):
    total = 0
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            if char != '*':
                continue
            numberStarts = set()
            for subRow in range(row-1, row+2):
                for subCol in range(col-1, col+2):
                    if subRow < 0 or subRow >= height or subCol < 0 or subCol >= width or not isDigit(input[subRow][subCol]):
                        continue
                    left = subCol
                    while left >= 0 and isDigit(input[subRow][left]):
                        left -= 1
                    numberStarts.add((subRow, left+1))
            if len(numberStarts) == 2:
                numbers = extractNumbers(numberStarts, input)
                gearRatio = numbers[0] * numbers[1]
                total += gearRatio
    return total

def extractNumbers(numberStarts, input):
    numbers = []
    for (row, col) in numberStarts:
        right = col
        while right < width and isDigit(input[row][right]):
            right += 1
        numbers.append(int(input[row][col:right]))
    return numbers

print(extractNumberStarts(input))