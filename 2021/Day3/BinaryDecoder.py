from input import input

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in input:
    for idx, char in enumerate(line):
        if char == "1":
            counts[idx] += 1
        if char == "0":
            counts[idx] -= 1
gama = 0
for val in counts:
    if val > 0:
        gama += 1
    gama <<= 1
gama >>= 1
epsilon = gama ^ 0b111111111111
print(epsilon * gama)