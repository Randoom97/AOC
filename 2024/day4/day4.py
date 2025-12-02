from input import input

def scan(word, row, col, drow, dcol, board):
    if word == "":
        return True
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    if board[row][col] != word[0]:
        return False
    return scan(word[1:], row+drow, col+dcol, drow, dcol, board)
    

def wordCount(word, board):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != word[0]:
                continue
            if scan(word, row, col, 0, 1, board):
                count += 1
            if scan(word, row, col, 1, 1, board):
                count += 1
            if scan(word, row, col, 1, 0, board):
                count += 1
            if scan(word, row, col, 1, -1, board):
                count += 1
            if scan(word, row, col, 0, -1, board):
                count += 1
            if scan(word, row, col, -1, -1, board):
                count += 1
            if scan(word, row, col, -1, 0, board):
                count += 1
            if scan(word, row, col, -1, 1, board):
                count += 1
    return count

def crossCount(board):
    count = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != "A":
                continue
            if scan("MAS", row-1, col-1, 1, 1, board) and scan("MAS", row+1, col-1, -1, 1, board):
                count += 1
            if scan("MAS", row+1, col-1, -1, 1, board) and scan("MAS", row+1, col+1, -1, -1, board):
                count += 1
            if scan("MAS", row+1, col+1, -1, -1, board) and scan("MAS", row-1, col+1, 1, -1, board):
                count += 1
            if scan("MAS", row-1, col+1, 1, -1, board) and scan("MAS", row-1, col-1, 1, 1, board):
                count += 1
    return count



print(crossCount(input))