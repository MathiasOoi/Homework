from itertools import combinations
with open("evolution.in") as fin:
    n = fin.readline()
    subpops = [line.split() for line in fin.readlines()]
    print(subpops)
    attributes = []
    has_attribute = []
    for pop in subpops:
        for i in pop[1:]:
            if i in attributes:
                continue
            attributes.append(i)
    print(attributes)
    for i in attributes:
        has = []
        for pop in subpops:
            if i in pop:
               has.append(subpops.index(pop))
        has_attribute.append(has)
    print(has_attribute)
def possibleProper(pair, i):
    def is_intersect(lst1, lst2):
        for i in lst1:
            if i in lst2:
                return True
        return False
    if not pair:
        return True
    pop1 = set(subpops[pair[0]][1:])
    pop2 = set(subpops[pair[1]][1:])
    if pop1.issubset(pop2) or pop2.issubset(pop1):
        return True
    if pop1.intersection(pop2) == set():
        return True
    print(pair)
    print(pop1)
    print(pop2)
    return False




with open("evolution.out", "w") as fout:
    yes = True
    for i in has_attribute:
        for k in combinations(i, 2):
            if possibleProper(k, i):
                continue
            yes = False
            break


#    yes = all(possibleProper(a) for a in pairs)
    fout.write("yes" if yes else "no")