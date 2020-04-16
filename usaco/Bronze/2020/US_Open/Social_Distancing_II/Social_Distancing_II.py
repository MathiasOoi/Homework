import time

start = time.time()
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1036
with open("socdist2.in") as fin:
    n = int(fin.readline())
    # Create a list of sorted tuples
    cows = sorted([(int(i), int(k)) for (i, k) in [x.split() for x in fin.readlines()]])
    healthy, infected, clusters, curr = [], [], [], []
    # Create a list of indexes of healthy and infected cows
    # Create a list of list of infected cows separated by healthy cows
    for cow in cows:
        if cow[1] == 1:
            infected.append(cow[0])
            curr.append(cow[0])
        else:
            healthy.append(cow[0])
            if curr:
                clusters.append(curr)
                curr = []
    if curr:
        clusters.append(curr)


def find_r():
    # Find r by finding the smallest difference between the location of healthy and infected cows
    differences = set()
    for a in infected:
        for b in healthy:
            differences.add(abs(a - b))
    return min(differences)


def solve():
    count, r = 0, find_r()
    # Find a continuous chains of sick cows separated that are at most r apart
    for cluster in clusters:
        count += 1
        curr = cluster[0]
        for i in cluster[1:]:
            if i not in range(curr, curr + r):
                count += 1
            curr = i
    return count


with open("socdist2.out", "w") as fout:
    fout.write(str(solve()))
    print(time.time() - start)
