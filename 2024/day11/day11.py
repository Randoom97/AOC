from input import input

def preprocess(stones):
    stoneMap = {}
    for stone in stones:
        if stone not in stoneMap:
            stoneMap[stone] = 0
        stoneMap[stone] += 1
    return stoneMap

def step(stoneMap):
    newStoneMap = {}
    for stone in stoneMap:
        stoneCount = stoneMap[stone]
        if stone == 0:
            if 1 not in newStoneMap:
                newStoneMap[1] = 0
            newStoneMap[1] += stoneCount
            continue
        stoneString = str(stone)
        if len(stoneString)%2 == 0:
            left = int(stoneString[:len(stoneString)//2])
            if left not in newStoneMap:
                newStoneMap[left] = 0
            newStoneMap[left] += stoneCount

            right = int(stoneString[len(stoneString)//2:])
            if right not in newStoneMap:
                newStoneMap[right] = 0
            newStoneMap[right] += stoneCount
            continue
        if stone*2024 not in newStoneMap:
            newStoneMap[stone*2024] = 0
        newStoneMap[stone*2024] += stoneCount
    return newStoneMap

stones = preprocess(input)
for i in range(75):
    stones = step(stones)

count = 0
for stone in stones:
    count += stones[stone]
print(len(stones))
print(count)