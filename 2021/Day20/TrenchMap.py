from input import algo, input

class Image:
    def __init__(self, image, depth=1):
        self.image = image
        self.depth = depth
        self.rowCount = len(self.image)
        self.colCount = len(self.image)

    def getPixel(self, row, col):
        if row < 0 or row >= self.rowCount or col < 0 or col >= self.colCount:
            return (1 if self.depth%2 == 0 else 0)
        else:
            return (1 if self.image[row][col] == '#' else 0)

    def lookup(self, row, col):
        index = 0
        for subRow in range(row-1, row+2):
            for subCol in range(col-1, col+2):
                index <<= 1
                index += self.getPixel(subRow, subCol)
        return index

    def enhance(self):
        newImageBuffer = []
        for row in range(-1, self.rowCount+1):
            rowData = []
            for col in range(-1, self.colCount+1):
                rowData.append(algo[self.lookup(row, col)])
            newImageBuffer.append(rowData)
        return Image(newImageBuffer, self.depth+1)

    def printImage(self):
        for row in range(0, self.rowCount):
            for col in range(0, self.colCount):
                print(self.image[row][col], end='')
            print('')


imageBuffer = []
for line in input:
    rowData = []
    for char in line:
        rowData.append(char)
    imageBuffer.append(rowData)

image = Image(imageBuffer)

for i in range(50):
    print(i)
    image = image.enhance()
count = 0
for row in image.image:
    for char in row:
        if char == "#":
            count += 1

print(count)