import numpy as np


def update_data(data):

    new_data = []
    for car in data:
        new_data.append(ord(car))
    extra = [17, 31, 73, 47, 23]
    for number in extra:
        new_data.append(number)
    return new_data


def reverse_list(n0, n1, array):

    if n1 > len(array):
        b = array[n0:] + array[: np.mod(n1, len(array))]
        b.reverse()
        array[n0:] = b[: len(array[n0:])]
        array[: np.mod(n1, len(array))] = b[len(array[n0:]) :]
        return array
    else:
        b = array[n0:n1]
        b.reverse()
        array[n0:n1] = b
        return array


def XOR(array):
    solution = []
    n = 0
    while n < len(array):
        if n == 0:
            counter = array[n]
        elif n == len(array) - 1:
            counter = counter ^ array[n]
            solution.append(counter)
        elif np.mod(n, 16) == 0:
            solution.append(counter)
            counter = array[n]
        else:
            counter = counter ^ array[n]
        n += 1
    return solution


def hex_array(array):
    solution = ""
    for number in array:
        if len(str(hex(number))) == 4:
            solution += str(hex(number))[2:]
        else:
            solution += "0" + str(hex(number))[2:]
    return solution


def Knot_Hash(data):
    data1 = update_data(data)
    array = list(range(256))
    current_position = 0
    skip = 0
    for i in range(64):
        for jump_len in data1:
            array = reverse_list(current_position, current_position + jump_len, array)
            current_position = np.mod(current_position + jump_len + skip, len(array))
            skip += 1
    return hex_array(XOR(array))


def day_14(knot_hash):
    result = ""
    for car in knot_hash:
        temp = bin(int(car, 16)).split("0b")[1]
        while len(temp) < 4:
            temp = "0" + temp
        result += temp
    return result


# Part 1
data_input = "oundnydw"
solution = 0
for x in range(128):
    data = data_input + "-" + str(x)
    solution += day_14(Knot_Hash(data)).count("1")

print("Solution Part 1:", solution)

# Part 2


def expand_group(row, column, groups, matrix):
    checked = set()
    to_check = [(row, column)]
    while len(to_check) > 0:
        temp = to_check.pop()
        matrix[temp[0]][temp[1]] = groups
        checked.add(temp)
        if temp[0] > 0:
            if (
                matrix[temp[0] - 1][temp[1]] == -1
                and (temp[0] - 1, temp[1]) not in checked
            ):
                to_check.append((temp[0] - 1, temp[1]))
        if temp[0] < 127:
            if (
                matrix[temp[0] + 1][temp[1]] == -1
                and (temp[0] + 1, temp[1]) not in checked
            ):
                to_check.append((temp[0] + 1, temp[1]))
        if temp[1] > 0:
            if (
                matrix[temp[0]][temp[1] - 1] == -1
                and (temp[0], temp[1] - 1) not in checked
            ):
                to_check.append((temp[0], temp[1] - 1))
        if temp[1] < 127:
            if (
                matrix[temp[0]][temp[1] + 1] == -1
                and (temp[0], temp[1] + 1) not in checked
            ):
                to_check.append((temp[0], temp[1] + 1))


data_input = "oundnydw"
matrix = np.zeros([128, 128])

for x in range(128):
    data = data_input + "-" + str(x)
    line = day_14(Knot_Hash(data))

    for n, car in enumerate(line):
        if car == "1":
            matrix[x][n] = -1
groups = 0
for row in range(128):
    for column in range(128):
        if matrix[row][column] == -1:
            groups += 1
            expand_group(row, column, groups, matrix)

print("Solution part 2:", groups)
