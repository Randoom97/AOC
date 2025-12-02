import math
import copy

def magnitude(number):
    if isinstance(number[0], int):
        left = 3*number[0]
    else:
        left = 3*magnitude(number[0])
    if isinstance(number[1], int):
        right = 2*number[1]
    else:
        right = 2*magnitude(number[1])
    return left+right

def add(number1, number2):
    return reduce([number1, number2])

def explode(number, i1, i2, i3, i4):
    left = number[i1][i2][i3][i4][0]
    right = number[i1][i2][i3][i4][1]

    # sum left
    if i4 != 0:
        leftNumber = number[i1][i2][i3][i4-1]
        if isinstance(leftNumber, int):
            number[i1][i2][i3][i4-1] += left
    elif i3 != 0:
        leftNumber = number[i1][i2][i3-1]
        if isinstance(leftNumber, int):
            number[i1][i2][i3-1] += left
    elif i2 != 0:
        leftNumber = number[i1][i2-1]
        if isinstance(leftNumber, int):
            number[i1][i2-1] += left
    elif i1 != 0:
        leftNumber = number[i1-1]
        if isinstance(leftNumber, int):
            number[i1-1] += left
    else:
        leftNumber = None

    if leftNumber != None and not isinstance(leftNumber, int):
        while not isinstance(leftNumber[1], int):
            leftNumber = leftNumber[1]
        leftNumber[1] += left

    # sum right
    if i4 < len(number[i1][i2][i3]) - 1:
        rightNumber = number[i1][i2][i3][i4+1]
        if isinstance(rightNumber, int):
            number[i1][i2][i3][i4+1] += right
    elif i3 < len(number[i1][i2]) - 1:
        rightNumber = number[i1][i2][i3+1]
        if isinstance(rightNumber, int):
            number[i1][i2][i3+1] += right
    elif i2 < len(number[i1]) - 1:
        rightNumber = number[i1][i2+1]
        if isinstance(rightNumber, int):
            number[i1][i2+1] += right
    elif i1 < len(number) - 1:
        rightNumber = number[i1+1]
        if isinstance(rightNumber, int):
            number[i1+1] += right
    else:
        rightNumber = None
    
    if rightNumber != None and not isinstance(rightNumber, int):
        while not isinstance(rightNumber[0], int):
            rightNumber = rightNumber[0]
        rightNumber[0] += right

    # reset to 0
    number[i1][i2][i3][i4] = 0
    

def split(number):
    return [math.floor(number/2), math.ceil(number/2)]

def reduce(number):
    # check for nest of 4
    for i1, number_1 in enumerate(number):
        if isinstance(number_1, int):
            continue
        for i2, number_2 in enumerate(number_1):
            if isinstance(number_2, int):
                continue
            for i3, number_3 in enumerate(number_2):
                if isinstance(number_3, int):
                    continue
                for i4, number_4 in enumerate(number_3):
                    if isinstance(number_4, int):
                        continue
                    explode(number, i1, i2, i3, i4)
                    return reduce(number)
    # check for any regular number 10 or greater
    for i1, number_1 in enumerate(number):
        if isinstance(number_1, int):
            if number_1 >= 10:
                number[i1] = split(number_1)
                return reduce(number)
            continue
        for i2, number_2 in enumerate(number_1):
            if isinstance(number_2, int):
                if number_2 >= 10:
                    number[i1][i2] = split(number_2)
                    return reduce(number)
                continue
            for i3, number_3 in enumerate(number_2):
                if isinstance(number_3, int):
                    if number_3 >= 10:
                        number[i1][i2][i3] = split(number_3)
                        return reduce(number)
                    continue
                for i4, number_4 in enumerate(number_3):
                    if number_4 >= 10:
                        number[i1][i2][i3][i4] = split(number_4)
                        return reduce(number)
    return number

from input import input

maxMag = 0
for i1, number1 in enumerate(input):
    for i2, number2 in enumerate(input):
        if i1 == i2:
            continue
        number1c = copy.deepcopy(number1)
        number2c = copy.deepcopy(number2)
        mag = magnitude(add(number1c, number2c))
        if mag > maxMag:
            maxMag = mag
print(maxMag)