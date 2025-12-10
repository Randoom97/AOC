from input import input
from scipy.optimize import linprog


# (indicator_target, buttons, joltage)
machines = []
for line in input:
    parts = line.split()
    indicator_target = parts[0]
    joltage_target = parts[len(parts)-1]
    buttons = parts[1:-1]
    
    indicator_target = [True if c == '#' else False for c in indicator_target[1:-1]]
    joltage_target = [int(j) for j in joltage_target[1:-1].split(",")]
    buttons = [list(map(int, button[1:-1].split(','))) for button in buttons]
    machines.append((indicator_target, buttons, joltage_target))

# def indicators_from_buttons(buttons, presses, indicator_size):
#     indicators = [False]*indicator_size
#     for i, press in enumerate(presses):
#         if press == 0:
#             continue
#         button = buttons[i]
#         for j in button:
#             indicators[j] = not indicators[j]
#     return indicators

# def press_pattern(length):
#     if length == 1:
#         yield [0]
#         yield [1]
#     else:
#         for pattern in press_pattern(length-1):
#             yield [0, *pattern]
#             yield [1, *pattern]

# min_presses = []
# for indicator_target, buttons, _ in machines:
#     min_press = len(buttons)
#     for presses in press_pattern(len(buttons)):
#         indicators = indicators_from_buttons(buttons, presses, len(indicator_target))
#         # print(f"{buttons} {presses} {indicator_target} {indicators}")
#         if indicator_target == indicators:
#             min_press = min(min_press, sum(presses))
#     min_presses.append(min_press)
# print(sum(min_presses))

total = 0
for _, buttons, joltage_target in machines:
    costs = [1]*len(buttons)
    eqs = [[i in b for b in buttons] for i in range(len(joltage_target))]

    total += linprog(costs, A_eq=eqs, b_eq=joltage_target, integrality=1).fun
print(int(total))

