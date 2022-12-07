file = open("input.txt").read()

routes = []
tree = dict()

for i in file.split("\n"):
    x = i.split(' ')
    if x[0] == '$':
        reading = False

    if x[0] == '$' and x[1] == 'cd':
        if x[2] == '..':
            routes.pop()
        else:
            routes.append(x[2])
    elif x[0] == '$' and x[1] == 'ls':
        reading = True
        continue

    if reading:
        if x[0] != 'dir':
            actual = ''
            for r in routes:
                actual += r + '/'
                if actual not in tree:
                    tree[actual] = 0
                tree[actual] += int(x[0])

free = 70000000 - tree['//']
tree = {k: v for k, v in sorted(tree.items(), key=lambda item: item[1])}

for k, v in tree.items():
    if (free + v) >= 30000000:
        print(v)
        break
