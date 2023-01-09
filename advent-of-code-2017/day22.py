# Part1
infected = set()
for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value == "#":
            infected.add((i, j))
pos = (12, 12)
dire = (-1, 0)


def virus_d(pos, dire):
    dires = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if pos in infected:
        new_dire = dires[(dires.index(dire) + 1) % len(dires)]
        infected.remove(pos)
    else:
        new_dire = dires[(dires.index(dire) - 1) % len(dires)]
        infected.add(pos)
    return new_dire


def virus_move(pos, dire):
    return (pos[0] + dire[0], pos[1] + dire[1])


pos = (12, 12)
dire = (-1, 0)
n = 1
counter = 0
while n < 10000:

    dire = virus_d(pos, dire)
    if pos in infected:
        counter += 1
    pos = virus_move(pos, dire)
    n += 1
print("Solution part 1:", counter)

# Part2
infected = set()
weakened = set()
flagged = set()
for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value == "#":
            infected.add((i, j))
pos = (12, 12)
dire = (-1, 0)


def virus_d(pos, dire):
    dires = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if pos in infected:
        new_dire = dires[(dires.index(dire) + 1) % len(dires)]
        infected.remove(pos)
        flagged.add(pos)
    elif pos in weakened:
        new_dire = dire
        weakened.remove(pos)
        infected.add(pos)
    elif pos in flagged:
        new_dire = dires[(dires.index(dire) + 2) % len(dires)]
        flagged.remove(pos)

    else:
        new_dire = dires[(dires.index(dire) - 1) % len(dires)]
        weakened.add(pos)
    return new_dire


def virus_move(pos, dire):
    return (pos[0] + dire[0], pos[1] + dire[1])


pos = (12, 12)
dire = (-1, 0)
n = 1
counter = 0
while n < 10000000:

    dire = virus_d(pos, dire)
    if pos in infected:
        counter += 1
    pos = virus_move(pos, dire)
    n += 1
print("Solution part 2:", counter)
