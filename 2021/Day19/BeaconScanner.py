from input import input

class Scanner:
    def __init__(self, beacons):
        self.beacons = set(beacons)
        self.pos = (0,0,0)

    def rotateX(self):
        newBeacons = []
        for beacon in self.beacons:
            newBeacons.append((beacon[0], beacon[2], -beacon[1]))
        return Scanner(newBeacons)
    
    def rotateY(self):
        newBeacons = []
        for beacon in self.beacons:
            newBeacons.append((beacon[2], beacon[1], -beacon[0]))
        return Scanner(newBeacons)

    def rotateZ(self):
        newBeacons = []
        for beacon in self.beacons:
            newBeacons.append((beacon[1], -beacon[0], beacon[2]))
        return Scanner(newBeacons)

    def translate(self,x,y,z):
        newBeacons = []
        for beacon in self.beacons:
            newBeacons.append((beacon[0]+x, beacon[1]+y, beacon[2]+z))
        newScanner = Scanner(newBeacons)
        newScanner.pos = (self.pos[0]+x, self.pos[1]+y, self.pos[2]+z)
        return newScanner

    def copy(self):
        return Scanner(list(self.beacons))

def checkMatch(scanner1: Scanner, scanner2: Scanner):
    for s1beacon in scanner1.beacons:
        for s2beacon in scanner2.beacons:
            transx = s1beacon[0] - s2beacon[0]
            transy = s1beacon[1] - s2beacon[1]
            transz = s1beacon[2] - s2beacon[2]
            transScanner = scanner2.translate(transx, transy, transz)
            intersection = scanner1.beacons.intersection(transScanner.beacons)
            if len(intersection) >= 12:
                return transScanner
    return None

def checkOrientations(scanner1: Scanner, scanner2: Scanner):
    scanner2c = scanner2
    for _ in range(4):
        result = checkMatch(scanner1, scanner2c)
        if result != None:
            return result
        scanner2c = scanner2c.rotateX()
    scanner2c = scanner2.rotateY().rotateY()
    for _ in range(4):
        result = checkMatch(scanner1, scanner2c)
        if result != None:
            return result
        scanner2c = scanner2c.rotateX()
    return None

scanners = []
for beacons in input:
    scanners.append(Scanner(beacons))

groundTruths = []
groundTruths.append(scanners.pop(0))
while len(scanners) > 0:
    print(len(scanners))
    for truthScanner in groundTruths:
        match = False
        for sidx, scanner in enumerate(scanners):
            scannerc = scanner
            result = checkOrientations(truthScanner, scannerc)
            if result != None:
                groundTruths.append(result)
                scanners.pop(sidx)
                match = True
                break
            scannerc = scanner.rotateZ()
            result = checkOrientations(truthScanner, scannerc)
            if result != None:
                groundTruths.append(result)
                scanners.pop(sidx)
                match = True
                break
            scannerc = scanner.rotateY()
            result = checkOrientations(truthScanner, scannerc)
            if result != None:
                groundTruths.append(result)
                scanners.pop(sidx)
                match = True
                break
        if match:
            break

largestDist = 0
for truth1 in groundTruths:
    for truth2 in groundTruths:
        dist = abs(truth1.pos[0] - truth2.pos[0]) + abs(truth1.pos[1] - truth2.pos[1]) + abs(truth1.pos[2] - truth2.pos[2])
        if dist > largestDist:
            largestDist = dist
print(largestDist)


