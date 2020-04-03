with open("socdist1.in") as fin:
    n = fin.readline()
    s = fin.readline()
    stalls = [int(x) for x in s]


def longest_unoccupied(lst):
    longest = []
    curr = []
    for i in range(len(lst)):
        if lst[i] == 1:
            curr = []
        if lst[i] == 0:
            curr.append(i)
        if len(longest) == 0:
            longest = curr
        if len(curr) == 0:
            continue
        elif curr[-1] - curr[0] > longest[-1] - longest[0]:
            longest = curr
    return longest


with open("socdist1.out", "w") as fout:
    for i in range(2):
        longest = longest_unoccupied(stalls)
        middle = longest[len(longest)//2]
        stalls[middle] = 1
    fout.write(str(len(longest_unoccupied(stalls))))
