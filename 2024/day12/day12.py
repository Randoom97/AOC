from input import input

def preprocess(data):
    areaList = []
    visited = set()
    for row in range(len(data)):
        for col in range(len(data[0])):
            pos = (row,col)
            id = data[row][col]
            if pos in visited:
                continue
            areaSet = set()
            stack = [pos]
            while len(stack) > 0:
                curPos = stack.pop()
                (r, c) = curPos
                if curPos in visited or data[r][c] != id:
                    continue
                areaSet.add(curPos)
                visited.add(curPos)
                if r-1 >= 0:
                    stack.append((r-1,c))
                if c-1 >= 0:
                    stack.append((r,c-1))
                if r+1 < len(data):
                    stack.append((r+1,c))
                if c+1 < len(data[0]):
                    stack.append((r,c+1))
            areaList.append((id, areaSet))
    return areaList

def perimeter(areaSet):
    totalPerimeter = 0
    for point in areaSet:
        perimeter = 4
        if (point[0], point[1]-1) in areaSet:
            perimeter -= 1
        if (point[0]-1, point[1]) in areaSet:
            perimeter -= 1
        if (point[0], point[1]+1) in areaSet:
            perimeter -= 1
        if (point[0]+1, point[1]) in areaSet:
            perimeter -= 1
        totalPerimeter += perimeter
    return totalPerimeter

def sideCount(areaSet):
    edges = set()
    for (row, col) in areaSet:
        if (row-1, col) not in areaSet:
            edges.add(((row, col), (row, col+1)))
        if (row+1, col) not in areaSet:
            edges.add(((row+1, col), (row+1, col+1)))
        if (row, col-1) not in areaSet:
            edges.add(((row, col),(row+1, col)))
        if (row, col+1) not in areaSet:
            edges.add(((row, col+1), (row+1, col+1)))
    edgesCopy = edges.copy()
    sideCount = 0
    while len(edges) > 0:
        ((r1,c1), (r2,c2)) = edges.pop()
        if c1 == c2: # vertical
            r = r2+1
            c = c1
            while ((r-1,c), (r,c)) in edges and (((r-1,c),(r-1,c+1)) not in edgesCopy and ((r-1,c-1),(r-1,c)) not in edgesCopy):
                edges.remove(((r-1,c), (r,c)))
                r += 1
            r = r1-1
            while ((r,c),(r+1,c)) in edges and (((r+1,c),(r+1,c+1)) not in edgesCopy and ((r+1,c-1), (r+1,c)) not in edgesCopy):
                edges.remove(((r,c),(r+1,c)))
                r-=1
            sideCount += 1
        else: # horizontal
            c = c2+1
            r = r1
            while ((r,c-1), (r,c)) in edges and (((r,c-1),(r+1,c-1)) not in edgesCopy and ((r-1,c-1),(r,c-1)) not in edgesCopy):
                edges.remove(((r,c-1), (r,c)))
                c += 1
            c = c1-1
            while ((r,c),(r,c+1)) in edges and (((r,c+1),(r+1,c+1)) not in edgesCopy and ((r-1,c+1), (r,c+1)) not in edgesCopy):
                edges.remove(((r,c),(r,c+1)))
                c-=1
            sideCount += 1
    return sideCount
    

data = preprocess(input)
part1 = 0
part2 = 0
for (id, areaSet) in data:
    # line = id + " a:" + str(len(areaSet)) + " p:"+ str(sideCount(areaSet))
    # print(line)
    part1 += len(areaSet)*perimeter(areaSet)
    part2 += len(areaSet)*sideCount(areaSet)

print(part1)
print(part2)