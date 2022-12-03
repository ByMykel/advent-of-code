file = open("input.txt").read()

out = 0
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
seen = dict()

for i in file.split("\n"):
    if count == 3:
        count = 0
        seen = dict()

    if count == 0:
        for letter in i:
            if letter not in seen:
                seen[letter] = 1

    if count == 1:
        for letter in i:
            if letter in seen:
                seen[letter] = 2

    if count == 2:
        for letter in i:
            if letter in seen and seen[letter] == 2:
                seen[letter] = 3
        for letter in seen:
            if seen[letter] == 3:
                out += alpha.index(letter) + 1
    count += 1

print(out)