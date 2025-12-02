from input import input

class OctoGrid:
    def __init__(self, grid):
        self.grid = grid
        self.numRow = len(grid)
        self.numCol = len(grid[0])

    def step(self):
        # First, the energy level of each octopus increases by 1
        for row in range(self.numRow):
            for col in range(self.numCol):
                self.grid[row][col] += 1

        alreadyFlashed = set()
        # Then, any octopus with a level greater than 9 flashes. This increases the energy level of all adjacent octopi by 1
        flashedCount = 0
        while True:
            flashed = False
            for row in range(self.numRow):
                for col in range(self.numCol):
                    if self.grid[row][col] > 9 and (row, col) not in alreadyFlashed:
                        alreadyFlashed.add((row, col))
                        self.flashAdjacent(row, col)
                        flashed = True
                        flashedCount += 1
            if not flashed:
                break

        for coord in alreadyFlashed:
            self.grid[coord[0]][coord[1]] = 0
        return flashedCount

    def flashAdjacent(self, row, col):
        for adjRow in range(row-1, row+2):
            for adjCol in range(col-1, col+2):
                if adjRow < 0 or adjRow >= self.numRow or adjCol < 0 or adjCol >= self.numCol or (adjRow == row and adjCol == col):
                   continue
                self.grid[adjRow][adjCol] += 1
        

octoGrid = OctoGrid(input)

step = 0
while True:
    step += 1
    flashCount = octoGrid.step()
    if flashCount == octoGrid.numRow*octoGrid.numCol:
        break

print(step)

