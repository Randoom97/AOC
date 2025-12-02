from input import input, inputMap

window = 256

starts = []
for key in inputMap:
    if key.endswith("A"):
        starts.append(key)

def nextInputRange(node):
    current = node
    stepsToZ = set()
    for index in range(len(input)*window):
        direction = input[index%len(input)]
        current = inputMap[current][0] if direction == "L" else inputMap[current][1]
        if current.endswith("Z"):
            stepsToZ.add(index+1)
    return (node, current, stepsToZ)

print("computing the next " + str(window) + " steps")
nextRangeMaps = {}
for node in inputMap.keys():
    thing = nextInputRange(node)
    nextRangeMaps[thing[0]] = (thing[1], thing[2])
print("done")

rangeWalks = 0
currents = [nextRangeMaps[start] for start in starts]
while not set.intersection(*[current[1] for current in currents]):
    rangeWalks += 1
    if rangeWalks % 1000000 == 0:
        print(currents)
    currents = [nextRangeMaps[current[0]] for current in currents]
print(len(input)*rangeWalks*window)
print(set.intersection(*[current[1] for current in currents]))