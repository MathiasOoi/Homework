with open("breedflip.in") as fin:
    n = int(fin.readline())
    A, B = [list(i) for i in fin.readlines()]


def solve():
    # Find the list of substrings that need to be flipped
    # Return the length of the list
    lst = []
    curr = []
    for i in range(n):
        if B[i] == A[i]:
            if curr:
                lst.append(curr)
            curr = []
        else:
            curr.append(i)
    return str(len(lst))

with open("breedflip.out", "w") as fout:
    fout.write(solve())