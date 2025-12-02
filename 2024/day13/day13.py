import re
from input import input

def preprocess(lines):
    problems = []
    for i in range(0, len(lines), 3):
        (xstr, ystr) = re.match("Button A: X\\+(\\d+), Y\\+(\\d+)", lines[i]).groups()
        A = (int(xstr), int(ystr))
        (xstr, ystr) = re.match("Button B: X\\+(\\d+), Y\\+(\\d+)", lines[i+1]).groups()
        B = (int(xstr), int(ystr))
        (xstr, ystr) = re.match("Prize: X=(\\d+), Y=(\\d+)", lines[i+2]).groups()
        P = (int(xstr)+10000000000000, int(ystr)+10000000000000)
        # P = (int(xstr), int(ystr))
        problems.append((A, B, P))
    return problems

def minimum(problem):
    (A, B, P) = problem
    initialMax = 3*max(P[0]//A[0], P[1]//A[1]) + max(P[0]//B[0], P[1]//B[1]) + 4
    minimumCost = initialMax
    for acount in range(max(P[0]//A[0], P[1]//A[1])):
        target = (P[0]-A[0]*acount, P[1]-A[1]*acount)
        if target[0] % B[0] != 0 or target[1] % B[1] != 0:
            continue
        if target[0]//B[0] != target[1]//B[1]:
            continue
        minimumCost = min(minimumCost, 3*acount + target[0]//B[0])
    return minimumCost if minimumCost < initialMax else None

def betterMinimum(problem):
    (A, B, P) = problem
    bcount = (P[1]*A[0] - A[1]*P[0])/(A[0]*B[1] - A[1]*B[0])
    acount = (P[0] - B[0]*bcount)/A[0]
    if acount % 1 != 0 or bcount % 1 != 0:
        return None
    return int(acount*3 + bcount)

problems = preprocess(input)
total = 0
validCount = 0
for problem in problems:
    tokens = betterMinimum(problem)
    if tokens != None:
        total += tokens
        validCount += 1
print(validCount)
print(total)