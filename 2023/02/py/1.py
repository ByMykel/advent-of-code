import os

file_path = os.path.abspath(os.path.join("2023/02/input.txt"))

with open(file_path, "r") as file:
    content = file.read()

out = 0

for i in content.split("\n"):
    i += ';'
    valid_game = True
    count = [0, 0, 0]
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
            if (count[0] > 12 or count[1] > 13 or count[2] > 14):
                valid_game = False
            count = [0, 0, 0]
    if valid_game:
        out += int(game.split(' ')[1])
        
print(out)