highest = 0
for a in reversed(range(100, 1000)):
    for b in reversed(range(100, 1000)):
        if str(a*b)[::-1] == str(a*b):
            if a*b > highest:
                highest = a*b
print(highest)
