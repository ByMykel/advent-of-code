import re

file = open("input.txt").read()

out = 0
readingStack = True
stack = [[] for i in range(9)]

for i in file.split("\n"):
    if readingStack and '[' in i:
        for j in range(0, len(i), 4):
            if i[j + 1] != ' ':
                stack[j // 4].append(i[j + 1])
        continue
    if (i == "" or '[' not in i) and readingStack:
        for j in range(9):
            stack[j] = stack[j][::-1]
        readingStack = False
        continue

    move = re.findall(r'\d+', i)

    if move == []:
        continue

    items = [stack[int(move[1]) - 1].pop() for j in range(int(move[0]))]
    stack[int(move[2]) - 1].extend(items)

out = ''.join([j[-1] for j in stack])

print(out)
