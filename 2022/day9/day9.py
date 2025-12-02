from input import input

sections = [(0,0) for _ in range(10)]
tailVisited = set()

def updateTail(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail

    if head[0] != tail[0]:
        if head[0] < tail[0]:
            tail = (tail[0]-1, tail[1])
        else:
            tail = (tail[0]+1, tail[1])
    if head[1] != tail[1]:
        if head[1] < tail[1]:
            return (tail[0], tail[1]-1)
        else:
            return (tail[0], tail[1]+1)
    return tail
        
    

def updateHead(direction, head):
    if direction == "L":
        return (head[0]-1, head[1])
    elif direction == "R":
        return (head[0]+1, head[1])
    elif direction == "U":
        return (head[0], head[1]-1)
    elif direction == "D":
        return (head[0], head[1]+1)

for instruction in input:
    direction = instruction[0]
    for i in range(instruction[1]):
        sections[0] = updateHead(direction, sections[0])
        for j in range(1, len(sections)):
            sections[j] = updateTail(sections[j-1], sections[j])
        tailVisited.add(sections[len(sections)-1])
        for j in range(1, len(sections)):
            if abs(sections[j][0] - sections[j-1][0]) > 1 or abs(sections[j][1] - sections[j-1][1]) > 1:
                print("sanity check failed")

print(len(tailVisited))
