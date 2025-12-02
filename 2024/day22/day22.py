from input import secretNumbers

def nextNumber(number: int):
    number = ((number << 6) ^ number) % 16777216
    number = ((number >> 5) ^ number) % 16777216
    number = ((number << 11) ^ number) % 16777216
    return number

def toQuadTuple(list):
    return (list[0], list[1], list[2], list[3])

changesToPrice = {}
for secretNumber in secretNumbers:
    currentChangesToPrice = {}
    changes = []
    number: int = secretNumber
    for _ in range(2000):
        prevNumber = number
        number = nextNumber(prevNumber)
        change = (number%10) - (prevNumber%10)
        changes.append(change)
        if len(changes) > 4:
            changes.pop(0)
            changesTuple = toQuadTuple(changes)
            if changesTuple not in currentChangesToPrice:
                currentChangesToPrice[changesTuple] = number%10
    for key in currentChangesToPrice:
        if key not in changesToPrice:
            changesToPrice[key] = 0
        changesToPrice[key] += currentChangesToPrice[key]

maxPrice = None
for key in changesToPrice:
    if maxPrice == None or changesToPrice[key] > maxPrice:
        maxPrice = changesToPrice[key]
print(maxPrice)

