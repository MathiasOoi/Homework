from itertools import permutations
with open("evolution.in") as fin:
    n = fin.readline()
    subpops = [line.split() for line in fin.readlines()]
    traits = set()
    for subpop in subpops:
        if len(subpop) == 2:
            traits.add(subpop[1])

def possibleProper(lst1, lst2):
    if lst1[0] == 0 or lst2[0] == 0:
        return True
    set1 = set(lst1[1:])
    set2 = set(lst2[1:])
    set1 -= traits
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    if set1.intersection(set2) == set():
        return True
    return False


with open("evolution.out", "w") as fout:
    pairs = permutations(subpops, 2)
    yes = all(possibleProper(a,b) for (a,b) in pairs)
    fout.write("yes" if yes else "no")