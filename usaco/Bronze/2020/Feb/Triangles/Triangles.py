from itertools import permutations
with open("triangles.in") as fin:
    n = int(fin.readline())
    cords = [(int(k), int(v)) for (k, v) in [i.split() for i in fin.readlines()]]
    print(cords)

with open("triangles.out", "w") as fout:
    largest = 0
    for x, y, z in permutations(cords, 3):
        if x[0] == y[0] and x[1] == z[1]:
            area = (y[1] - x[1]) * (z[0] - x[0])
            if area < 0:
                area *= -1
            if area > largest:
                largest = area
    fout.write(str(largest))
