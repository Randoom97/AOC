from input import input

def processLine(line:str):
    maxes = {'red': 0, 'green': 0, 'blue': 0}
    gameId = int(line[5:line.index(':')])
    line = line[line.index(':')+2:]
    rounds = line.split(';')
    for round in rounds:
        round = round.strip()
        pulls = round.split(',')
        for pull in pulls:
            pull = pull.strip()
            parts = pull.split(' ')
            count = int(parts[0])
            color = parts[1]
            if maxes[color] < count:
                maxes[color] = count
    return gameId, maxes

desired = {'red': 12, 'green': 13, 'blue': 14}

totalPower = 0
for line in input:
    _, maxes = processLine(line)
    power = 1
    for value in maxes.values():
        power *= value
    totalPower += power
print(totalPower)
