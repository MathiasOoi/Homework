from itertools import permutations
with open("lineup.in") as fin:
    ordered_cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
    n = int(fin.readline())
    params = []
    for i in range(n):
        line = fin.readline().split()
        params.append([line[0], line[-1]])
    print(params)

def correct(perm):
    for param in params:
        if abs(perm.index(param[0]) - perm.index(param[1])) != 1:
            return False
    return True


with open("lineup.out", "w") as fout:
    permutations = permutations(ordered_cows)
    for perm in permutations:
        if correct(perm):
            for cow in perm:
                fout.write(cow + "\n")
            break


