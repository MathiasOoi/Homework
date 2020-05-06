with open("herding.in") as fin:
    cows = sorted([int(i) for i in fin.readline().split()])

with open("herding.out", "w") as fout:
    if cows[1] - cows[0] == 1 and cows[2] - cows[1] == 1:
        fout.write("0\n")
    elif cows[1] - cows[0] == 2 or cows[2] - cows[1] == 2:
        fout.write("1\n")
    else:
        fout.write("2\n")
    fout.write(str(max(cows[2] - cows[1], cows[1] - cows[0]) - 1))