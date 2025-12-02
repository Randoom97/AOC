from input import input

map = {}

for segment in input:
    if segment[0][0] == segment[1][0]:
        # Horizontal segment
        x = segment[0][0]
        miny = min(segment[0][1], segment[1][1])
        maxy = max(segment[0][1], segment[1][1])
        for y in range(miny, maxy + 1):
            key = str(x)+":"+str(y)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1
    elif segment[0][1] == segment[1][1]:
        # Vertical segment
        y = segment[0][1]
        minx = min(segment[0][0], segment[1][0])
        maxx = max(segment[0][0], segment[1][0])
        for x in range(minx, maxx + 1):
            key = str(x)+":"+str(y)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1
    else:
        dx = segment[0][0] - segment[1][0]
        dy = segment[0][1] - segment[1][1]
        stepx = -dx // abs(dx)
        stepy = -dy // abs(dy)
        x = segment[0][0]
        y = segment[0][1]
        while x != segment[1][0]:
            key = str(x)+":"+str(y)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1
            x += stepx
            y += stepy
        key = str(segment[1][0])+":"+str(segment[1][1])
        if key in map:
            map[key] += 1
        else:
            map[key] = 1

count = 0
for key in map:
    if map[key] > 1:
        count += 1
print(count)

