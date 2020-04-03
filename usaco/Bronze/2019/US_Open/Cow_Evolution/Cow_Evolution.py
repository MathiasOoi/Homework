from collections import defaultdict
import time

#start = time.time()

with open("evolution.in") as fin:
    n = fin.readline()
    # Lists of list of all attributes for every sub-population
    subpops = [line.split()[1:] for line in fin.readlines()]
    attributes = set()
    attrs = defaultdict(set)
    for i in subpops:
        for k in i:
            attributes.add(k)
    # Maps every attribute to a set of sub-populations (index) containing that attribute
    for att in attributes:
        for pop in subpops:
            if att in pop:
                attrs[att].add(subpops.index(pop))
#    print(attrs)
#    print(subpops)
#    print(attributes)


def possibleProper():
    # For each pair of Attributes check if they are
    # 1. One is a subset of another
    # 2. They are disjoint (don't overlap)
    for v1 in attrs.values():
        for v2 in attrs.values():
            if v1 == v2:
                continue
            if v1.issubset(v2) or v2.issubset(v1):
                continue
            if v1.isdisjoint(v2):
                continue
            return False
    return True


with open("evolution.out", "w") as fout:
    fout.write("yes" if possibleProper() else "no")

#end = time.time()
#print(end - start)
