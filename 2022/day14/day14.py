
from input import input

solids = set()

lowestPos = 0
for line in input:
    for i in range(len(line)-1):
        start = line[i]
        end = line[i+1]
        lowestPos = max(lowestPos, start[1], end[1])
        if start[0] == end[0]:
            # horizontal segment
            delta = (end[1]-start[1])//abs(end[1]-start[1])
            for x in range(start[1], end[1]+delta, delta):
                solids.add((start[0], x))
        else:
            # vertical segment
            delta = (end[0]-start[0])//abs(end[0]-start[0])
            for y in range(start[0], end[0]+delta, delta):
                solids.add((y, start[1]))
lowestPos += 2

sandCount = 0
while (500, 0) not in solids:
    sand = (500, 0)
    while True:
        if sand[1] == lowestPos-1:
            solids.add(sand)
            sandCount += 1
            break
        if (sand[0], sand[1]+1) not in solids:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in solids:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in solids:
            sand = (sand[0]+1, sand[1]+1)
        else:
            solids.add(sand)
            sandCount += 1
            break
print(sandCount)
