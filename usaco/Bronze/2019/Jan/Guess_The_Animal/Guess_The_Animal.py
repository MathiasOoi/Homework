with open("guess.in") as fin:
    n = int(fin.readline())
    traits = [set(line.split()[2:]) for line in fin]
    print(traits)

def solve():
    x = 0
    for cow1 in traits:
        for cow2 in traits:
            if cow1 != cow2:
                y = len(cow1.intersection(cow2))
                if y > x:
                    x = y
    return str(x + 1)

with open("guess.out", "w") as fout:
    fout.write(solve())
