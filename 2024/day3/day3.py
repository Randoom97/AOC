import re

from input import input

# part 1
# muls = re.findall("mul\\((\\d+),(\\d+)\\)", input)
# total = 0
# for mul in muls:
#     total += int(mul[0]) * int(mul[1])
# print(total)

# part 2
instructions = re.findall("(do\\(\\))|(don't\\(\\))|(mul\\((\\d+),(\\d+)\\))", input)
total = 0
doMuls = True
for instruction in instructions:
    if instruction[0]:
        doMuls = True
    if instruction[1]:
        doMuls = False
    if instruction[2] and doMuls:
        total += int(instruction[3]) * int(instruction[4])
print(total)