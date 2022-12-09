def new_tail(head, tail):
    diff = (abs(head[0] - tail[0]), abs(head[1] - tail[1]))
    if diff[0] >= 2 and diff[1] >= 2:
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1,
                head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    elif diff[0] >= 2:
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
    elif diff[1] >= 2:
        tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    return tail


file = open("input.txt").read()

head = (0, 0)
tail = (0, 0)
visited = set()

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

for i in file.split("\n"):
    x = i.split(' ')
    for j in range(int(x[1])):
        head = (head[0] + directions[x[0]][0], head[1] + directions[x[0]][1])
        tail = new_tail(head, tail)
        visited.add(tail)

print(len(visited))
