from functools import lru_cache
import math


def solution(n):
    return options(1, n) - 1
    
@lru_cache(maxsize=16000)
def options(minStart, brickCount):
    if brickCount - minStart <= minStart:
        return 1
    optionCount = 0
    for stepHeight in range(minStart, math.ceil(brickCount / 2)):
        optionCount += options(stepHeight + 1, brickCount - stepHeight)
    return optionCount + 1
    
print(solution(200))