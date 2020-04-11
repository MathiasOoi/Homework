with open('swap.in') as fin:
    n, k = [int(x) for x in fin.readline().split()]
    swaps = [(int(x), int(y)) for (x, y) in [i.split() for i in fin.readlines()]]
    print(swaps)
    cows = list(range(1, n + 1))
    print(cows)


def swap(tup, curr_cow):
    lst = []
    for i in range(tup[0] - 1):
        lst.append(curr_cow[i])
    for i in reversed(range(tup[0] - 1, tup[1])):
        lst.append(curr_cow[i])
    for i in range(tup[1], n):
        lst.append(curr_cow[i])
    return lst


with open("swap.out", "w") as fout:
    for i in range(k):
        cows = swap(swaps[0], cows)
        cows = swap(swaps[1], cows)
    fout.write("\n".join([str(i) for i in cows]))
