from input import input

# def is_valid_id(id: str) -> bool:
#     if len(id) % 2 == 1:
#         return True
#     char_dist = len(id) // 2
#     for i in range(char_dist):
#         if id[i] != id[i + char_dist]:
#             return True
#     return False

def is_valid_id(id: str) -> bool:
    max_char_dist = len(id) // 2
    for char_dist in range(1, max_char_dist+1):
        if len(id) % char_dist != 0:
            continue
        invalid_found = True
        for i in range(0, char_dist):
            for j in range(i, len(id)-char_dist, char_dist):
                if id[j] != id[j+char_dist]:
                    invalid_found = False
                    break
        if invalid_found:
            return False
    return True

total = 0
for line in input:
    [left, right] = line.split("-")
    for i in range(int(left), int(right) + 1):
        if not is_valid_id(str(i)):
            total += i
print(total)
