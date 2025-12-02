from input import input

inputWidth = len(input)
inputHeight = len(input[0])

def scenicScore(x, y):
    height = input[x][y]
    right = 0
    for x1 in range(x+1, inputWidth):
        right += 1
        if height <= input[x1][y]:
            break
    left = 0
    for x1 in range(x-1, -1, -1):
        left += 1
        if height <= input[x1][y]:
            break
    down = 0
    for y1 in range(y+1, inputHeight):
        down += 1
        if height <= input[x][y1]:
            break
    up = 0
    for y1 in range(y-1, -1, -1):
        up += 1
        if height <= input[x][y1]:
            break
    # print('x:'+str(x)+' y:'+str(y)+' left:'+str(left)+' right:'+str(right)+' down:'+str(down)+' up:'+str(up)+' score:'+str(left*right*down*up))
    return left * right * down * up


maxScenicScore = 0
for x in range(inputWidth):
    for y in range(inputHeight):
        score = scenicScore(x,y)
        maxScenicScore = max(score, maxScenicScore)
print(maxScenicScore)


# visible=[]
# for x in range(inputWidth):
#     row = []
#     for y in range(inputWidth):
#         row.append(0)
#     visible.append(row)

# for x in range(inputWidth):
#     height = -1
#     for y in range(inputHeight):
#         if input[x][y] > height:
#             visible[x][y] = 1
#             height = input[x][y]
#     height = -1
#     for y in range(inputHeight-1, 0, -1):
#         if input[x][y] > height:
#             visible[x][y] = 1
#             height = input[x][y]

# for y in range(inputHeight):
#     height = -1
#     for x in range(inputWidth):
#         if input[x][y] > height:
#             visible[x][y] = 1
#             height = input[x][y]
#     height = -1
#     for x in range(inputWidth-1, 0, -1):
#         if input[x][y] > height:
#             visible[x][y] = 1
#             height = input[x][y]
# for line in visible:
#     print(line)
# print(sum([item for sublist in visible for item in sublist], 0))