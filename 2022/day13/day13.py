from functools import cmp_to_key

from input import input

def compare(left, right):
    # print("Comparing: "+str(left)+" vs "+str(right))
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif right < left:
            return -1
        else:
            return 0
    if type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            comparison = compare(left[i], right[i])
            if comparison == 1 or comparison == -1:
                return comparison
        if len(left) < len(right):
            return 1
        elif len(right) < len(left):
            return -1
        else:
            return 0
    else:
        if type(left) == int:
            return compare([left], right)
        elif type(right) == int:
            return compare(left, [right])


# indicies = []
# for i in range(0, len(input), 2):
#     left = input[i]
#     right = input[i+1]
#     result = compare(left, right)
#     if result == True:
#         indicies.append(i//2 + 1)
# print(sum(indicies))

sortedInput = sorted(input, key=cmp_to_key(compare), reverse=True)
for i in range(len(sortedInput)):
    if sortedInput[i] == [[2]]:
        index1 = i+1
    if sortedInput[i] == [[6]]:
        index2 = i+1

print(index1)
print(index2)
print(index1*index2)
    