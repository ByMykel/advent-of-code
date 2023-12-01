file = open("input.txt").read()

for i in file.split("\n"):
    for j in range(0, len(i) - 4):
        if len(set(i[j:j+4])) == 4:
            print(j+4)
            break