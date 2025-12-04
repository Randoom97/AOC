from input import map

rolls = set()
for row, line in enumerate(map):
    for col, char in enumerate(line):
        if char == "@":
            rolls.add((row,col))

# accessable_rolls = 0
# for roll in rolls:
#     adjacent_count = 0
#     for row in range(roll[0]-1, roll[0]+2):
#         for col in range(roll[1]-1, roll[1]+2):
#             if (row, col) == roll:
#                 continue
#             if (row, col) in rolls:
#                 adjacent_count += 1
#     if adjacent_count < 4:
#         accessable_rolls += 1
# print(accessable_rolls)

removed_rolls = 0
while True:
    to_remove = set()
    for roll in rolls:
        adjacent_count = 0
        for row in range(roll[0]-1, roll[0]+2):
            for col in range(roll[1]-1, roll[1]+2):
                if (row, col) == roll:
                    continue
                if (row, col) in rolls:
                    adjacent_count += 1
        if adjacent_count < 4:
            to_remove.add(roll)
    if len(to_remove) == 0:
        break
    removed_rolls += len(to_remove)
    rolls -= to_remove
print(removed_rolls)