file = open("input.txt").read()

grid = [[int(char) for char in line] for line in file.split("\n")]
count = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

for x in range(len(grid)):
    highest = -1
    for y in range(len(grid[0])):
        if grid[x][y] > highest:
            count[x][y] += 1
            highest = grid[x][y]

    highest = -1
    for y in range(len(grid[0]) - 1, -1, -1):
        if grid[x][y] > highest:
            count[x][y] += 1
            highest = grid[x][y]

for x in range(len(grid)):
    highest = -1
    for y in range(len(grid[0])):
        if grid[y][x] > highest:
            count[y][x] += 1
            highest = grid[y][x]

    highest = -1
    for y in range(len(grid[0]) - 1, -1, -1):
        if grid[y][x] > highest:
            count[y][x] += 1
            highest = grid[y][x]

ans = sum([sum([1 if i > 0 else 0 for i in j]) for j in count])

print(ans)
