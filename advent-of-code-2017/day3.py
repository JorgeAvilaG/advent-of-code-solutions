input_number = 347991
import numpy as np
import math


def move_right(pos):
    pos[0] += 1


def move_left(pos):
    pos[0] -= 1


def move_up(pos):
    pos[1] += 1


def move_down(pos):
    pos[1] -= 1


def check_pos(pos):
    total = 0
    if (pos[0], pos[1]) in dict_pos:
        return dict_pos[(pos[0], pos[1])]
    else:
        for i in range(pos[0] - 1, pos[0] + 2):
            for j in range(pos[1] - 1, pos[1] + 2):
                if (i, j) in dict_pos:
                    total += dict_pos[(i, j)]

        return total


# Part 1

# States:
# 0: move right
# 1: move up
# 2: move left
# 3: move down

state = 0
pos = [0, 0]
counter = 1
while counter < input_number:
    counter += 1
    if state == 0 and pos[0] <= abs(pos[1]):
        move_right(pos)

    elif state == 1 and not pos[0] == pos[1]:
        move_up(pos)

    elif state == 2 and not pos[0] == -1 * pos[1]:
        move_left(pos)

    elif state == 3 and not pos[0] == pos[1]:
        move_down(pos)

    else:  # pass to the next state
        state = np.mod(state + 1, 4)
        counter -= 1

print("Solution part 1:", (abs(pos[0]) + abs(pos[1])))

# Part 2

# States:
# 0: move right
# 1: move up
# 2: move left
# 3: move down

state = 0
pos = [0, 0]
dict_pos = {(pos[0], pos[1]): 1}
counter = 1
while counter < input_number:
    dict_pos[(pos[0], pos[1])] = check_pos(pos)
    counter = dict_pos[(pos[0], pos[1])]
    if state == 0 and pos[0] <= abs(pos[1]):
        move_right(pos)

    elif state == 1 and not pos[0] == pos[1]:
        move_up(pos)

    elif state == 2 and not pos[0] == -1 * pos[1]:
        move_left(pos)

    elif state == 3 and not pos[0] == pos[1]:
        move_down(pos)

    else:  # pass to the next state
        state = np.mod(state + 1, 4)


print("Solution part 2:", counter)
