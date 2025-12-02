from input import input

patterns = [set([(0,0),(1,0),(2,0),(3,0)]), set([(1,2),(0,1),(1,1),(2,1),(1,0)]), set([(2,2),(2,1),(0,0),(1,0),(2,0)]), set([(0,3),(0,2),(0,1),(0,0)]), set([(0,1),(1,1),(0,0),(1,0)])]

solids = set()

highestPoint = -1
def setSolid(point):
    global highestPoint
    highestPoint = max(highestPoint, point[1])
    solids.add(point)

def translate(shape, x, y):
    newSet = set()
    for point in shape:
        newSet.add((point[0]+x, point[1]+y))
    return newSet

def getJetDir(index):
    return input[index % len(input)]

def getPattern(index):
    return patterns[index % len(patterns)]

heightTracker = []
jetIndex = 0
for i in range(2022):
    pattern = translate(getPattern(i), 2, highestPoint+4)

    while True:
        # print('')
        # for y in range(17, -1, -1):
        #     for x in range(7):
        #         if (x,y) in solids:
        #             print('#', end='')
        #         elif (x,y) in pattern:
        #             print('@', end='')
        #         else:
        #             print('.', end='')
        #     print('')

        # Move sideways
        jetDir = getJetDir(jetIndex)
        jetIndex += 1
        if jetDir == '<':
            movedPattern = translate(pattern, -1, 0)
        else:
            movedPattern = translate(pattern, 1, 0)
        valid = True
        for point in movedPattern:
            if point[0] < 0 or point[0] > 6 or point in solids:
                valid = False
                break
        if valid:
            pattern = movedPattern

        # print('')
        # for y in range(17, -1, -1):
        #     for x in range(7):
        #         if (x,y) in solids:
        #             print('#', end='')
        #         elif (x,y) in pattern:
        #             print('@', end='')
        #         else:
        #             print('.', end='')
        #     print('')

        # Move down
        movedPattern = translate(pattern, 0, -1)
        valid = True
        for point in movedPattern:
            if point in solids or point[1] < 0:
                valid = False
                break
        if valid:
            pattern = movedPattern
            continue
        prevHighest = highestPoint
        for point in pattern:
            setSolid(point)
        newHighest = highestPoint
        heightTracker.append(newHighest-prevHighest)
        break

# print('')
# for y in range(17, -1, -1):
#     for x in range(7):
#         if (x,y) in solids:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print('')

print(heightTracker)

print(highestPoint+1)







        