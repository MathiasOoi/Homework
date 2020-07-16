with open("grid.txt") as fin:
    grid = ([[int(k) for k in i.split()] for i in fin])
    print(grid)
    # 20x20

def solve():
    highest, temp = 0, 0
    for i in range(20):
        for k in range(20):
            if i < 17:
                temp = grid[i][k] * grid[i + 1][k] * grid[i + 2][k] * grid[i + 3][k]
            if temp > highest:
                highest = temp
            if k < 17:
                temp = grid[i][k] * grid[i][k + 1] * grid[i][k + 2] * grid[i][k + 3]
                if temp > highest:
                    highest = temp
            if i < 17 and k < 17:
                temp = grid[i][k] * grid[i + 1][k + 1] * grid[i + 2][k + 2] * grid[i + 3][k + 3]
                if temp > highest:
                    highest = temp
            if i < 17 and k > 2:
                temp = grid[i][k] * grid[i + 1][k - 1] * grid[i + 2][k - 2] * grid[i + 3][k - 3]
                if temp > highest:
                    highest = temp
    print(highest)

if __name__ == "__main__":
    solve()