from input import input

aim = 0
position = 0
depth = 0
for line in input:
    command = line.split(" ")
    if command[0] == "forward":
        position += int(command[1])
        depth += aim*int(command[1])
    if command[0] == "down":
        aim += int(command[1])
    if command[0] == "up":
        aim -= int(command[1])
print("Position * Depth = " + str(position * depth))