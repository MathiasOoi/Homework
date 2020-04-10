from itertools import permutations
with open("photo.in") as fin:
    # Parse data
    n = int(fin.readline())
    cows = [int(i) for i in fin.readline().split()]


def correct(iterable):
    # For every i value in range of 0 to n - 1
    # Check if a[i] + a[i+1] = b[i]
    for i in range(n-1):
        if iterable[i] + iterable[i+1] == cows[i]:
            continue
        return False
    return True

with open("photo.out", "w") as fout:
    # Permutations function returns permutations of an iterable in a lexicographically minimum order
    # So the first permutation which satisfies correct() is the lexicographically minimum permutation
    for perm in permutations(range(1, n+1)):
        if correct(perm):
            fout.write(" ".join([str(i) for i in perm]))
            break