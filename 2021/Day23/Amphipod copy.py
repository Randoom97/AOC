import heapq

from input import input

energyCosts = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
correctColumns={'A': 2, 'B': 4, 'C': 6, 'D': 8}
validHalwayColumns=[0,1,3,5,7,9,10]

correctStates = set([('A', (2,1)), ('A', (2,2)), ('A', (2,3)), ('A', (2,4)), ('B', (4,1)), ('B', (4,2)), ('B', (4,3)), ('B', (4,4)), ('C', (6,1)), ('C', (6,2)), ('C', (6,3)), ('C', (6,4)), ('D', (8,1)), ('D', (8,2)), ('D', (8,3)), ('D', (8,4))])
def isFinalState(state):
    inCorrectPosCount = 0
    for i in range(16):
        if state[i] in correctStates:
            inCorrectPosCount += 1
    return inCorrectPosCount == 16
    

def canMoveTo(fromPos, toPos, occupied):
    stepDir = (toPos[0]-fromPos[0])//abs(toPos[0]-fromPos[0])
    xpos = fromPos[0]
    ypos = fromPos[1]
    if fromPos[1] == 0:
        while xpos != toPos[0]:
            xpos += stepDir
            if (xpos, ypos) in occupied:
                return False
        while ypos != toPos[1]:
            ypos += 1
            if (xpos, ypos) in occupied:
                return False
        return True
    else:
        while ypos != toPos[1]:
            ypos -= 1
            if (xpos, ypos) in occupied:
                return False
        while xpos != toPos[0]:
            xpos += stepDir
            if (xpos, ypos) in occupied:
                return False
        return True

def createNewState(oldState, oldAmphipod, newAmphipod):
    newState = list(oldState)
    index = 0
    for idx, amphipod in enumerate(newState):
        if amphipod == oldAmphipod:
            index = idx
            break
    newState[index] = newAmphipod
    return (newState[0], newState[1], newState[2], newState[3], newState[4], newState[5], newState[6], newState[7], newState[8], newState[9], newState[10], newState[11], newState[12], newState[13], newState[14], newState[15])

def cost(type, fromPos, toPos):
    return energyCosts[type]*(abs(fromPos[0]-toPos[0])+abs(fromPos[1]-toPos[1]))

def genNeighborStates(state, weight):
    neighborStates = []
    amphipods = set(state)
    occupied = set()
    for amphipod in amphipods:
        occupied.add(amphipod[1])
    for amphipod in amphipods:
        if amphipod[1][1] == 0:
            # in hallway
            canMoveIntoRoom = False
            for y in range(4, 0, -1):
                if (correctColumns[amphipod[0]], y) not in occupied:
                    canMoveIntoRoom = True
                    break
                elif (amphipod[0], (correctColumns[amphipod[0]], y)) not in amphipods:
                    break
            if canMoveIntoRoom and canMoveTo(amphipod[1], (correctColumns[amphipod[0]], y), occupied):
                neighborStates.append(((weight + cost(amphipod[0], amphipod[1], (correctColumns[amphipod[0]], y))), createNewState(state, amphipod, (amphipod[0], (correctColumns[amphipod[0]], y)))))
        elif amphipod[1][1] >= 1:
            blockingIncorrect = False
            if amphipod[1][1] != 4:
                for i in range(amphipod[1][1]+1, 5):
                    if (amphipod[0], (amphipod[1][0], i)) not in amphipods:
                        blockingIncorrect = True
                        break
            if blockingIncorrect or amphipod not in correctStates:
                for validHallwayColumn in validHalwayColumns:
                    if canMoveTo(amphipod[1], (validHallwayColumn, 0), occupied):
                        neighborStates.append(((weight + cost(amphipod[0], amphipod[1], (validHallwayColumn, 0)), createNewState(state, amphipod, (amphipod[0], (validHallwayColumn, 0))))))
    return neighborStates

initalState =((input[0], (2,1)), (input[1], (2,2)), (input[2], (2,3)), (input[3], (2,4)), (input[4], (4,1)), (input[5], (4,2)), (input[6], (4,3)), (input[7], (4,4)), (input[8], (6,1)), (input[9], (6,2)), (input[10], (6,3)), (input[11], (6,4)), (input[12], (8,1)), (input[13], (8,2)), (input[14], (8,3)), (input[15], (8,4)))

queue = []
visited = set()
heapq.heappush(queue, (0, initalState))
while True:
    (weight, state) = heapq.heappop(queue)
    if isFinalState(state):
        break
    if state in visited:
        continue
    visited.add(state)
    neighborStates = genNeighborStates(state, weight)
    for neighborState in neighborStates:
        heapq.heappush(queue, neighborState)

print(weight, state)