from collections import defaultdict
import time

start = time.time()

with open("evolution.in") as fin:
    n = fin.readline()
    subpops = [line.split() for line in fin.readlines()]
    attributes = set()
    attrs = defaultdict(set)
    for i in subpops:
        for k in i[1:]:
            attributes.add(k)
    for att in attributes:
        for pop in subpops:
            if att in pop:
                attrs[att].add(subpops.index(pop))
    print(attrs)
    print(subpops)
    print(attributes)


def possibleProper():
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

end = time.time()
print(end - start)
