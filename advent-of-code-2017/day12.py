data1 = data.split("\n")
dict_programs = {}
for line in data1:
    node = int(line.split("<->")[0])
    leafs = [int(x) for x in (line.split("<->")[1]).split(",")]
    dict_programs[node] = leafs


def part_1(initial_node, dict_programs):
    seen = set()
    node_to_check = []
    node_checked = set()

    node_to_check.append(initial_node)

    while len(node_to_check) != 0:
        temp = node_to_check.pop()
        seen.add(temp)
        for leaf in dict_programs[temp]:
            if leaf not in node_checked:
                node_to_check.append(leaf)
        node_checked.add(temp)
    return len(seen)


print("Solution Part 1:", part_1(0, dict_programs))


def part_2(n_programs, dict_programs):
    totals = []
    for x in range(n_programs):
        totals.append(part_1(x, dict_programs))

    groups = 0
    for x in set(totals):
        groups += totals.count(x) / x

    return groups


print("Solution Part 2:", part_2(len(data1), dict_programs))
