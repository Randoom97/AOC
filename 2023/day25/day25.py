from input import input

def processInput(input):
    graph: dict[str, set[str]] = {}
    for line in input:
        label, connections = line.split(":")
        connections = connections.strip().split()
        if label not in graph:
            graph[label] = set()
        for connection in connections:
            graph[label].add(connection)
            if connection not in graph:
                graph[connection] = set()
            graph[connection].add(label)
    return graph

def calculateBetweenness(graph):
    betweenness = {}
    graphKeys = graph.keys()
    for key in graphKeys:
        stack = []
        stack.append((key, [key]))
        visited = set()
        while stack:
            current, history = stack.pop(0)
            if current in visited:
                continue
            visited.add(current)
            if len(history) > 1:
                for i in range(len(history)-1):
                    if (history[i], history[i+1]) not in betweenness:
                        betweenness[(history[i], history[i+1])] = 0
                    betweenness[(history[i], history[i+1])] += 1
                    if (history[i+1], history[i]) not in betweenness:
                        betweenness[(history[i+1], history[i])] = 0
                    betweenness[(history[i+1], history[i])] += 1
            for node in graph[current]:
                newHistory = history.copy()
                newHistory.append(node)
                stack.append((node, newHistory))
    return betweenness

def subGraphs(graph: dict[str, set[str]], removedEdges):
    graphKeys = list(graph.keys())
    graphSets = []
    for key in graphKeys:
        alreadyFound = False
        for graphSet in graphSets:
            if key in graphSet:
                alreadyFound = True
                break
        if alreadyFound:
            continue
        stack = []
        visited = set()
        stack.append(key)
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for node in graph[current]:
                if (current, node) in removedEdges or (node, current) in removedEdges:
                    continue
                stack.append(node)
        graphSets.append(visited)
    return graphSets

graph = processInput(input)

highestBetweenness = [0, 0, 0]
highestEdge: list[tuple[str, str]] = [None, None, None]
for i in range(3):
    # print()
    # for key in graph:
    #     print(key + ": " + str(graph[key]))
    betweenness = calculateBetweenness(graph)
    for key in betweenness:
        if betweenness[key] > highestBetweenness[i]:
            highestBetweenness[i] = betweenness[key]
            highestEdge[i] = key
    if highestEdge[i] != None:
        node1, node2 = highestEdge[i]
        print(str(node1) + " " + str(node2))
        graph[node1].remove(node2)
        graph[node2].remove(node1)
graphs = subGraphs(graph, [])
print(len(graphs))
print(len(graphs[0]), len(graphs[1]))
        
    
# pairs = []
# graphKeys = list(graph.keys())
# for i in range(len(graphKeys)-1):
#     for j in range(i+1, len(graphKeys)):
#         if graphKeys[j] in graph[graphKeys[i]]:
#             pairs.append((graphKeys[i], graphKeys[j]))

# print(len(pairs))

# for i in range(len(pairs)-2):
#     for j in range(i+1, len(pairs)-1):
#         for k in range(j+1, len(pairs)):
#             # print(str(i) + " " + str(j) + " " + str(k))
#             removedEdges = [pairs[i], pairs[j], pairs[k]]
#             graphSets = subGraphs(graph, removedEdges)
#             if len(graphSets) == 2:
#                 print(len(graphSets[0])*len(graphSets[1]))