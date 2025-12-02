from input import input

def enumerate(left: set, operands: list):
    right = operands.pop(0)
    leftSet = set()
    for l in left:
        leftSet.add(l+right)
        leftSet.add(l*right)
        leftSet.add(int(str(l)+str(right)))
    if len(operands) == 0:
        return leftSet
    return enumerate(leftSet, operands)

validCount = 0
for line in input:
    target = line.pop(0)
    leftSet = set()
    leftSet.add(line.pop(0))
    values = enumerate(leftSet, line)
    if target in values:
        validCount += target
print(validCount)