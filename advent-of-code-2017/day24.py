nodes = []
for item in data:
    item[0] = int(item[0])
    item[1] = int(item[1])
    nodes.append(tuple(item))
duplicates = []
for node in nodes:
    if node[0] == node[1]:
        duplicates.append(node[0])

graph = {}
to_check = [tuple([0, 0])]
seen = set()

while to_check:
    item = to_check.pop()
    graph[item] = set()
    seen.add(item)
    for i in nodes:
        if i != item:
            if i[0] in item or i[1] in item:
                graph[item].add(i)
                if not i in seen:
                    to_check.append(i)

# Part 1
def dfs_paths(graph, start, initial, goal):
    stack = [(start, [start], initial)]
    while stack:
        (vertex, path, bond) = stack.pop()
        can_go = set()
        for posible in graph[vertex]:
            if bond in posible:
                can_go.add(posible)
        for next in can_go - set(path):
            if next == goal:
                yield path + [next]
            else:
                if next[0] == bond:
                    temp = next[1]
                else:
                    temp = next[0]
                stack.append((next, path + [next], temp))


totals = []
for node in graph.keys():
    total = 0
    for element in dfs_paths(graph, tuple([0, 0]), 0, node):
        sol = sum([sum(number) for number in element])
        if sol > total:
            total = sol
    totals.append(total)
    # print(node,total)
print("Solution Part 1", max(totals))


# Part 2
def dfs_paths(graph, start, initial, goal):
    stack = [(start, [start], initial)]
    while stack:
        (vertex, path, bond) = stack.pop()
        can_go = set()
        for posible in graph[vertex]:
            if bond in posible:
                can_go.add(posible)
        for next in can_go - set(path):
            if next == goal:
                yield path + [next]
            else:
                if next[0] == bond:
                    temp = next[1]
                else:
                    temp = next[0]
                stack.append((next, path + [next], temp))


total = 0
strong = 0
for node in graph.keys():
    for element in dfs_paths(graph, tuple([0, 0]), 0, node):
        long = len(element)
        sol = sum([sum(number) for number in element])
        if long > total:
            total = long
            strong = sol
        elif long == total:
            if sol > strong:
                strong = sol
    totals.append([total, strong])
    # print(node,total,strong)
print("Solution Part 1", strong)
