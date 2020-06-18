with open("grid.txt") as fin:
    grid = ([[int(k) for k in i.split()] for i in fin])
    print(grid)
    # 20x20

def HorVer(grid):
    output = 0
    for i in range(len(grid)):
        for k in range(len(grid)-4):
            x = 1
            y = 1
            for n in range(k, k+4):
                if not output:
                    print(grid[i][n])
                x *= grid[i][n]
                y *= grid[n][i]
            output = max(x, y, output)
    return output


print(HorVer(grid))
