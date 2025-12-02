# note: Unfinished, maybe someday

from functools import lru_cache

from input import input

runs = 0

# bestPathSoFar = 0
# def calcPathScore(bots, resources, timeLeft):
#     value = 0
#     for bidx in range(len(bots)):
#         value += bots[bidx]*(bidx+1)
#     for ridx in range(len(resources)):
#         value += resources[ridx]*(ridx+1)
#     return value*timeLeft

# Something is broken about this method
def factoryShouldIdle(bots, resources, blueprints):
    for blueprint in blueprints:
        if resources >= blueprint:
            continue
        for ridx in range(len(resources)):
            if blueprint[ridx] > 0 and resources[ridx] < blueprint[ridx] and bots[ridx] > 0:
                return True
    return False

@lru_cache(maxsize=None)
def maxGeodes(bots, resources, blueprints, timeLeft):
    global runs, bestPathSoFar
    runs += 1
    # pathScore = calcPathScore(bots, resources, timeLeft)

    # # print(bots)
    # # print(resources)
    # # print(timeLeft)
    # # print(pathScore)
    # # print()

    # if pathScore < 0.25*bestPathSoFar:
    #     return 0
    # bestPathSoFar = max(bestPathSoFar, pathScore)

    if timeLeft <= 0:
        return 0
    resources = tuple(map(lambda i, j: i+j, resources, bots))

    options = []
    for bidx in range(len(blueprints)):
        blueprint = blueprints[bidx]
        if all(map(lambda i,j: i >= j, resources, blueprint)):
            newResources = tuple(map(lambda i, j: i-j, resources, blueprint))
            botsList = list(bots)
            botsList[bidx] += 1
            newBots = tuple(botsList)
            options.append(bots[3]+maxGeodes(newBots, newResources, blueprints, timeLeft-1))
    if factoryShouldIdle(bots, resources, blueprints):
        options.append(bots[3]+maxGeodes(bots, resources, blueprints, timeLeft-1))
    return max(options)

print(maxGeodes((1,0,0,0), (0,0,0,0), input[0], 20))
print(runs)