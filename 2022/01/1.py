file = open("input.txt").read()

out = 0
count = 0

for i in file.split("\n"):
    if i == "":
        out = max(out, count)
        count = 0
    else:
        count += int(i)

print(out)