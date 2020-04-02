import itertools
for i in itertools.permutations([1,2,3], 2):
    print(i)
print("BLOCK")
for i in itertools.combinations([1], 2):
    print(i)