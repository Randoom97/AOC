from input import input

min = min(input)
max = max(input)

fuelCost = float("inf")
minPos = 0
for pos in range(min, max+1):
    cost = 0
    for horizPos in input:
        dist = abs(horizPos - pos)
        cost += dist*(dist+1)//2
    if cost <= fuelCost:
        fuelCost = cost
        minPos = pos
print(fuelCost, minPos)