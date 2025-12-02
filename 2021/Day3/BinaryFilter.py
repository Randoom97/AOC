from input import input

idx = 0
def keepZero(value):
    return value[idx] == '0'
def keepOne(value):
    return value[idx] == '1'

tmpInput = input
while len(tmpInput) > 1:
    count = 0
    for line in tmpInput:
        if line[idx] == "1":
            count += 1
        if line[idx] == "0":
            count -= 1
    if count >= 0:
        tmpInput = list(filter(keepOne, tmpInput))
    else:
        tmpInput = list(filter(keepZero, tmpInput))
    idx += 1
    
oxy = int(tmpInput[0], 2)

idx = 0
tmpInput = input
while len(tmpInput) > 1:
    count = 0
    for line in tmpInput:
        if line[idx] == "1":
            count += 1
        if line[idx] == "0":
            count -= 1
    if count >= 0:
        tmpInput = list(filter(keepZero, tmpInput))
    else:
        tmpInput = list(filter(keepOne, tmpInput))
    idx += 1
        
co2 = int(tmpInput[0], 2)
print(co2*oxy)