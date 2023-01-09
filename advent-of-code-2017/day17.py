# Part1
p_input = 382
circular_list = [0]
position = 0

for x in range(1, 2018):
    position = (position + p_input) % len(circular_list)
    circular_list.insert(position + 1, x)
    position += 1

print("Solution Part 1:", circular_list[position + 1])

# Part2
p_input = 382
position = 0
solution = 0

for x in range(1, 50000000):
    position = (position + p_input) % x
    if position == 0:
        solution = x
    position += 1

print("Solution Part 2:", solution)
