file = open("input.txt").read()

out = 0
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
seenFirst = dict()
seenSecond = dict()

for i in file.split("\n"):
    first = i[:len(i)//2]
    second = i[len(i)//2:]

    for j in first:
        if j not in seenFirst:
            seenFirst[j] = 1

    for j in second:
        if j in seenFirst and j not in seenSecond:
            print(first, second, j)
            out += alpha.index(j) + 1
            seenSecond[j] = 1

    seenFirst = dict()
    seenSecond = dict()
        
print(out)