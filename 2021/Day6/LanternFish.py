from input import input

days = [0]*9
for val in input:
    days[val] += 1

totalFish = len(input)
for _ in range(256):
    newSpawned = days.pop(0)
    totalFish += newSpawned
    days[6] += newSpawned
    days.append(newSpawned)

print(totalFish)
