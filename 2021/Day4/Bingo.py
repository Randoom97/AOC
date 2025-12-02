from input import input, grids
from BingoBoard import Board

boards = []

for grid in grids:
    boards.append(Board(grid))

# for val in input:
#     for board in boards:
#         if board.mark(val):
#             print(board.value()*val)
#             exit()

for val in input:
    boardsToRemove = []
    for board in boards:
        if board.mark(val):
            boardsToRemove.append(board)
            if(len(boards) - len(boardsToRemove) == 0):
                print(board.value()*val)
                exit()
    for boardToRemove in boardsToRemove:
        boards.remove(boardToRemove)
            