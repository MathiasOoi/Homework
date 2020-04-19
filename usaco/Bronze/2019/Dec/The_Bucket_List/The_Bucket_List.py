# http://www.usaco.org/index.php?page=viewproblem2&cpid=856
# Algorithmic Complexity O(N Log N) because you need to sort the list
with open("blist.in") as fin:
    # Create list of tuples (start-time, end-time, buckets) sorted by time
    n = int(fin.readline())
    cows = sorted([(int(s), int(t), int(b)) for (s, t, b) in [i.split() for i in fin.readlines()]], key=lambda x: x[0])
    print(cows)

with open("blist.out", "w") as fout:
    buckets = 0
    still_milking = []
    for time in range(1, max([i[1] for i in cows])):
        for i, k in enumerate(still_milking):
            if time == k[1]:
                still_milking.pop(i)
        if still_milking:
            avail = buckets - sum(i[2] for i in still_milking)
        if not still_milking:
            avail = buckets
        if cows:
            if time == cows[0][0]:
                if cows[0][2] > avail:
                    buckets = buckets - avail + cows[0][2]
                still_milking.append(cows.pop(0))
    fout.write(str(buckets))



