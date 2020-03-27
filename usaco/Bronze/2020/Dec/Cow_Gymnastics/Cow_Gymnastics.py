with open("gymnastics.in") as fin:
    k, n = fin.readline().split()
    lines = [line.split() for line in fin.readlines()]


def pairs(lst):
    l = []
    for i in range(len(lst) - 1):
        for x in range(i+1, len(lst)):
            l.append([lst[i], lst[x]])
    return l


with open("gymnastics.out", "w") as fout:
    l = pairs(lines[0])
    for i in range(1,int(k)):
        l = [x for x in l if x in pairs(lines[i])]
    fout.write(str(len(l)))


