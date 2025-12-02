from input import input

for i in range(10000):
    if i % 1000 == 0:
        print("round "+str(i))
    for monkey in input:
        while len(monkey.items) > 0:
            item, target = monkey.inspection()
            input[target].items.append(item)
print(input)
inspectionCounts = list(map(lambda monkey: monkey.inspectionCount, input))
inspectionCounts.sort(reverse=True)
print(inspectionCounts[0]*inspectionCounts[1])