from input import input

scoreMap = {'(': 1, '[': 2, '{': 3, '<': 4}
scores = []

for chunk in input:
    corrupted = False
    stack = []
    for char in chunk:
        if char in {'(', '[', '{', '<'}:
            stack.append(char)
        elif (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{') or (char == '>' and stack[-1] == '<'):
            stack.pop()
        else:
            corrupted = True
            break
    if corrupted:
        continue
    stack.reverse()
    score = 0
    for char in stack:
        score *= 5
        score += scoreMap[char]
    scores.append(score)

scores.sort()
print(scores[len(scores)//2])