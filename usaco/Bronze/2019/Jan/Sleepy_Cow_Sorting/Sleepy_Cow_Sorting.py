with open("sleepy.in") as fin:
    n = int(fin.readline())
    cows = [int(i) for i in fin.readline().split()]
    print(cows)

with open("sleepy.out", "w") as fout:
    x = n-1
    for i in reversed(range(1, n)):
        print(i)
        if cows[i] > cows[i-1]:
            x -= 1
        else:
            break
    fout.write(str(x))