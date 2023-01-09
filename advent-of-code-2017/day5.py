data = list(map(int, input_data.split("\n")))

# Part 1
instructions = data.copy()
len_inst = len(instructions)
n = 0
counter = 0
while n < len_inst:
    counter += 1
    action = instructions[n]
    instructions[n] += 1
    n += action
print("Solution part 1:", counter)


# Part 2
instructions = data.copy()
len_inst = len(instructions)
n = 0
counter = 0
while n < len_inst:
    counter += 1
    action = instructions[n]
    if action >= 3:
        instructions[n] -= 1
    else:
        instructions[n] += 1
    n += action
print("Solution part 2:", counter)
