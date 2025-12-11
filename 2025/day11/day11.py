from input import input

graph = {}
for line in input:
    node, adjacent = line.split(":")
    graph[node] = {adj: 1 for adj in adjacent.strip().split()}

def squash_graph(keep_nodes):
    to_squash = set(graph.keys())
    for node in keep_nodes:
        to_squash.remove(node)
    for squash_key in to_squash:
        # print(graph)
        # print(squash_key)
        adjacents = graph[squash_key]
        for key in graph:
            if squash_key in graph[key]:
                count = graph[key][squash_key]
                del graph[key][squash_key]
                for adjacent in adjacents:
                    if adjacent not in graph[key]:
                        graph[key][adjacent] = 0
                    graph[key][adjacent] += count * adjacents[adjacent]
        del graph[squash_key]
squash_graph(["fft", "dac", "svr"])
# print(graph)

def path_count(start, end):
    pc = 0
    stack = [(start, 1)]
    while len(stack) != 0:
        next, count = stack.pop()
        if next == end:
            pc += count
            continue
        if next in graph:
            for adjacent in graph[next]:
                stack.append((adjacent, graph[next][adjacent]))
    return pc

dac_fft_count = path_count("svr", "dac") * path_count("dac", "fft") * path_count("fft", "out")
fft_dac_count = path_count("svr", "fft") * path_count("fft", "dac") * path_count("dac", "out")

print(dac_fft_count + fft_dac_count)