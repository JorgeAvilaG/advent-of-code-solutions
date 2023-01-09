data = input_data.split("\n")
tree = {}
weights = {}
nodes_total = set()
leafs_total = set()

# Create the tree
for line in data:
    if " -> " in line:
        temp = line.split(" -> ")
        node = temp[0].split(" ")[0]
        leafs = temp[1].split(", ")
        tree[node] = leafs
        weights[node] = int(temp[0].split(" ")[1].split("(")[1].split(")")[0])
        nodes_total.add(node)
        for leaf in leafs:
            leafs_total.add(leaf)
    else:
        node = line.split(" ")[0]
        leafs = []
        tree[node] = leafs
        weights[node] = int(line.split(" ")[1].split("(")[1].split(")")[0])
        nodes_total.add(node)

# Part 1
import numpy as np

for x in nodes_total:
    if x not in leafs_total:
        print("Solution part 1:", x)

# Part 2
def cal_sum(node):
    if tree[node] == []:
        return weights[node]
    else:
        total = weights[node]
        for leaf in tree[node]:
            total += cal_sum(leaf)
        return total


def checking_diference(node, correct_value):
    leafs = tree[node]
    if not leafs == []:
        whs = [cal_sum(leaf) for leaf in leafs]
        for n, element in enumerate(whs):
            if whs.count(element) == 1:
                diference = element - whs[np.mod(n + 1, len(whs))]
                correct_value = weights[leafs[n]] - diference
                return checking_diference(leafs[n], correct_value)
        return correct_value


print("Solution part 2:", checking_diference("bpvhwhh", 0))
