with open("whereami.in") as fin:
    x = fin.readline()
    n = int(x)
    boxes = fin.readline()


def correct(string, k):
    subStr = set()
    for i in range(len(string) - k):
        if string[i:i+k] in subStr:
            return False
        subStr.add(string[i:i+k])
    return True


with open("whereami.out", "w") as fout:
    for i in range(1, n):
        if correct(boxes, i):
            fout.write(str(i))
            break