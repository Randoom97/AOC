from input import input

# problems = []
# operations = []
# for line in input:
#     parts = [part.strip() for part in line.strip().split()]
#     if parts[0] == '*' or parts[0] == '+':
#         operations = parts
#     else:
#         if len(problems) == 0:
#             problems = [[] for _ in range(len(parts))]
#         for i, p in enumerate(parts):
#             problems[i].append(int(p))

# answer = 0
# for i, operator in enumerate(operations):
#     if operator == '+':
#         total = sum(problems[i])
#     else:
#         total = 1
#         for value in problems[i]:
#             total *= value
#     answer += total
# print(answer)

totals = []
operands = []
for col in range(len(input[0])-1, -1, -1):
    cur_num_string = ""
    for row in range(len(input)):
        c = input[row][col]
        if c == ' ':
            continue
        if c == '+' or c == '*':
            if cur_num_string != "":
                operands.append(int(cur_num_string))
            if c == '+':
                total = sum(operands)
            else:
                total = 1
                for operand in operands:
                    total *= operand
            totals.append(total)
            operands.clear()
            cur_num_string = ""
        else:
            cur_num_string += c
    if cur_num_string != "":
        operands.append(int(cur_num_string))
print(sum(totals))