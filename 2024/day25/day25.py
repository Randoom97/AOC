from input import input

def to5Tuple(list):
    return (list[0],list[1],list[2],list[3],list[4])

keys = []
locks = []
for item in input:
    profile = []
    char = item[0][0]
    for col in range(len(item[0])):
        for row in range(1,len(item)):
            if item[row][col] != char:
                profile.append(row-1)
                break
    profileTuple = to5Tuple(profile)
    if char == '.':
        keys.append(profileTuple)
    else:
        locks.append(profileTuple)
# for key in keys:
#     print(key)
# print()
# for lock in locks:
#     print(lock)


fitCount = 0
for key in keys:
    for lock in locks:
        fits = True
        for i in range(len(key)):
            if key[i] < lock[i]:
                fits = False
                break
        if fits:
            fitCount += 1
print(fitCount)
