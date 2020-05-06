with open("teleport.in") as fin:
    with open("teleport.out", "w") as fout:
        a, b, x, y = [int(i) for i in fin.readline().split()]
        fout.write(str(min(abs(a-b), abs(a-x) + abs(b-y), abs(a-y) + abs(b - x))))


