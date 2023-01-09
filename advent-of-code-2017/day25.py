# Part 1
ones = set()
pos = 0
state = "A"
n = 1

while n <= 12459852:
    n += 1
    if state == "A":
        if pos in ones:

            pos -= 1
            state = "E"
        else:
            ones.add(pos)
            pos += 1
            state = "B"
    elif state == "B":
        if pos in ones:

            pos += 1
            state = "F"
        else:
            ones.add(pos)
            pos += 1
            state = "C"
    elif state == "C":
        if pos in ones:
            ones.remove(pos)
            pos += 1
            state = "B"
        else:
            ones.add(pos)
            pos -= 1
            state = "D"
    elif state == "D":
        if pos in ones:
            ones.remove(pos)
            pos -= 1
            state = "C"
        else:
            ones.add(pos)
            pos += 1
            state = "E"
    elif state == "E":
        if pos in ones:
            ones.remove(pos)
            pos += 1
            state = "D"
        else:
            ones.add(pos)
            pos -= 1
            state = "A"
    elif state == "F":
        if pos in ones:

            pos += 1
            state = "C"
        else:
            ones.add(pos)
            pos += 1
            state = "A"


print(len(ones))
