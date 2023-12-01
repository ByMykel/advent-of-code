file = open("input.txt").read()

for i in file.split("\n"):
    for j in range(0, len(i) - 14):
        if len(set(i[j:j+14])) == 14:
            print(j+14)
            break