# Part 1 and 2
groups = 0
garbage = False
ignore_next = False
characters = 0
score = 0

for n in data:
    if n == "!" and not ignore_next:
        ignore_next = True
    elif n == "<" and not garbage and not ignore_next:
        garbage = True
    elif n == ">" and not ignore_next:
        garbage = False
    elif n == "{" and not garbage and not ignore_next:
        groups += 1
    elif n == "}" and not garbage and not ignore_next:
        score += groups
        groups -= 1
    elif garbage and not ignore_next:
        characters += 1
    elif ignore_next:
        ignore_next = False


print("Solution Part 1:", score)
print("Solution Part 2:", characters)
