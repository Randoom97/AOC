from input import input

points = set(input)

xs = list(map(lambda point: point[0], input))
ys = list(map(lambda point: point[1], input))
zs = list(map(lambda point: point[2], input))

minX = min(xs)
maxX = max(xs)
minY = min(ys)
maxY = max(ys)
minZ = min(zs)
maxZ = max(zs)

fills = set()

toCheck = [(minX-1, minY-1, minZ-1)]
while len(toCheck) > 0:
    point = toCheck.pop()
    if point in fills or point in points:
        continue
    fills.add(point)
    x = point[0]
    y = point[1]
    z = point[2]
    adj = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
    fadj = filter(lambda point: point[0] >= minX-1 and point[0] <= maxX+1 and point[1] >= minY-1 and point[1] <= maxY+1 and point[2] >= minZ-1 and point[2] <= maxZ+1, adj)
    for adjPoint in fadj:
        toCheck.append(adjPoint)

def faces(point, solids):
    x = point[0]
    y = point[1]
    z = point[2]

    adj = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
    return sum(list(map(lambda point: 0 if point in solids else 1, adj)))

fillSum = sum(list(map(lambda point: faces(point, fills), fills)))

xDelta = (maxX+1) - (minX-1)+1
yDelta = (maxY+1) - (minY-1)+1
zDelta = (maxZ+1) - (minZ-1)+1

xArea = yDelta*zDelta*2
yArea = xDelta*zDelta*2
zArea = xDelta*yDelta*2

print(fillSum - xArea - yArea - zArea)

