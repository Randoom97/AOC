from input import network

vertecies = set()
map = {}
for pair in network:
    left, right = pair
    vertecies.add(left)
    vertecies.add(right)
    if left not in map:
        map[left] = set()
    map[left].add(right)
    if right not in map:
        map[right] = set()
    map[right].add(left)

def toTriTuple(list):
    list.sort()
    return (list[0], list[1], list[2])

# sets = set()
# for first in map:
#     for second in map[first]:
#         for third in map[second]:
#             if third in map[first] and (first[0] == 't' or second[0] == 't' or third[0] == 't'):
#                 sets.add(toTriTuple([first, second, third]))
# print(len(sets))

def BronKerbosch(R: set, P: set, X: set):
    if len(P) == 0 and len(X) == 0:
        return R
    results = []
    for v in P.copy():
        result = BronKerbosch(R.union(set([v])), P.intersection(map[v]), X.intersection(map[v]))
        if result != None:
            results.append((len(result), result))
        P.remove(v)
        X.add(v)
    results.sort()
    if len(results) == 0:
        return None
    return results.pop()[1]

largestClique = BronKerbosch(set(), vertecies ,set())
if largestClique == None:
    print("couldn't find a clique")
else:
    cliqueList = list(largestClique)
    cliqueList.sort()
    password = ""
    for node in cliqueList:
        password += node+","
    print(password)
