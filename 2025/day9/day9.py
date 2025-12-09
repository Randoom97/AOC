from input import input

def area(t1, t2):
    return (abs(t1[0]-t2[0])+1) * (abs(t1[1]-t2[1])+1)

horizontals = []
verticals = []
for i in range(len(input)):
    p1 = input[i]
    p2 = input[(i+1)%len(input)]
    if p1[0] != p2[0]:
        # (y, x_min, x_max)
        horizontals.append((p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])))
    else:
        # (x, y_min, y_max)
        verticals.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))

def intersect(p1, p2):
    xmin, xmax = sorted([p1[0], p2[0]])
    ymin, ymax = sorted([p1[1], p2[1]])
    for vertical in verticals:
        if xmin < vertical[0] < xmax and (vertical[1] <= ymin < vertical[2] or vertical[1] < ymax <= vertical[2]):
            return True
    for horizontal in horizontals:
        if ymin < horizontal[0] < ymax and (horizontal[1] <= xmin < horizontal[2] or horizontal[1] < xmax <= horizontal[2]):
            return True
    return False

largest_area = 0
largest_points = None
for i in range(len(input)-1):
    for j in range(i+1, len(input)):
        p1 = input[i]
        p2 = input[j]
        if intersect(p1, p2):
            continue
        largest_area = max(largest_area, area(p1, p2))
print(largest_area)