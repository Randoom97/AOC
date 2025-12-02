from input import input

cubes = set()
lineCount = len(input)
linesCompleted = 0
for line in input:
    print(str(linesCompleted)+"/"+str(lineCount))
    instruction = line.split(' ')
    linesCompleted += 1
    command = instruction[0]
    bounds = instruction[1].split(',')
    xrange = bounds[0].split('=')[1].split('..')
    yrange = bounds[1].split('=')[1].split('..')
    zrange = bounds[2].split('=')[1].split('..')
    for x in range(int(xrange[0]), int(xrange[1])+1):
        for y in range(int(yrange[0]), int(yrange[1])+1):
            for z in range(int(zrange[0]), int(zrange[1])+1):
                cube = (x,y,z)
                if command == 'on':
                    cubes.add(cube)
                elif cube in cubes:
                    cubes.remove(cube)
print(len(cubes))
                    

