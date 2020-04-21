with open("shell.in") as fin:
    n = int(fin.readline())
    guesses, swaps =[], []
    for a, b, g in [i.split() for i in fin.readlines()]:
        swaps.append((int(a) - 1, int(b) - 1))
        guesses.append(int(g) - 1)


def get_score(initial_state):
    score = 0
    for i, swap in enumerate(swaps):
        a, b = swap[0], swap[1]
        temp = initial_state[a]
        initial_state[a] = initial_state[b]
        initial_state[b] = temp
        if initial_state[guesses[i]]:
            score += 1
    return score


with open("shell.out", "w") as fout:
    sit1, sit2, sit3 = [False, True, False], [False, False, True], [True, False, False]
    results = []
    results.append(get_score(sit1))
    results.append(get_score(sit2))
    results.append(get_score(sit3))
    fout.write(str(max(results)))