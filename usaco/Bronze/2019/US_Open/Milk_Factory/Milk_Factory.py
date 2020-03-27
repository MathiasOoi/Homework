with open("factory.in") as fin:
    n = fin.readline()
    to = []
    for line in fin.readlines():
        x = line.split()
        to.append(int(x[0]))
    print(to)


with open("factory.out", "w") as fout:
    x = -1
    b = False
    for i in range(1, int(n)):
        if to.count(i) == 0 and x != -1:
            fout.write("-1")
            b = True
            break
        if to.count(i) == 0:
            x = i
    if not b:
        fout.write(str(x))
