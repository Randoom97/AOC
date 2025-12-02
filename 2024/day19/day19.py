from input import available, desired

maxLenAvailable = 0
for item in available:
    maxLenAvailable = max(maxLenAvailable, len(item))

isPossibleCache = {}
def isPossible(pattern):
    if pattern in isPossibleCache:
        return isPossibleCache[pattern]
    if len(pattern) == 0:
        return True
    maxLen = min(maxLenAvailable, len(pattern))
    for i in range(maxLen):
        if pattern[:maxLen-i] in available:
            if isPossible(pattern[maxLen-i:]):
                isPossibleCache[pattern] = True
                return True
    isPossibleCache[pattern] = False
    return False

totalPossible = 0
for pattern in desired:
    if isPossible(pattern):
        totalPossible += 1
print(totalPossible)

combinationCountCache = {}
def combinationCount(pattern):
    if pattern in combinationCountCache:
        return combinationCountCache[pattern]
    if len(pattern) == 0:
        return 1
    maxLen = min(maxLenAvailable, len(pattern))
    comboCount = 0
    for i in range(maxLen):
        if pattern[:maxLen-i] in available:
            comboCount += combinationCount(pattern[maxLen-i:])
    combinationCountCache[pattern] = comboCount
    return comboCount

comboTotal = 0
for pattern in desired:
    comboTotal += combinationCount(pattern)
print(comboTotal)