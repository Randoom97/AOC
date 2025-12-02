from input import input

paths = {}

def hasBeenVisited(node: str, visited: set):
    if (node == "start" and node in visited) or (node == "end" and node in visited):
        return True
    doubleVisited = False
    for cave in visited:
        if cave.endswith('2'):
            doubleVisited = True
            break
    if (doubleVisited and node in visited):
        return True
    return False

def visit(node, visited: set):
    if node in visited:
        visited.add(node+"2")
    else:
        visited.add(node)

def unvisit(node, visited: set):
    if node+"2" in visited:
        visited.remove(node+"2")
    elif node in visited:
        visited.remove(node)

def search(node: str, visited: set):
    if hasBeenVisited(node, visited):
        return 0
    if node == "end":
        return 1
    if node == node.lower():
        visit(node, visited)
    pathCount = 0
    for neighbor in paths[node]:
        pathCount += search(neighbor, visited)
    unvisit(node, visited)
    return pathCount

for edge in input:
    points = edge.split('-')
    if points[0] not in paths:
        paths[points[0]] = set()
    paths[points[0]].add(points[1])
    if points[1] not in paths:
        paths[points[1]] = set()
    paths[points[1]].add(points[0])

print(search("start", set()))