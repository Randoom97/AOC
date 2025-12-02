from input import data, boardDim

def debugPrint():
    board = []
    for _ in range(boardDim[1]):
        board.append([0]*boardDim[0])
    for robot in data:
        board[robot[1]][robot[0]] += 1
    for row in board:
        rowString = ""
        for col in row:
            rowString += str(col) if col > 0 else '.'
        print(rowString)

def step():
    for robot in data:
        robot[0] = (robot[0]+robot[2])%boardDim[0]
        robot[1] = (robot[1]+robot[3])%boardDim[1]

for i in range(6752):
    step()
debugPrint()

# for i in range(57):
#     step()
# while True:
#     print(i)
#     debugPrint()
#     input()
#     for j in range(103):
#         step()
#     i+=103
# debugPrint()

tlcount = 0
trcount = 0
blcount = 0
brcount = 0
for robot in data:
    if robot[0] < boardDim[0]//2 and robot[1] < boardDim[1]//2:
        tlcount += 1
    if robot[0] > boardDim[0]//2 and robot[1] < boardDim[1]//2:
        trcount += 1
    if robot[0] < boardDim[0]//2 and robot[1] > boardDim[1]//2:
        blcount += 1
    if robot[0] > boardDim[0]//2 and robot[1] > boardDim[1]//2:
        brcount += 1
print(tlcount*trcount*blcount*brcount)
    