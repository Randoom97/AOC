import math

from input import input

def quadratic(a:int, b:int, c:float):
    rootPart = (b**2-4*a*c)**0.5
    return math.ceil((-b-rootPart)/2*a), math.floor((-b+rootPart)/2*a)

total = 1
for parts in input:
    low, high = quadratic(1, -parts[0], parts[1]+0.1)
    print(quadratic(1, -parts[0], parts[1]+0.1))
    total *= (high - low +1)

print(total)