from input import shapes, spaces
import math

# yes the problem was constructed in a way that a simple count works
shape_sizes = []
shape_size = 0
for line in shapes[1:]:
    if ":" in line:
        shape_sizes.append(shape_size)
        shape_size = 0
        continue
    shape_size += sum(map(lambda x: 1 if x == '#' else 0, line))
shape_sizes.append(shape_size)

can_fit = 0
for line in spaces:
    area_size, shape_counts = line.split(":")
    area_size = math.prod(map(int, area_size.split("x")))
    shape_counts = list(map(int, shape_counts.strip().split()))
    shape_area_size = sum([sc*ss for sc, ss in zip(shape_counts, shape_sizes)])
    if area_size >= shape_area_size:
        can_fit += 1
print(can_fit)