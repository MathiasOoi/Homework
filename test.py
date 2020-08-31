with open("test.txt") as fin:
    k, n = (int(i) for i in fin.readline().split())
    cows = [[int(i) for i in k.split()] for k in fin]
    print(cows)

def pairs(lst):
    l = set()
    for i in range(len(lst)-1):
        for k in range(i, len(lst)-1):
            l.add((lst[i], lst[k]))
    return l

with open("text.txt", "w") as fout:
    consistent_pairs = pairs(cows[0])
    for session in cows[1:]:
        print(session)
        consistent_pairs = consistent_pairs.intersection(pairs(session))
    print(consistent_pairs)
