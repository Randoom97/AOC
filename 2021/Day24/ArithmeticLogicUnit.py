from input import instructions

number = 100000000000000
while True:
    number -= 1
    if number % 10000 == 0:
        print(number)
    input = []
    numberc = number
    invalid = False
    while numberc > 0:
        digit = numberc % 10
        if digit == 0:
            invalid = True
            break
        input.append(numberc % 10)
        numberc //= 10
    if invalid:
        continue
    input.reverse()

    registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def getValue(arg):
        if arg in registers:
            return registers[arg]
        else:
            return int(arg)

    for instruction in instructions:
        parts = instruction.split(' ')
        opcode = parts[0]
        arg1 = parts[1]
        arg2 = None if len(parts) != 3 else parts[2]

        if opcode == 'inp':
            registers[arg1] = input.pop(0)
        elif opcode == 'add':
            registers[arg1] = getValue(arg1) + getValue(arg2)
        elif opcode == 'mul':
            registers[arg1] = getValue(arg1) * getValue(arg2)
        elif opcode == 'div':
            registers[arg1] = getValue(arg1) // getValue(arg2)
        elif opcode == 'mod':
            registers[arg1] = getValue(arg1) % getValue(arg2)
        elif opcode == 'eql':
            registers[arg1] = 1 if getValue(arg1) == getValue(arg2) else 0
    if registers['z'] == 0:
        break

print("Finished with number: "+str(number))