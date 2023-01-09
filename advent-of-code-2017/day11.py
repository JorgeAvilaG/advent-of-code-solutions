import numpy as np


def lector_direction(car):
    if car == "n":
        return np.array([1, -1, 0])
    elif car == "s":
        return np.array([-1, 1, 0])
    elif car == "ne":
        return np.array([1, 0, -1])
    elif car == "sw":
        return np.array([-1, 0, 1])
    elif car == "nw":
        return np.array([0, 1, -1])
    elif car == "se":
        return np.array([0, -1, 1])


data = input_data.split(",")

# Part 1 and 2
solution = []
position = np.array([0, 0, 0])

for car in data:
    position += lector_direction(car)
    solution.append((abs(position[0]) + abs(position[1]) + abs(position[2])) / 2)

print("Solution Part 1:", solution[-1])
print("Solution Part 2:", max(solution))
