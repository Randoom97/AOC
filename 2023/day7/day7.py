
from input import input

def strength(hand:str):
    counts = {}
    for char in hand:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    if "J" in counts:
        highest = None
        highestCount = 0
        for card in counts:
            if card == "J":
                continue
            if counts[card] > highestCount:
                highestCount = counts[card]
                highest = card
        if highest:
            counts[highest] += counts["J"]
            counts["J"] = 0

    numbers = list(counts.values())
    numbers.sort(reverse = True)
    # five of a kind
    if numbers[0] == 5:
        return 7
    # four of a kind
    if numbers[0] == 4:
        return 6
    # full house
    if numbers[0] == 3 and numbers[1] == 2:
        return 5
    # three of a kind
    if numbers[0] == 3:
        return 4
    # two pair
    if numbers[0] == 2 and numbers[1] == 2:
        return 3
    # one pair
    if numbers[0] == 2:
        return 2
    # high card
    return 1

def cardStrength(card):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 1
    if card == "T":
        return 10
    return int(card)

def compare(hand1, hand2):
    strengthDiff = strength(hand1) - strength(hand2)
    if strengthDiff != 0:
        return strengthDiff
    for index in range(5):
        cardDiff = cardStrength(hand1[index]) - cardStrength(hand2[index])
        if cardDiff != 0:
            return cardDiff
    return 0

from functools import cmp_to_key
sortedInput = sorted(input, key=cmp_to_key(lambda a, b: compare(a[0], b[0])))
sortedBids = [line[1] for line in sortedInput]
print(sum([bid*(index+1) for index, bid in enumerate(sortedBids)]))