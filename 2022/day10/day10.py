from input import input

x = 1
cycle = 0
image = ['']

def incrementCycle():
    global cycle
    if cycle % 40 == 0:
        image.append('')
    if abs((cycle % 40) - x) <= 1:
        image[cycle//40] += '▓'
    else:
        image[cycle//40] += '░'
    cycle += 1

for line in input:
    if line.startswith("noop"):
        incrementCycle()
    elif line.startswith("addx"):
        value = int(line.split(' ')[1])
        incrementCycle()
        incrementCycle()
        x += value

for line in image:
    print(line)
