with open("triangle.txt") as fin:
    tree = [[int(i) for i in k.split()] for k in fin]
    print(tree)

def solveBruteForce(total = 0, depth = 0, index = 0):
    pass