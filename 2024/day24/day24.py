import random

from input import initialState, functions

computeCache = initialState.copy()
def compute(varName):
    if varName in computeCache:
        return computeCache[varName]
    leftName, operator, rightName = functions[varName]
    leftValue = compute(leftName)
    rightValue = compute(rightName)
    match operator:
        case "AND":
            value = leftValue & rightValue
        case "OR":
            value = leftValue | rightValue
        case "XOR":
            value = leftValue ^ rightValue
    computeCache[varName] = value
    return value

def getUpstream(varName):
    global functions
    upstream = set()
    stack = [varName]
    while len(stack) > 0:
        item = stack.pop()
        if item in functions and item not in upstream:
            upstream.add(item)
            left, _, right = functions[item]
            stack.append(left)
            stack.append(right)
    return upstream

def getPotentialIncorrectFunctions(incorrectBits):
    incorrectFunctions = set()
    i = 0
    while incorrectBits > 0:
        if incorrectBits & 0b1:    
            stack = ["z"+str(i).zfill(2)]
            while len(stack) > 0:
                item = stack.pop()
                if item in functions and item not in incorrectFunctions:
                    incorrectFunctions.add(item)
                    left, _, right = functions[item]
                    stack.append(left)
                    stack.append(right)
        i += 1
        incorrectBits >>= 1
    return incorrectFunctions

value = 0
i = 0
while "z"+str(i).zfill(2) in functions:
    value += compute("z"+str(i).zfill(2)) << i
    i += 1
print(value)

swaps = [("z12","fgc"),("z29","mtj"), ("dgr","vvm"), ("z37","dtv")]
for swap in swaps:
    temp = functions[swap[0]]
    functions[swap[0]] = functions[swap[1]]
    functions[swap[1]] = temp

alreadyPrinted = set()
for i in range(45): 
    zstring = "z"+str(i).zfill(2)
    print("upstream of "+zstring)
    upstreams = getUpstream(zstring)
    for upstream in upstreams:
        if upstream in alreadyPrinted:
            continue
        alreadyPrinted.add(upstream)
        print(str(upstream)+": "+str(functions[upstream]))
    print()

outputList = []
for swap in swaps:
    outputList.append(swap[0])
    outputList.append(swap[1])
outputList.sort()
print(",".join(outputList))
