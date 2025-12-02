from input import input

def processInput(input):
    lines = []
    for line in input:
        coordString, velocityString = "".join(line.split()).split('@')
        coords = coordString.split(',')
        coord = (int(coords[0]), int(coords[1]), int(coords[2]))
        velocities = velocityString.split(',')
        velocity = (int(velocities[0]), int(velocities[1]), int(velocities[2]))
        lines.append((coord, velocity))
    return lines

def lineIntersection(A, B, C, D):
    a1 = B[1]
    b1 = -B[0]
    c1 = a1*(A[0]) + b1*(A[1])

    a2 = D[1]
    b2 = -D[0]
    c2 = a2*(C[0]) + b2*(C[1])

    determinant = a1*b2 - a2*b1
    if determinant == 0:
        return None
    x = (b2*c1 - b1*c2)/determinant
    y = (a1*c2 - a2*c1)/determinant
    
    # intersection in past for either stone
    if (x-A[0])/B[0] < 0 or (x-C[0])/D[0] < 0:
        return None

    return (x, y)

lines = processInput(input)

# count = 0
# lower = 200000000000000
# higher = 400000000000000
# for i in range(len(lines)-1):
#     for j in range(i+1, len(lines)):
#         intersection = lineIntersection(lines[i][0], lines[i][1], lines[j][0], lines[j][1])
#         if intersection == None:
#             continue
#         if intersection[0] >= lower and intersection[0] <= higher and intersection[1] >= lower and intersection[1] <= higher:
#             count += 1
# print(count)

from z3 import *
x,y,z,vx,vy,vz = Int('x'),Int('y'),Int('z'),Int('vx'),Int('vy'),Int('vz')
T = [Int(f'T{i}') for i in range(3)]
SOLVE = Solver()
for i in range(3):
    SOLVE.add(x + vx*T[i] - lines[i][0][0] - lines[i][1][0]*T[i] == 0)
    SOLVE.add(y + vy*T[i] - lines[i][0][1] - lines[i][1][1]*T[i] == 0)
    SOLVE.add(z + vz*T[i] - lines[i][0][2] - lines[i][1][2]*T[i] == 0)
res = SOLVE.check()
M = SOLVE.model()
print(M.eval(x+y+z))