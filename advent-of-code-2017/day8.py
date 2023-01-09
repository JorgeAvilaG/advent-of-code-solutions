data_initial = input_data.split("\n")


def change_value(value, function, amount):
    if function == "inc":
        if value in registers:
            registers[value] += int(amount)
        else:
            registers[value] = int(amount)
    if function == "dec":
        if value in registers:
            registers[value] -= int(amount)
        else:
            registers[value] = -1 * (int(amount))


def check_condition(value, function, amount):
    if value in registers:
        value_amount = registers[value]
    else:
        registers[value] = 0
        value_amount = registers[value]
    if function == "==":
        if value_amount == int(amount):
            return True
        else:
            return False
    if function == "!=":
        if value_amount != int(amount):
            return True
        else:
            return False
    if function == ">":
        if value_amount > int(amount):
            return True
        else:
            return False
    if function == "<":
        if value_amount < int(amount):
            return True
        else:
            return False
    if function == ">=":
        if value_amount >= int(amount):
            return True
        else:
            return False
    if function == "<=":
        if value_amount <= int(amount):
            return True
        else:
            return False


# Part 1
registers = {}
data2 = data_initial.copy()
for line in data2:
    data = line.split()
    if check_condition(data[4], data[5], data[6]):
        change_value(data[0], data[1], data[2])

max_value = 0
for key in registers:
    if registers[key] > max_value:
        max_value = registers[key]
print("Solution part 1:", max_value)

# Part 2
registers = {}
max_value = 0
data2 = data_initial.copy()
for line in data2:
    data = line.split()
    if check_condition(data[4], data[5], data[6]):
        change_value(data[0], data[1], data[2])
        if registers[data[0]] > max_value:
            max_value = registers[data[0]]
print("Solution part 2:", max_value)
