with open("photo.in") as fin:
    # Parse data
    n = int(fin.readline())
    cows = [int(i) for i in fin.readline().split()]


def photoshoot(i):
    # Return list that satisfies a[i] + a[i+1] = b[i]
    lst = [i]
    for i in cows:
        lst.append(i-lst[-1])
    return lst

with open("photo.out", "w") as fout:
    # Iterate over every number (i) from 1 to n+1
    # Check if photoshoot(i) satisfies
    # 1. Unique (No overlapping elements)
    # 2. All elements in range of 1 to n+1
    for i in range(1, n+1):
        if len(set(photoshoot(i))) == n and set(photoshoot(i)) == set(range(1, n+1)):
            # First list found that satisfies constraints will be lexicographically minimum
            fout.write(" ".join([str(s) for s in photoshoot(i)]))
            break