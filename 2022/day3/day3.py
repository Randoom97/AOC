from input import input

# Part 1
# sum = 0
# for line in input:
#     lineLength = len(line)
#     left = line[:lineLength//2]
#     right = line[lineLength//2:]
#     leftSet = set()
#     rightSet = set()
#     for char in left:
#         leftSet.add(char)
#     for char in right:
#         rightSet.add(char)
#     val = ord(leftSet.intersection(rightSet).pop())
#     if val > ord('Z'):
#         val = val - ord('a') + 1
#     else:
#         val = val + 27 - ord('A')
#     sum += val

# print(sum)

# Part 2
sum = 0
for i in range(0, len(input), 3):
    setOne = set()
    setTwo = set()
    setThree = set()
    for char in input[i]:
        setOne.add(char)
    for char in input[i+1]:
        setTwo.add(char)
    for char in input[i+2]:
        setThree.add(char)
    val = ord(setOne.intersection(setTwo).intersection(setThree).pop())
    if val > ord('Z'):
        val = val - ord('a') + 1
    else:
        val = val + 27 - ord('A')
    sum += val

print(sum)