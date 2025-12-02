import math

from input import template, input

mapping = {}
for line in input:
    lineSplit = line.split(" -> ")
    mapping[lineSplit[0]] = lineSplit[1]

polymer = list(template)
pairCounts = {}
for index in range(len(polymer)-1):
    pair = polymer[index: index+2]
    pairStr = pair[0]+pair[1]
    if pairStr not in pairCounts:
        pairCounts[pairStr] = 0
    pairCounts[pairStr] += 1

for i in range(40):
    newPairCounts = pairCounts.copy()
    for pairStr in pairCounts:
        if pairCounts[pairStr] == 0:
            continue
        if pairStr in mapping:
            newPairCounts[pairStr] -= pairCounts[pairStr]
            insertElement = mapping[pairStr]
            firstPair = pairStr[0] + insertElement
            secondPair = insertElement + pairStr[1]
            if firstPair not in newPairCounts:
                newPairCounts[firstPair] = 0
            if secondPair not in newPairCounts:
                newPairCounts[secondPair] = 0
            newPairCounts[firstPair] += pairCounts[pairStr]
            newPairCounts[secondPair] += pairCounts[pairStr]
    pairCounts = newPairCounts

elementMap = {}
for pair in pairCounts:
    if pair[0] not in elementMap:
        elementMap[pair[0]] = 0
    if pair[1] not in elementMap:
        elementMap[pair[1]] = 0
    elementMap[pair[0]] += pairCounts[pair]
    elementMap[pair[1]] += pairCounts[pair]

minElement = float("inf")
maxElement = 0
for element in elementMap:
    count = elementMap[element]
    if count < minElement:
        minElement = count
    if count > maxElement:
        maxElement = count

minElement = math.ceil(minElement/2)
maxElement = math.ceil(maxElement/2)
print(maxElement - minElement)