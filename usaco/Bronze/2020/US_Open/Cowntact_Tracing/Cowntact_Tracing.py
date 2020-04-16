from collections import defaultdict
import time

start = time.time()
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1037
# Only passes 15/16 test cases
# Fails one on time
# Time complexity O(NT^2)
with open("tracing.in") as fin:
    n, t = [int(i) for i in fin.readline().split()]
    end_state = [int(i) for i in fin.readline()[:-1]]
    # Create a list of tuples of interactions sorted by time
    interactions = sorted([(int(t), int(x) - 1, int(y) - 1) for (t, x, y) in [s.split() for s in fin.readlines()]],
                          key=lambda x: x[0])


def possible(p0, k):
    # Given patient zero and k
    # Simulate all interactions
    handshakes = defaultdict(int)
    state = [0] * n
    state[p0] = 1
    for interaction in interactions:
        if state[interaction[1]] == 1 and state[interaction[2]] == 1:
            handshakes[interaction[1]] += 1
            handshakes[interaction[2]] += 1
        elif state[interaction[1]] == 1 and handshakes[interaction[1]] < k:
            if state[interaction[2]] == 1:
                handshakes[interaction[2]] += 1
            state[interaction[2]] = 1
            handshakes[interaction[1]] += 1
        elif state[interaction[2]] == 1 and handshakes[interaction[2]] < k:
            if state[interaction[1]] == 1:
                handshakes[interaction[1]] += 1
            state[interaction[1]] = 1
            handshakes[interaction[2]] += 1
    return state == end_state


with open("tracing.out", "w") as fout:
    possible_k, possible_patientZ = set(), set()
    # Iterate through every possible combination of patient zero and k
    for patientZ in range(n):
        # If k > t it's the same as k = t
        # So you only have to iterate over 0 to t
        for k in range(t + 1):
            if possible(patientZ, k):
                possible_k.add(k)
                possible_patientZ.add(patientZ)
    # If k could be t
    # Then k could be any value more than t
    # So the maximum value of k is infinity
    if max(possible_k) == t:
        fout.write(str(len(possible_patientZ)) + " " + str(min(possible_k)) + " " + "Infinity")
    else:
        fout.write(str(len(possible_patientZ)) + " " + str(min(possible_k)) + " " + str(max(possible_k)))
print(time.time() - start)
