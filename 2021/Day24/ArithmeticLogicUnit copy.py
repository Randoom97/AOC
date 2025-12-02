import functools

from input import instructions, divZ, addX, addY

def run(digitIdx, z, digit):
    x = (z%26) + addX[digitIdx]
    z = z // divZ[digitIdx]
    if x != digit:
        z *= 26
        z += digit + addY[digitIdx]
    return z

Zbudget = [26**len([x for x in range(len(divZ)) if divZ[x]==26 and x >= i]) for i in range(len(divZ))]
CANDIDATES = list(range(1,10))
@functools.lru_cache(maxsize=None)
def search(ch, zsofar):
    if ch == 14:
        if zsofar == 0:
            return [""]
        return []
    if zsofar > Zbudget[ch]:
        return []
    xwillbe = addX[ch] + zsofar % 26
    wopts = CANDIDATES
    if xwillbe in range(1, 10):
        wopts = [xwillbe]
    ret = []
    for w in wopts:
        znext = run(ch, zsofar, w)
        nxt = search(ch+1,znext)
        for x in nxt:
            ret.append(str(w)+x)
    return ret

solns = search(0,0)
solns = [int(x) for x in solns]
print("num solutions", len(solns))
print(max(solns), min(solns))

# number = 100000000000000
# while number > 0:
#     number -= 1
#     if number % 100000 == 0:
#         print(number)
#     input = []
#     numberc = number
#     invalid = False
#     while numberc > 0:
#         digit = numberc % 10
#         if digit == 0:
#             invalid = True
#             break
#         input.append(numberc % 10)
#         numberc //= 10
#     if invalid:
#         continue
#     input.reverse()

#     z = 0
#     for digitIdx, digit in enumerate(input):
#         if digitIdx > 0 and digit != (z%26)+addX[digitIdx]:
#             break
#         z = run(digitIdx, z, digit)
#     if z == 0:
#         break

# print("Finished with number: "+str(number))