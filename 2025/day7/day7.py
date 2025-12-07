from typing import Dict
from input import input

# manifold = [list(line) for line in input]

# for row in range(len(manifold)-1):
#     for col in range(len(manifold[0])):
#         m_char = manifold[row][col]
#         if m_char == 'S' or m_char == '|':
#             if manifold[row+1][col] == '^':
#                 manifold[row+1][col+1] = '|'
#                 manifold[row+1][col-1] = '|'
#             else:
#                 manifold[row+1][col] = '|'

# # for row in manifold:
# #     print(''.join(row))

# split_count = 0
# for row in range(1, len(manifold)):
#     for col in range(len(manifold[0])):
#         if manifold[row][col] == '^' and manifold[row-1][col] == '|':
#             split_count += 1
# print(split_count)

s_pos = (0,0)
splitters = set()
end_row = len(input)
for row, line in enumerate(input):
    for col, char in enumerate(line):
        if char == 'S':
            s_pos = (row, col)
        if char == '^':
            splitters.add((row, col))

beams = {s_pos: 1}
for _ in range(end_row):
    new_beams = {}
    for beam in beams:
        row, col = beam
        beam_value = beams[beam]
        if (row+1, col) in splitters:
            left = (row+1, col-1)
            if left not in new_beams:
                new_beams[left] = 0
            new_beams[left] += beam_value
            right = (row+1, col+1)
            if right not in new_beams:
                new_beams[right] = 0
            new_beams[right] += beam_value
        else:
            down = (row+1, col)
            if down not in new_beams:
                new_beams[down] = 0
            new_beams[down] += beam_value
    beams = new_beams
print(sum(beams.values()))