from input import input

class valve:
    def __init__(self, key, flow, connections):
        self.key = key
        self.flow = flow
        self.connections = connections

valves = {}
for item in input:
    v = valve(item[0], item[1], item[2])
    valves[v.key] = v

def genCacheKey(locations, openValves: set, minutes: int):
    sortedValves = list(openValves)
    sortedValves.sort()
    return "loc:"+str(locations)+"o:"+str(sortedValves)+"m:"+str(minutes)

cache = {}
def flowRate(locations, openValves: set, minutes: int):
    if minutes[0] == 0 and minutes[1] == 0:
        return 0
    cacheKey = genCacheKey(locations, openValves, minutes)
    if cacheKey in cache:
        return cache[cacheKey]
    
    myLoc = locations[0]
    myMinutes = minutes[0]
    elephLoc = locations[1]
    elephMinutes = minutes[1]
    flows = []

    openFraction = (len(input) - len(openValves))*0.50 / len(input)
    timeFraction = (myMinutes+elephMinutes)/(26*2)

    if openFraction > timeFraction:
        return 0

    if myMinutes > 0:
        v = valves[myLoc]
        newMinutes = (myMinutes-1, elephMinutes)
        if v.flow > 0 and myLoc not in openValves:
            newOpenValves = openValves.copy()
            newOpenValves.add(myLoc)
            flows.append(flowRate(locations, newOpenValves, newMinutes)+v.flow*(myMinutes-1))
        for newLocation in v.connections:
            flows.append(flowRate((newLocation, elephLoc), openValves, newMinutes))
    
    if elephMinutes > 0:
        v = valves[elephLoc]
        newMinutes = (myMinutes, elephMinutes-1)
        if v.flow > 0 and elephLoc not in openValves:
            newOpenValves = openValves.copy()
            newOpenValves.add(elephLoc)
            flows.append(flowRate(locations, newOpenValves, newMinutes)+v.flow*(elephMinutes-1))
        for newLocation in v.connections:
            flows.append(flowRate((myLoc, newLocation), openValves, newMinutes))
    
    maxFlow = max(flows)
    cache[cacheKey] = maxFlow
    return maxFlow

print(flowRate(("AA","AA"), set(), (26,26)))
print(len(cache))
    