from input import input

def findHorizontalReflection(map):
    height = len(map)
    for row in range(height-1):
        smudge = False
        mirror = True
        for col in range(len(map[0])):
            for offset in range(min(row+1, height-row-1)):
                if map[row-offset][col] != map[row+1+offset][col]:
                    if smudge:
                        mirror = False
                        break
                    else:
                        smudge = True
            if not mirror:
                break
        if mirror and smudge:
            return row
    return None

def findVerticalReflection(map):
    width = len(map[0])
    for col in range(width-1):
        smudge = False
        mirror = True
        for row in range(len(map)):
            for offset in range(min(col+1, width-col-1)):
                if map[row][col-offset] != map[row][col+1+offset]:
                    if smudge:
                        mirror = False
                        break
                    else:
                        smudge = True
            if not mirror:
                break
        if mirror and smudge:
            return col
    return None

left = 0
up = 0
for map in input:
    verticalReflection = findVerticalReflection(map)
    if verticalReflection != None:
        left += verticalReflection+1
    horizontalReflection = findHorizontalReflection(map)
    if horizontalReflection != None:
        up += horizontalReflection+1
print(left + 100*up)