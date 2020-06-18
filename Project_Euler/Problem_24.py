from itertools import permutations
for i, k in enumerate(permutations("0123456789")):
    if i+1 == 1000000:
        print("".join(k))
        break