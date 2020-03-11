import random
list = [1, 2, 3, 4, 5]
print(list)
r1 = random.randint(1,5)
r2 = random.randint(1,5)
print(r1)
print(r2)
list[int(r1-1)] = int(r2)
list[int(r2-1)] = int(r1)
print(list)

