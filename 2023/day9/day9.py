from input import input

def extrapolateSequences(sequence):
    sequences = [sequence]
    lastSequence = sequence
    while any(lastSequence):
        sequences.append([lastSequence[i+1] - lastSequence[i] for i in range(len(lastSequence)-1)])
        lastSequence = sequences[len(sequences)-1]
    return sequences

def getNext(sequence):
    sequences = extrapolateSequences(sequence)
    for sequence in sequences:
        print(sequence)
    nextValue = 0
    for i in range(len(sequences)-2, -1, -1):
        nextValue = sequences[i][len(sequences[i])-1]+nextValue
    return nextValue

def getPrevious(sequence):
    sequences = extrapolateSequences(sequence)
    prevValue = 0
    for i in range(len(sequences)-2, -1, -1):
        prevValue = sequences[i][0]-prevValue
    return prevValue

total = 0
for line in input:
    sequence = [int(value) for value in line.split()]
    prev = getPrevious(sequence)
    total += prev
    print(prev)
print(total)
