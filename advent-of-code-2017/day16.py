data = data.split(",")


def spin(x, p_list):
    x = int(x)
    temp = p_list[-x:] + p_list[:-x]
    return temp


def exchange(string, p_list):
    A, B = string.split("/")
    temp = p_list.copy()
    temp[int(A)], temp[int(B)] = temp[int(B)], temp[int(A)]
    return temp


def partner(string, p_list):
    A, B = string.split("/")
    A = p_list.index(A)
    B = p_list.index(B)
    temp = p_list.copy()
    temp[A], temp[B] = temp[B], temp[A]
    return temp


# part1
p_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
]

for dance in data:
    if dance[0] == "s":
        p_list = spin(dance[1:], p_list)
    elif dance[0] == "x":
        p_list = exchange(dance[1:], p_list)
    elif dance[0] == "p":
        p_list = partner(dance[1:], p_list)

solution = ""
for item in p_list:
    solution += item
print("Solution Part 1:", solution)

# part2
p_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
]

for x in range(60):
    for dance in data:
        if dance[0] == "s":
            p_list = spin(dance[1:], p_list)
        elif dance[0] == "x":
            p_list = exchange(dance[1:], p_list)
        elif dance[0] == "p":
            p_list = partner(dance[1:], p_list)

    if x == (1000000000 - 1) % 60:
        solution = ""
        for item in p_list:
            solution += item

        print("Solution Part 2:", solution, x)
