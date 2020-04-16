with open("socdist1.in") as fin:
    n = int(fin.readline())
    org_state = [int(i) for i in fin.readline()]
    print(org_state)


def longest_unoccupied(state):
    longest, curr = [], []
    for i in range(n):
        if state[i] == 1:
            if len(curr) > len(longest):
                longest = curr
            curr = []
        else:
            curr.append(i)
    if len(curr) > len(longest):
        longest = curr
    return longest
print(longest_unoccupied(org_state))

with open("socdist1.out", "w") as fout:
    d = 0
    if org_state[0] == 0 and org_state[-1] == 0:
        temp = org_state[:]
        temp[0] = 1
        temp[-1] = 1
        if len(longest_unoccupied(temp)) > d:

            print(len(longest_unoccupied(temp)))
            print(1)
            d = len(longest_unoccupied(temp))
    if org_state[0] == 0:
        temp = org_state[:]
        temp[0] = 1
        temp[longest_unoccupied(temp)[round(len(longest_unoccupied(temp)) / 2)]] = 1
        if len(longest_unoccupied(temp)) > d:

            print(len(longest_unoccupied(temp)))
            print(2)
            d = len(longest_unoccupied(temp))
    if org_state[-1] == 0:
        temp = org_state[:]
        temp[-1] = 1
        temp[longest_unoccupied(temp)[round(len(longest_unoccupied(temp)) / 2)]] = 1
        if len(longest_unoccupied(temp)) > d:

            print(len(longest_unoccupied(temp)))
            print(3)
            d = len(longest_unoccupied(temp))
    if len(longest_unoccupied(org_state)) >= 2:
        temp = org_state[:]
        temp[longest_unoccupied(temp)[round(len(longest_unoccupied(temp)) / 2)]] = 1
        temp[longest_unoccupied(temp)[round(len(longest_unoccupied(temp)) / 2)]] = 1
        if len(longest_unoccupied(temp)) > d:

            print(len(longest_unoccupied(temp)))
            print(4)
            d = len(longest_unoccupied(temp))
    print(len(longest_unoccupied(org_state)))
    if len(longest_unoccupied(org_state)) >= 3:
        temp = org_state[:]
        x = longest_unoccupied(temp)
        temp[x[len(x) // 3]] = 1
        temp[x[int(len(x) * (2 / 3))]] = 1
        print(len(longest_unoccupied(temp)))
        if len(longest_unoccupied(temp)) > d:
            print(len(longest_unoccupied(temp)))
            print(5)
            d = len(longest_unoccupied(temp))
    fout.write(str(d))
