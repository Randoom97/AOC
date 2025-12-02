from input import program, regA, regB, regC

IP = 0

output = []

def comboOperand(op):
    match op:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
        # case 7: # invalid
    return 0 # should never happen
            


def instruction(opcode, operand):
    global regA
    global regB
    global regC
    global IP
    global firstOutput
    match opcode:
        case 0:
            regA = int(regA/(2**comboOperand(operand)))
        case 1:
            regB = regB ^ operand
        case 2:
            regB = comboOperand(operand) % 8
        case 3:
            if regA != 0:
                IP = operand-2
        case 4:
            regB = regB ^ regC
        case 5:
            output.append(comboOperand(operand) % 8)
        case 6:
            regB = int(regA/(2**comboOperand(operand)))
        case 7:
            regC = int(regA/(2**comboOperand(operand)))
    IP += 2

def runProgram(value):
    global regA
    global regB
    global regC
    global IP
    global output
    
    regA = value
    regB = 0
    regC = 0
    IP = 0
    output = []

    while IP < len(program)-1:
        instruction(program[IP], program[IP+1])
    return output

# print(runProgram(regA))

def runProgram2(regA):
    output = []
    regB = 0
    regC = 0
    while True:
      regB = regA % 8
      regB = regB ^ 5
      regC = int(regA/(2**regB))
      regB = regB ^ 6
      regB = regB ^ regC
      output.append(regB % 8)
      regA >>= 3 # regA = int(regA/(2**3))
      if regA == 0:
          break
    return output

options = [0]
for i in range(len(program)):
    newOptions = []
    for j in range(8):
        for option in options:
            value = (option<<3)+j
            output = runProgram(value)
            expected = program[len(program)-i-1:]
            print("value="+str(value)+" output="+str(output)+" expected="+str(expected))
            if output == expected:
                newOptions.append(value)
    options = newOptions
    print(options)
    input()
options.sort()
print(options[0])
