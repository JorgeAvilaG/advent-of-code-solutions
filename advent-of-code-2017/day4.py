input_data_2 = input_data.split("\n")
data = []
for row in input_data_2:
    data.append(row.split())

# Part 1
counter = 0

for row in data:
    good_passphrase = True
    seen = set()
    for word in row:
        if word in seen:
            good_passphrase = False
        else:
            seen.add(word)
    if good_passphrase:
        counter += 1
print("Solution part 1:", counter)

# Part 2
counter = 0


def is_anagram(word1, word2):
    temp1 = list(word1)
    temp2 = list(word2)
    if not len(temp1) == len(temp2):
        return False
    for car in temp1:
        if car in temp2:
            temp2.pop(temp2.index(car))
        else:
            return False
    return True


for row in data:
    good_passphrase = True
    seen = set()
    for word in row:
        for word2 in seen:
            if is_anagram(word, word2):

                good_passphrase = False

        seen.add(word)
    if good_passphrase:
        counter += 1
print("Solution part 2:", counter)
