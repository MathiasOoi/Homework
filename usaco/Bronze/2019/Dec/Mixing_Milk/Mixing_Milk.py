with open("mixmilk.in") as fin:
    lst = [int(i) for k in [s.split() for s in fin.readlines()] for i in k]
    Bucket1, Bucket2, Bucket3 = lst[:2], lst[2:4], lst[4:]

def pour(B1, B2):
    poured = min(B1[1], B2[0] - B2[1])
    B1[1] -= poured
    B2[1] += poured
with open("mixmilk.out", "w") as fout:
    for i in range(100//3):
        pour(Bucket1, Bucket2)
        pour(Bucket2, Bucket3)
        pour(Bucket3, Bucket1)
    pour(Bucket1, Bucket2)
    fout.write(str(Bucket1[1]) + "\n")
    fout.write(str(Bucket2[1]) + "\n")
    fout.write(str(Bucket3[1]) + "\n")





