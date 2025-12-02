from input import input

count = 0
for line in input:
    lineSplit = line.split("|")
    observations = lineSplit[0].split(" ")

    patterns = [set()]*10
    zeroOrSixOrNine = []
    twoOrThreeOrFive = []

    for observation in observations:
        observationSet = set(observation)
        length = len(observation)
        if length == 2:
            patterns[1] = observationSet
        elif length == 4:
            patterns[4] = observationSet
        elif length == 3:
            patterns[7] = observationSet
        elif length == 7:
            patterns[8] = observationSet
        elif length == 6:
            zeroOrSixOrNine.append(observationSet)
        elif length == 5:
            twoOrThreeOrFive.append(observationSet)

    topSegment = patterns[7].difference(patterns[1])
    rightSegment = patterns[7].intersection(patterns[1])
    middleSegment = patterns[4].difference(patterns[1])
    lowerSegment = patterns[8].difference(patterns[7].union(patterns[4]))

    for number in zeroOrSixOrNine:
        numberSet = set(number)
        if len(numberSet.intersection(middleSegment)) == 1:
            patterns[0] = numberSet
        elif len(numberSet.intersection(rightSegment)) == 1:
            patterns[6] = numberSet
        else:
            patterns[9] = numberSet
    
    for number in twoOrThreeOrFive:
        numberSet = set(number)
        if len(numberSet.intersection(middleSegment)) == 1 and len(numberSet.intersection(rightSegment)) == 1:
            patterns[2] = numberSet
        elif len(numberSet.intersection(middleSegment)) == 1 and len(numberSet.intersection(lowerSegment)) == 1:
            patterns[3] = numberSet
        else:
            patterns[5] = numberSet

    value = 0
    outputs = lineSplit[1].split(" ")
    for output in outputs:
        for i in range(10):
            if patterns[i] == set(output):
                value += i
                break
        value *= 10
    value //= 10 
    count += value

print(count)