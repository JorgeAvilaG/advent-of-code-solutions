data = """14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"""
data = list(map(int, data.split()))

import numpy as np


def redistribute(banks):
    maximum = max(banks)

    start = banks.index(maximum)

    new_banks = banks.copy()
    new_banks[start] = 0
    start = np.mod(start + 1, len(new_banks))

    while maximum > 0:
        new_banks[start] += 1
        start = np.mod(start + 1, len(new_banks))
        maximum -= 1

    return new_banks


def list_to_word(list1):
    word = ""
    for number in list1:
        word += str(number)
    return word


# Part1
new_banks = data.copy()
not_bucle = True
seen = set()
str_banks = list_to_word(new_banks)
seen.add(str_banks)
counter = 0
while not_bucle:
    counter += 1
    new_banks = redistribute(new_banks)
    str_banks = list_to_word(new_banks)
    if str_banks in seen:
        not_bucle = False
    else:
        seen.add(str_banks)
print("Solution part 1:", counter)

# Part2
counter1 = counter
solution1 = str_banks

new_banks = data.copy()
not_bucle = True
seen = set()
str_banks = list_to_word(new_banks)
seen.add(str_banks)
counter = 0
while not_bucle:
    counter += 1
    new_banks = redistribute(new_banks)
    str_banks = list_to_word(new_banks)
    if str_banks == solution1:
        not_bucle = False
    else:
        seen.add(str_banks)
print("Solution part 2:", counter1 - counter)
