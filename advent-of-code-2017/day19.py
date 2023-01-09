import numpy as np

data = [list(line) for line in imput_data.split("\n")]
matrix = np.matrix(data)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
for n in range(matrix[0].size):
    if matrix[0, n] == "|":
        position = np.array([0, n])
direction = "down"
last_letter = "Q"
solution = ""

valor = matrix[tuple(position)]
while valor != last_letter:

    if direction == "down":
        position += [1, 0]
    elif direction == "up":
        position += [-1, 0]
    elif direction == "left":
        position += [0, -1]
    elif direction == "right":
        position += [0, 1]
    valor = matrix[tuple(position)]
    if valor == "+":
        if direction == "down" or direction == "up":
            if (
                matrix[tuple(position + [0, 1])] == "-"
                or matrix[tuple(position + [0, 1])] in letters
            ):
                direction = "right"
            elif (
                matrix[tuple(position + [0, -1])] == "-"
                or matrix[tuple(position + [0, -1])] in letters
            ):
                direction = "left"
        elif direction == "left" or direction == "right":
            if (
                matrix[tuple(position + [1, 0])] == "|"
                or matrix[tuple(position + [1, 0])] in letters
            ):
                direction = "down"
            elif (
                matrix[tuple(position + [-1, 0])] == "|"
                or matrix[tuple(position + [-1, 0])] in letters
            ):
                direction = "up"
    elif valor in letters:
        solution += valor

print("Solution part 1:", solution)

# Part 2
for n in range(matrix[0].size):
    if matrix[0, n] == "|":
        position = np.array([0, n])
direction = "down"
last_letter = "Q"
solution = 1

valor = matrix[tuple(position)]
while valor != last_letter:

    if direction == "down":
        position += [1, 0]
    elif direction == "up":
        position += [-1, 0]
    elif direction == "left":
        position += [0, -1]
    elif direction == "right":
        position += [0, 1]
    valor = matrix[tuple(position)]
    solution += 1
    if valor == "+":
        if direction == "down" or direction == "up":
            if (
                matrix[tuple(position + [0, 1])] == "-"
                or matrix[tuple(position + [0, 1])] in letters
            ):
                direction = "right"
            elif (
                matrix[tuple(position + [0, -1])] == "-"
                or matrix[tuple(position + [0, -1])] in letters
            ):
                direction = "left"
        elif direction == "left" or direction == "right":
            if (
                matrix[tuple(position + [1, 0])] == "|"
                or matrix[tuple(position + [1, 0])] in letters
            ):
                direction = "down"
            elif (
                matrix[tuple(position + [-1, 0])] == "|"
                or matrix[tuple(position + [-1, 0])] in letters
            ):
                direction = "up"


print("Solution part 2:", solution)
