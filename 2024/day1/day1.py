from input import input

# Part 1
# list1 = []
# list2 = []
# for i in range(len(input)):
#     if i % 2 == 0: 
#         list1.append(input[i])
#     else:
#         list2.append(input[i])

# list1.sort()
# list2.sort()

# print(len(list1))
# print(len(list2))

# total = 0
# for i in range(len(list1)):
#     total += abs(list1[i] - list2[i])

# print(total)



# Part 2
list = []
map = {}
for i in range(len(input)):
    if i % 2 == 0:
        list.append(input[i])
    else:
        if input[i] in map:
            map[input[i]] += 1
        else:
            map[input[i]] = 1

total = 0
for number in list:
    value = 0
    if number in map:
        value = map[number]
    total += number * value

print(total)