gridSize = 5

class Board:
    def __init__(self, grid):
        self.marked = [0]*(gridSize*gridSize)
        self.indexer = {}
        self.grid = grid
        for idx, val in enumerate(self.grid):
            self.indexer[val] = idx

    def mark(self, val):
        if val in self.indexer.keys():
            idx = self.indexer[val]
            self.marked[idx] = 1
            return self.checkRow(idx) or self.checkColumn(idx)
        return False
    
    def checkRow(self, idx):
        rowStart = idx - idx % gridSize
        for idx2 in range(rowStart, rowStart+gridSize):
            if self.marked[idx2] == 0:
                return False
        return True

    def checkColumn(self, idx):
        colStart = idx % gridSize
        for idx2 in range(colStart, gridSize*gridSize, gridSize):
            if self.marked[idx2] == 0:
                return False
        return True

    def value(self):
        count = 0
        for idx in range(gridSize*gridSize):
            if self.marked[idx] == 0:
                count += self.grid[idx]
        return count