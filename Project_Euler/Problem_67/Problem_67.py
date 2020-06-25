with open("triangle.txt") as fin:
    tree = [[int(i) for i in k.split()] for k in fin]
    for i in tree:
        while len(i) < len(tree[-1]):
            i.append(0)
    print(tree)

def solve(tree):
    n = len(tree[-1])-1
    while n >= 0:
        k = 0
        while k <= len(tree[-1])-2:
            left = tree[n][k] + tree[n-1][k]
            right = tree[n][k+1] + tree[n-1][k]
            if left > right:
                tree[n - 1][k] = left
            else:
                tree[n - 1][k] = right
            k += 1
        n -= 1
    return tree[0][0]

print(solve(tree))