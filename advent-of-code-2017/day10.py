# Part 1
import numpy as np


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


data = [34, 88, 2, 222, 254, 93, 150, 0, 199, 255, 39, 32, 137, 136, 1, 167]
array = list(range(256))
current_position = 0
skip = 0
for jump_len in data:
    array = reverse_list(current_position, current_position + jump_len, array)
    current_position = np.mod(current_position + jump_len + skip, len(array))
    skip += 1
print("Solution Part 1:", array[0] * array[1])

# Part 2
data = "34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167"
new_data = []
for car in data:
    new_data.append(ord(car))
extra = [17, 31, 73, 47, 23]
for number in extra:
    new_data.append(number)


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


data = new_data
array = list(range(256))
current_position = 0
skip = 0
for i in range(64):
    for jump_len in data:
        # print(array)
        array = reverse_list(current_position, current_position + jump_len, array)
        # print(array)
        current_position = np.mod(current_position + jump_len + skip, len(array))
        # print(current_position)
        skip += 1

print("Solution Part 2:", hex_array(XOR(array)))
