import numpy as np

pos = []
vel = []
ace = []
for line in data:
    temp = line.split(", ")
    numbers = [int(number) for number in temp[0][3:-1].split(",")]
    pos.append(np.array(numbers))
    numbers = [int(number) for number in temp[1][3:-1].split(",")]
    vel.append(np.array(numbers))
    numbers = [int(number) for number in temp[2][3:-1].split(",")]
    ace.append(np.array(numbers))

# Part1
def dist(item):
    return abs(item[0]) + abs(item[1]) + abs(item[2])


solution = 1000000
particle = []
for index, item in enumerate(ace):
    distance = dist(item)

    if distance < solution:
        solution = distance
        particle = [index]
    elif distance == solution:
        particle.append(index)

solution = 1000000
particle2 = 0
for index in particle:
    distance = dist(vel[index])

    if distance < solution:
        solution = distance
        particle2 = [index]
    elif distance == solution:
        particle2.append(index)

if len(particle2) == 1:
    print("Solution Part 1:", particle2[0])

# Part 2

i = 0
while i < 40:
    for x in range(len(pos)):
        vel[x] += ace[x]
        pos[x] += vel[x]
    new_pos = []
    new_vel = []
    new_ace = []
    temp = [str(line) for line in pos]
    for x in range(len(temp)):
        if temp.count(temp[x]) == 1:
            new_pos.append(pos[x])
            new_vel.append(vel[x])
            new_ace.append(ace[x])
    pos = new_pos
    vel = new_vel
    ace = new_ace
    i += 1
print("Solution Part 2:", len(pos))
