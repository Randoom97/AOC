from input import input, stacks

for instruction in input:
    for item in stacks[instruction[1]-1][-instruction[0]:]:
        stacks[instruction[2]-1].append(item)
    stacks[instruction[1]-1] = stacks[instruction[1]-1][:-instruction[0]]
for stack in stacks:
    print(stack.pop().capitalize(), end='')
print()