from input import input, area

def distance(point1, point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

sensorDistances = list(map(lambda pair: [pair[0], distance(pair[0], pair[1])], input))

x=0
while x <= area:
    if x % 100000 == 0:
        print(x)
    ranges = set()
    for sensorDistance in sensorDistances:
        sensorPos = sensorDistance[0]
        verticalDist = sensorDistance[1]-abs(x-sensorPos[0])
        if verticalDist >= 0:
           ranges.add((sensorPos[1]-verticalDist, sensorPos[1]+verticalDist))
    y=0
    while y <= area:
        validPoint = True
        for range in ranges:
            if y >= range[0] and y <= range[1]:
                y = range[1]
                validPoint = False
                break
        if validPoint:
            break
        y += 1
    if validPoint:
        break
    x += 1
print((x,y))
print(x*area+y)



# totalChecks = 0

# x = 0
# while x <= area:
#     if x % 100000 == 0:
#         print(x)
#     y = 0
#     while y <= area:
#         testPoint = (x,y)
#         validPoint = True
#         for sensorDistance in sensorDistances:
#             sensorPos = sensorDistance[0]
#             dist = sensorDistance[1]
#             testDistance = distance(testPoint, sensorPos)
#             # totalChecks += 1
#             if testDistance <= dist:
#                 if testPoint[1] < sensorPos[1]:
#                     y += dist+testDistance-1
#                 else:
#                     y += dist-testDistance
#                 validPoint = False
#                 break
#         if validPoint:
#             break
#         y += 1
#     if validPoint:
#         break
#     x += 1
# print(testPoint)
# print(totalChecks)