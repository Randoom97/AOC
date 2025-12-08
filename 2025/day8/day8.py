from input import boxes

def dist_square(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

dists = {}
for i, box1 in enumerate(boxes[:-1]):
    for j, box2 in enumerate(boxes[i+1:]):
        dists[(i,j+i+1)] = dist_square(box1, box2)

sorted_dists = sorted(dists.items(), key=lambda x: x[1])

connected = {b: set([b]) for b in range(len(boxes))}
dist_idx = 0
while len(connected[0]) != len(boxes):
    pair, _ = sorted_dists[dist_idx]
    left, right = pair
    group = connected[left].union(connected[right])
    for box in group:
        connected[box] = group
    dist_idx += 1
print(boxes[pair[0]][0] * boxes[pair[1]][0])

# connected = {b: set([b]) for b in range(len(boxes))}
# for pair, _ in sorted_dists[:1000]:
#     left, right = pair
#     group = connected[left].union(connected[right])
#     for box in group:
#         connected[box] = group

# uncounted = set(range(len(boxes)))
# groups = []
# while len(uncounted) != 0:
#     box = uncounted.pop()
#     groups.append(connected[box])
#     uncounted = uncounted - connected[box]

# total = 1
# for group_size in sorted(map(len, groups), reverse=True)[:3]:
#     total *= group_size
# print(total)


