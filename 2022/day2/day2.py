from input import input, scores

sum = 0
for round in input:
    sum += scores[round]

print(sum)