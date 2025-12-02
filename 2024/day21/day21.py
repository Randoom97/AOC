from input import codes

keypad = ["789","456","123",".0A"]
dirpad = [".^A","<v>"]

def genPaths(pad, neighborOrder):
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
                # else:
                #     continue
                padPaths[(startChar, endChar)].add(path)
                for (dr, dc, char) in neighborOrder:
                    if r+dr >= 0 and r+dr < len(pad) and c+dc >= 0 and c+dc < len(pad[0]):
                        queue.append(((r+dr,c+dc), path+char))
    return padPaths

# order of neighbor checks matters here to avoid switching keys to avoid empty space
keypadPaths = genPaths(keypad, [(-1,0,'^'), (0,1,'>'), (1,0,'v'), (0,-1,'<')])
# and unfortunately is not the same from the keypad to the dirpad
dirpadPaths = genPaths(dirpad, [(1,0,'v'), (0,1,'>'), (-1,0,'^'), (0,-1,'<')])

def convertCode(padPaths, prevChar, code):
    newCodes = set()
    if len(code) == 1:
        for sequence in padPaths[(prevChar, code[0])]:
            newCodes.add(sequence+"A")
        return newCodes
    for sequence in padPaths[(prevChar,code[0])]:
        for nextSequence in convertCode(padPaths, code[0], code[1:]):
            newCodes.add(sequence+"A"+nextSequence)
    return newCodes

def convertCodes(padPaths, codes):
    newCodes = set()
    for code in codes:
        newCodes = newCodes.union(convertCode(padPaths, "A", code))
    return newCodes

def retainShortest(codes):
    shortest = None
    for code in codes:
        if shortest == None:
            shortest = len(code)
        shortest = min(len(code), shortest)
    shortSet = set()
    for code in codes:
        if len(code) == shortest:
            shortSet.add(code)
    return shortSet



total = 0
for code in codes:
    codes1 = retainShortest(convertCodes(keypadPaths, set([code])))
    codes2 = retainShortest(convertCodes(dirpadPaths, codes1))
    codes3 = retainShortest(convertCodes(dirpadPaths, codes2))
    total += int(code[:len(code)-1])*len(codes3.pop())
print(total)
    



                
