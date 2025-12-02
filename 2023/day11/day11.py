from input import input

galaxies = []
rowsWithGalaxies = set()
colsWithGalaxies = set()
for row, line in enumerate(input):
    for col, char in enumerate(line):
        if char == '#':
            galaxies.append((row,col))
            rowsWithGalaxies.add(row)
            colsWithGalaxies.add(col)

# account for galactic expansion
expansion = 999999
rowConversion = {}
rowOffset = 0
for row in range(len(input)):
    if row not in rowsWithGalaxies:
        rowOffset += expansion
    else:
        rowConversion[row] = row+rowOffset
colConversion = {}
colOffset = 0
for col in range(len(input[0])):
    if col not in colsWithGalaxies:
        colOffset += expansion
    else:
        colConversion[col] = col+colOffset

expandedGalaxies = []
for galaxy in galaxies:
    row, col = galaxy
    expandedGalaxies.append((rowConversion[row], colConversion[col]))

totalDist = 0
for i in range(len(expandedGalaxies)-1):
    for j in range(i+1,len(expandedGalaxies)):
        totalDist += abs(expandedGalaxies[i][0] - expandedGalaxies[j][0]) + abs(expandedGalaxies[i][1] - expandedGalaxies[j][1])
print(totalDist)