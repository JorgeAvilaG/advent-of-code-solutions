# part1
def sound(X):
    registers["frequency"] = registers[X]


def sets(X, Y):
    if Y in registers:
        registers[X] = registers[Y]
    else:
        registers[X] = int(Y)


def increase(X, Y):
    if Y in registers:
        registers[X] += registers[Y]
    else:
        registers[X] += int(Y)


def multiply(X, Y):
    if Y in registers:
        registers[X] *= registers[Y]
    else:
        registers[X] *= int(Y)


def modulo(X, Y):
    if Y in registers:
        registers[X] = registers[X] % registers[Y]
    else:
        registers[X] = registers[X] % int(Y)


def recover(X):
    if registers[X] != 0:
        registers["recover"] = registers["frequency"]


def jump(X, Y):
    if X in registers:
        if registers[X] > 0:
            if Y in registers:
                registers["pos"] += registers[Y] - 1
            else:
                registers["pos"] += int(Y) - 1
    else:
        if int(X) > 0:
            if Y in registers:
                registers["pos"] += registers[Y] - 1
            else:
                registers["pos"] += int(Y) - 1


functions = {}
functions["snd"] = sound
functions["set"] = sets
functions["add"] = increase
functions["mul"] = multiply
functions["mod"] = modulo
functions["rcv"] = recover
functions["jgz"] = jump

registers = {}
for line in data:
    registers[line[1]] = 0
del registers["1"]
registers["pos"] = 0
while True:
    pos = registers["pos"]
    if len(data[pos]) == 2:
        functions[data[pos][0]](data[pos][1])
    elif len(data[pos]) == 3:
        functions[data[pos][0]](data[pos][1], data[pos][2])
    registers["pos"] += 1
    if "recover" in registers:
        print("Solution Part 1:", registers["recover"])
        break
        
# part2
def send(X, register):
    if register["ID"] == 0:
        register_1["queue"].append(register[X])
    else:
        register_0["queue"].append(register[X])
    return True


def sets(X, Y, register):
    if Y in register:
        register[X] = register[Y]
    else:
        register[X] = int(Y)


def increase(X, Y, register):
    if Y in register:
        register[X] += register[Y]
    else:
        register[X] += int(Y)


def multiply(X, Y, register):
    if Y in register:
        register[X] *= register[Y]
    else:
        register[X] *= int(Y)


def modulo(X, Y, register):
    if Y in register:
        register[X] = register[X] % register[Y]
    else:
        register[X] = register[X] % int(Y)


def receive(X, register):
    if len(register["queue"]) > 0:
        register[X] = register["queue"].pop(0)
        return True
    else:
        return False


def jump(X, Y, register):
    if X in register:
        if register[X] > 0:
            if Y in register:
                register["pos"] += register[Y] - 1
            else:
                register["pos"] += int(Y) - 1
    else:
        if int(X) > 0:
            if Y in register:
                register["pos"] += register[Y] - 1
            else:
                register["pos"] += int(Y) - 1


functions = {}
functions["snd"] = send
functions["set"] = sets
functions["add"] = increase
functions["mul"] = multiply
functions["mod"] = modulo
functions["rcv"] = receive
functions["jgz"] = jump

register_0 = {"ID": 0, "i": 0, "a": 0, "p": 0, "b": 0, "f": 0, "pos": 0, "queue": []}
register_1 = {"ID": 1, "i": 0, "a": 0, "p": 1, "b": 0, "f": 0, "pos": 0, "queue": []}

counter = 0
while True:
    while True:
        pos = register_0["pos"]

        if len(data[pos]) == 2:
            cont = functions[data[pos][0]](data[pos][1], register_0)
            if not cont:
                break
            else:
                register_0["pos"] += 1
        elif len(data[pos]) == 3:
            functions[data[pos][0]](data[pos][1], data[pos][2], register_0)
            register_0["pos"] += 1

    while True:
        pos = register_1["pos"]
        if len(data[pos]) == 2:
            cont = functions[data[pos][0]](data[pos][1], register_1)
            if data[pos][0] == "snd":
                counter += 1
            if not cont:
                break
            else:
                register_1["pos"] += 1
        elif len(data[pos]) == 3:
            functions[data[pos][0]](data[pos][1], data[pos][2], register_1)
            register_1["pos"] += 1

    if len(register_0["queue"]) == 0 and len(register_1["queue"]) == 0:
        print("Solution Part 2:", counter)
        break
