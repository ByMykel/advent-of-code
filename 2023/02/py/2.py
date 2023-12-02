import os

file_path = os.path.abspath(os.path.join("2023/02/input.txt"))

with open(file_path, "r") as file:
    content = file.read()

out = 0

for i in content.split("\n"):
    i += ';'
    count = [0, 0, 0]
    count_max = [-1, -1, -1]
    game, cubes = i.split(': ')
    sets = cubes.split(' ')
    for j in range(0, len(sets) - 1, 2):
        sets[j + 1] = sets[j + 1].replace(',', '')
        if ('red' in sets[j + 1]):
            count[0] += int(sets[j])
        if ('green' in sets[j + 1]):
            count[1] += int(sets[j])
        if ('blue' in sets[j + 1]):
            count[2] += int(sets[j])
        if (';' in sets[j + 1]):
            count_max = [max(count[0], count_max[0]), max(count[1], count_max[1]), max(count[2], count_max[2])]
            count = [0, 0, 0]
    out += count_max[0] * count_max[1] * count_max[2]
        
print(out)