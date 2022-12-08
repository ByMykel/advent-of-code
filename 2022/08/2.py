file = open("input.txt").read()

grid = [[int(char) for char in line] for line in file.split("\n")]
count = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]

for x in range(len(grid)):
    for y in range(len(grid[0])):
        score = 1
        tree = 0
        for i in range(x + 1, len(grid)):
            tree += 1
            if grid[i][y] >= grid[x][y]:
                break

        score *= tree
        tree = 0
        for i in range(x - 1, -1, -1):
            tree += 1
            if grid[i][y] >= grid[x][y]:
                break

        score *= tree
        tree = 0
        for i in range(y + 1, len(grid[0])):
            tree += 1
            if grid[x][i] >= grid[x][y]:
                break

        score *= tree
        tree = 0
        for i in range(y - 1, -1, -1):
            tree += 1
            if grid[x][i] >= grid[x][y]:
                break

        score *= tree
        count[x][y] = score

ans = max([max(i) for i in count])

print(ans)
