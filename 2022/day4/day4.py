from input import input

# Part 1
# sum = 0
# for pairs in input:
#     elfOne = pairs[0]
#     elfTwo = pairs[1]
#     if (elfOne[0] >= elfTwo[0] and elfOne[1] <= elfTwo[1]) or (elfTwo[0] >= elfOne[0] and elfTwo[1] <= elfOne[1]):
#         sum += 1
# print(sum)

# Part 2
sum = 0
for pairs in input:
    elfOne = pairs[0]
    elfTwo = pairs[1]
    if (elfOne[0] >= elfTwo[0] and elfOne[0] <= elfTwo[1]) or (elfOne[1] >= elfTwo[0] and elfOne[1] <= elfTwo[1]) or (elfTwo[0] >= elfOne[0] and elfTwo[0] <= elfOne[1]) or (elfTwo[1] >= elfOne[0] and elfTwo[1] <= elfOne[1]):
        sum += 1
print(sum)