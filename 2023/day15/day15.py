from input import input

def hash(string:str):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def printBoxes(boxes):
    for index, box in enumerate(boxes):
        if box:
            print("Box " + str(index) + ": " + str(box))

def getFocusingPower(boxes):
    power = 0
    for boxIndex, box in enumerate(boxes):
        for lensIndex, lens in enumerate(box):
            power += (boxIndex+1)*(lensIndex+1)*(lens[1])
    return power

boxes = [[] for x in range(256)]
for line in input:
    if '-' in line:
        label = line[:-1]
        labelHash = hash(label)
        for lens in boxes[labelHash]:
            if lens[0] != label:
                continue
            boxes[labelHash].remove(lens)
            break
    elif '=' in line:
        label, focal = line.split('=')
        focal = int(focal)
        labelHash = hash(label)
        replaced = False
        for index, lens in enumerate(boxes[labelHash]):
            if lens[0] == label:
                replaced = True
                boxes[labelHash][index] = (label, focal)
                break
        if not replaced:
            boxes[labelHash].append((label, focal))

print(getFocusingPower(boxes))
