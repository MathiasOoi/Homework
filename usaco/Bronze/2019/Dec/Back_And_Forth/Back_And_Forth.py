# http://www.usaco.org/index.php?page=viewproblem2&cpid=857
with open("backforth.in") as fin:
    Buc1 = [int(i) for i in fin.readline().split()]
    Buc2 = [int(i) for i in fin.readline().split()]
    Barn1 = 1000


def tue(barn, buc1, buc2):
    for i in buc1:
        nextBuc2 = buc2[:]
        nextBuc2.append(i)
        nextBuc1 = buc1[:]
        nextBuc1.remove(i)
        wed(barn - i, nextBuc1, nextBuc2)


def wed(barn, buc1, buc2):
    for i in buc2:
        nextBuc2 = buc2[:]
        nextBuc2.remove(i)
        nextBuc1 = buc1[:]
        nextBuc1.append(i)
        thur(barn + i, nextBuc1, nextBuc2)


def thur(barn, buc1, buc2):
    for i in buc1:
        nextBuc2 = buc2[:]
        nextBuc2.append(i)
        nextBuc1 = buc1[:]
        nextBuc1.remove(i)
        fri(barn - i, nextBuc2)


def fri(barn, buc2):
    for i in buc2:
        results.add(barn + i)


with open("backforth.out", "w") as fout:
    results = set()
    results.add(Barn1)
    # Simulate everyday Mon - Tue - Wen - Thu - Fri
    # Add all possible results to set
    tue(Barn1, Buc1, Buc2)
    fout.write(str(len(results)))