from input import codes

keypad = ["789","456","123",".0A"]
dirpad = [".^A","<v>"]

def genPaths(pad):
    padPaths = {}
    for row in range(len(pad)):
        for col in range(len(pad[0])):
            if pad[row][col] == '.':
                continue
            startChar = pad[row][col]
            queue = [((row, col), "")]
            visited = {}
            while len(queue) > 0:
                pos, path = queue.pop(0)
                r,c = pos
                if pad[r][c] == '.':
                    continue
                endChar = pad[r][c]
                if pos in visited and len(path) > visited[pos]:
                    continue
                visited[pos] = len(path)
                if (startChar, endChar) not in padPaths:
                    padPaths[(startChar, endChar)] = set()
                padPaths[(startChar, endChar)].add(path)
                for (dr, dc, char) in [(1,0,'v'), (-1,0,'^'), (0,1,'>'), (0,-1,'<')]:
                    if r+dr >= 0 and r+dr < len(pad) and c+dc >= 0 and c+dc < len(pad[0]):
                        queue.append(((r+dr,c+dc), path+char))
    return padPaths

keypadPaths = genPaths(keypad)
dirpadPaths = genPaths(dirpad)

bestDirpadCache = {}
def bestDirpad(curChar, nextChar, indirection):
    cacheKey = (curChar, nextChar, indirection)
    if cacheKey in bestDirpadCache:
        return bestDirpadCache[cacheKey]
    if indirection == 1:
        bestDirpadCache[cacheKey] = len(list(dirpadPaths[(curChar, nextChar)])[0])+1
        return bestDirpadCache[cacheKey]
    minimum = None
    for path in dirpadPaths[(curChar, nextChar)]:
        total = 0
        newCurChar = "A"
        for char in path+"A":
            total += bestDirpad(newCurChar, char, indirection-1) # type: ignore
            newCurChar = char
        if minimum == None or total < minimum:
            minimum = total
    bestDirpadCache[cacheKey] = minimum
    return minimum

def bestKeypad(curChar, nextChar, indirection):
    minimum = None
    for path in keypadPaths[(curChar, nextChar)]:
        total = 0
        newCurChar = "A"
        for char in path+"A":
            total += bestDirpad(newCurChar, char, indirection) # type: ignore
            newCurChar = char
        if minimum == None or total < minimum:
            minimum = total
    return minimum

complexity = 0
for code in codes:
    prevChar = "A"
    length = 0
    for char in code:
        length += bestKeypad(prevChar, char, 25) # type: ignore
        prevChar = char
    complexity += length*int(code[:len(code)-1])
    print(str(length)+" * "+str(int(code[:len(code)-1])))
print(complexity)