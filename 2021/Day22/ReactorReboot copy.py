from input import input

class Cube:
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, sign=1):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.sign = sign

    def cubeIntersection(self, otherCube):
        xmin = max(self.xmin, otherCube.xmin)
        xmax = min(self.xmax, otherCube.xmax)
        ymin = max(self.ymin, otherCube.ymin)
        ymax = min(self.ymax, otherCube.ymax)
        zmin = max(self.zmin, otherCube.zmin)
        zmax = min(self.zmax, otherCube.zmax)
        if xmin <= xmax and ymin <= ymax and zmin <= zmax:
            return Cube(xmin, xmax, ymin, ymax, zmin, zmax, -self.sign)
        else:
            return None
    
    def area(self):
        # print(self.xmax-self.xmin+1)
        # print(self.ymax-self.ymin+1)
        # print(self.zmax-self.zmin+1)
        return (self.xmax-self.xmin+1)*(self.ymax-self.ymin+1)*(self.zmax-self.zmin+1)*self.sign

cubes = []
lineCount = len(input)
linesCompleted = 0
for line in input:
    print(str(linesCompleted)+"/"+str(lineCount))
    linesCompleted += 1
    instruction = line.split(' ')
    command = instruction[0]
    bounds = instruction[1].split(',')
    xrange = bounds[0].split('=')[1].split('..')
    yrange = bounds[1].split('=')[1].split('..')
    zrange = bounds[2].split('=')[1].split('..')
    cube = Cube(int(xrange[0]), int(xrange[1]), int(yrange[0]), int(yrange[1]), int(zrange[0]), int(zrange[1]), 1 if command == 'on' else -1)
    newCubes = cubes.copy()
    for otherCube in cubes:
        intersection = otherCube.cubeIntersection(cube)
        if intersection != None:
            newCubes.append(intersection)
    if command == 'on':
        newCubes.append(cube)
    cubes = newCubes

totalArea = 0
for cube in cubes:
    totalArea += cube.area()
print(totalArea)
                    

