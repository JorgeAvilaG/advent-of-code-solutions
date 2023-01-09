data1 = [x.split(":") for x in data.split("\n")]
dict_radars = {}
for item in data1:
    dict_radars[int(item[0])] = int(item[1])

import numpy as np

# Part 1
solution = 0
for key in dict_radars:
    number = 2 * dict_radars[key] - 2
    if np.mod(key, number) == 0:
        solution += key * dict_radars[key]
print("Solution Part 1:", solution)

# Part 2
n = 0
caught = True
while caught:
    n += 2
    caught = False
    for key in dict_radars:
        number = 2 * dict_radars[key] - 2
        if np.mod(key + n, number) == 0:
            caught = True
            break


print("Solution Part 2:", n)
