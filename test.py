from itertools import permutations

with open("lineup.in") as fin:
    n = int(fin.readline())
    l = []
    cows = sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"])
    print(cows)
    for line in fin:
        x = line.split()
        l.append([x[0], x[-1]])
    print(l)

def isGood(cows):
    for c in l:
        if abs(cows.index(c[0]) - cows.index(c[1])) != 1:
            return False
    return True

def solve():
    for order in permutations(cows):
        if isGood(order):
            return order

with open("lineup.out", "w") as fout:
    for cow in solve():
        fout.write(cow + "\n")
