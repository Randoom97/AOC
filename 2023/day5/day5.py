from input import input

def transform(inputRanges: list, mappings):
    newRanges = []
    while inputRanges:
        inputRange = inputRanges.pop()
        overlapFound = False
        for mapping in mappings:
            length = mapping[2]
            destStart = mapping[0]

            sourceStart = mapping[1]
            sourceEnd = sourceStart+length-1
            inputStart = inputRange[0]
            inputEnd = inputStart + inputRange[1]-1

            # fully contained
            if inputStart >= sourceStart and inputEnd <= sourceEnd:
                newRanges.append((destStart +inputStart-sourceStart, inputRange[1]))
                overlapFound = True
                break
            # fully eclipsing two new input ranges and one transformed one
            if sourceStart > inputStart and sourceEnd < inputEnd:
                newRanges.append((destStart, length))
                inputRanges.append((inputStart, sourceStart-inputStart))
                inputRanges.append((sourceEnd+1, inputEnd-sourceEnd))
                overlapFound = True
                break
            # left overlap: convert left half retry right half
            if sourceStart <= inputStart <= sourceEnd:
                newRanges.append((destStart+inputStart-sourceStart, sourceEnd-inputStart+1))
                inputRanges.append((sourceEnd+1, inputEnd-sourceEnd))
                overlapFound = True
                break
            # right overlap: convert right half retry left half
            if sourceStart <= inputEnd <= sourceEnd:
                newRanges.append((destStart, inputEnd-sourceStart+1))
                inputRanges.append((inputStart, sourceStart-inputStart))
                overlapFound = True
                break
        if not overlapFound:
            newRanges.append(inputRange)
    return newRanges


soil = transform(input["seeds"], input["seed-to-soil"])
fertilizer = transform(soil, input["soil-to-fertilizer"])
water = transform(fertilizer, input["fertilizer-to-water"])
light = transform(water, input["water-to-light"])
temp = transform(light, input["light-to-temperature"])
humid = transform(temp, input["temperature-to-humidity"])
location = transform(humid, input["humidity-to-location"])

print(location)
lengths = [x[1] for x in location]
print(len(lengths))
print(sum(lengths))
starts = [x[0] for x in location]
starts.sort()
print(min(starts))
