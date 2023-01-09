gen_A_0 = 703
gen_B_0 = 516

gen_A = 16807
gen_B = 48271


def generator(number, kind):
    denominator = 2147483647
    return (number * kind) % denominator


# Part1
counter = 0
A = gen_A_0
B = gen_B_0
for x in range(40 * 10 ** 6):
    A = generator(A, gen_A)
    B = generator(B, gen_B)

    if (A & 0xFFFF) == (B & 0xFFFF):
        counter += 1

print("Solution Part 1:", counter)

# Part2
counter = 0
solution = 0
A = gen_A_0
B = gen_B_0

while counter < 5 * 10 ** 6:
    while True:
        A = generator(A, gen_A)
        if A % 4 == 0:
            break
    while True:
        B = generator(B, gen_B)
        if B % 8 == 0:
            break
    counter += 1

    if (A & 0xFFFF) == (B & 0xFFFF):
        solution += 1

print("Solution Part 2:", solution)
