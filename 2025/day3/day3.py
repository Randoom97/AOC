from input import input

# total_joltage = 0
# for line in input:
#     left_digit = max(enumerate(line[:-1]), key=lambda x: x[1])
#     right_digit = max(line[left_digit[0]+1:])
#     total_joltage += int(f"{left_digit[1]}{right_digit}")
# print(total_joltage)


def biggest_joltage(bank, digits):
    if digits == 1:
        return str(max(bank))
    digit = max(enumerate(bank[:-digits+1]), key=lambda x: x[1])
    return f"{digit[1]}{biggest_joltage(bank[digit[0]+1:], digits-1)}"

total_joltage = 0
for line in input:
    total_joltage += int(biggest_joltage(line, 12))
print(total_joltage)