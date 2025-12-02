from input import input

counts = {}

for i in range(14):
    counts[input[i]] = counts.get(input[i], 0) + 1

index = 0
while any(map(lambda val: val > 1, counts.values())):
    counts[input[index]] -= 1
    index += 1
    counts[input[index+13]] = counts.get(input[index+13], 0) + 1

print(index+14)
