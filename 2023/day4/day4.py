from input import input

def getCardScore(card:str):
    card = card[card.index(":")+2:]
    numberParts = card.split('|')
    winning = set([int(number) for number in numberParts[0].split()])
    numbers = set([int(number) for number in numberParts[1].split()])
    return len(winning.intersection(numbers))

cardScores = [getCardScore(card) for card in input]

cardCounts = [1 for _ in range(len(input))]

for index in range(len(cardCounts)):
    for copyIndex in range(cardScores[index]):
        cardCounts[index+copyIndex+1] += cardCounts[index]

print(sum(cardCounts))