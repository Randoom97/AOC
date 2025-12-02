import math

from input import xmin, xmax, ymin, ymax

def step(pos, vel):
    newPos = (pos[0]+vel[0], pos[1]+vel[1])
    xvel = vel[0]
    if xvel > 0:
        xvel -= 1
    elif xvel < 0:
        xvel += 1
    newVel = (xvel, vel[1]-1)
    return (newPos, newVel)

start = (0,0)
initymin = ymin
initymax = abs(ymin)-1
initxmin = math.ceil(-((1-((1+8*xmin)**0.5))//2))

hitCount = 0
for y in range(initymin, initymax+1):
    x = initxmin
    while x <= xmax:
        pos = (0,0)
        vel = (x,y)
        initVel = (x,y)
        while True:
            (pos, vel) = step(pos, vel)
            if pos[0] >= xmin and pos[0] <= xmax and pos[1] >= ymin and pos[1] <= ymax:
                hitCount += 1
                break
            if pos[0] > xmax or pos[1] < ymin:
                break
        x += 1
print(hitCount)