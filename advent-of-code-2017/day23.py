def sets(X, Y, register):
    if Y in register:
        register[X] = register[Y]
    else:
        register[X] = int(Y)


def decrease(X, Y, register):
    if Y in register:
        register[X] -= register[Y]
    else:
        register[X] -= int(Y)


def multiply(X, Y, register):
    if Y in register:
        register[X] *= register[Y]
    else:
        register[X] *= int(Y)


def jump(X, Y, register):
    if X in register:
        if register[X] != 0:
            if Y in register:
                register["pos"] += register[Y] - 1
            else:
                register["pos"] += int(Y) - 1
    else:
        if int(X) != 0:
            if Y in register:
                register["pos"] += register[Y] - 1
            else:
                register["pos"] += int(Y) - 1


functions = {}
functions["set"] = sets
functions["sub"] = decrease
functions["mul"] = multiply
functions["jnz"] = jump


# part 1
registers = {
    "ID": 0,
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "pos": 0,
}
counter = 0
while True:
    pos = registers["pos"]
    if len(data[pos]) == 2:
        functions[data[pos][0]](data[pos][1], register)
    elif len(data[pos]) == 3:
        functions[data[pos][0]](data[pos][1], data[pos][2], registers)
    registers["pos"] += 1

    if data[pos][0] == "mul":
        counter += 1

print("Solution part 1:", counter)

# Part2
# Find NON prime number between 'b' and 'c'
# Step is 17 from last instruction
import numpy as np
import math

counter = 0

n = registers["b"]
while n <= registers["c"]:
    isPrime = True
    for num in range(2, int(math.sqrt(n) + 1)):
        if n % num == 0:
            isPrime = False
    if not isPrime:
        counter += 1
    n += 17
print("Solution part 2:", counter)
