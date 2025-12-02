from input import input

def preprocess(data):
    newData = []
    for i in range(len(data)):
        newData.append(((i//2) if i % 2 == 0 else -1, int(data[i])))
    return newData

def part1(data):
    newData = []
    data = preprocess(data)
    leftIdx = 0
    left = data[leftIdx]
    rightIdx = len(data)-1
    right = data[rightIdx]
    while leftIdx < rightIdx:
        if left[0] >= 0:
            newData.append(left)
            leftIdx += 1
            left = data[leftIdx]
        else:
            if left[1] >= right[1]:
                newData.append(right)
                left = (left[0], left[1]-right[1])
                if rightIdx - 2 < leftIdx:
                    break
                rightIdx -= 2
                right = data[rightIdx]
                continue
            elif left[1] == 0:
                if leftIdx + 1 >= rightIdx:
                    break
                leftIdx += 1
                left = data[leftIdx]
            else:
                newData.append((right[0], left[1]))
                right = (right[0], right[1]-left[1])
                if leftIdx+1 >= rightIdx:
                    break
                leftIdx += 1
                left = data[leftIdx]
                continue
    if left[0] > 0:
        newData.append(left)
    elif right[0] > 0:
        newData.append(right)
    return checksum(newData)


# data format array of tuples of (id, size). if id is negative empty space
def checksum(data):
    count = 0
    index = 0
    for (id, size) in data:
        if id <= 0:
            index += size
        else:
            for _ in range(size):
                count += index*id
                index += 1
    return count
        
def debugPrint(data):
    string = ""
    for (id, size) in data:
        for _ in range(size):
            if id < 0:
                string += '.'
            else:
                string += str(id)
    print(string)

def collapseEmpty(data):
    newData = []
    for i in range(len(data)):
        if data[i][1] == 0:
            continue
        if data[i][0] >= 0:
            newData.append(data[i])
        else:
            if len(newData) > 0 and newData[len(newData)-1][0] == -1:
                left = newData.pop()
                newData.append((-1, left[1] + data[i][1]))
            else:
                newData.append(data[i])
    return newData

def part2(data):
    data = preprocess(data)
    dataCopy = data.copy()
    rightIdx = len(data)-1
    right = data[rightIdx]
    for i in range(0, len(dataCopy), 2):
        right = dataCopy[len(dataCopy)-1-i]
        # print(right)
        for j in range(len(data)):
            if data[j][0] == right[0]:
                break
            if data[j][0] >= 0:
                continue
            if data[j][1] < right[1]:
                continue
            data[j] = (data[j][0], data[j][1] - right[1])
            oldIdx = data.index(right)
            data.insert(oldIdx, (-1, right[1]))
            data.remove(right)
            data.insert(j, right)
            data = collapseEmpty(data)
            break
    # print(data)
    return checksum(data)


print(part2(input))