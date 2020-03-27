with open("photo.in", "r") as fin:
    n = int(fin.readline())
    k = fin.readline().split()
    for i in range(len(k)):
        k[i] = int(k[i])
    fin.close()


print(n)
print(k)