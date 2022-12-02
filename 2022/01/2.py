file = open("input.txt").read()

out = []
count = 0

for i in file.split("\n"):
    if i == "":
        out.append(count)
        count = 0
    else:
        count += int(i)

out.append(count)
out.sort(reverse=True)

print(sum(out[:3]))