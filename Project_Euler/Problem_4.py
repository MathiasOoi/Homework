lst = []
for a in reversed(range(100, 1000)):
    for b in reversed(range(100, 1000)):
        if str(a*b)[::-1] == str(a*b):
            lst.append(a*b)
print(max(lst))
