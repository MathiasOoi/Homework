import string
with open("names.txt") as fin:
    names = sorted(fin.read().replace('"', "").split(","))
    d = {char: i + 1 for i, char in enumerate(string.ascii_uppercase)}

def solve():
    total = 0
    for i, name in enumerate(names):
        total += sum(d[char] for char in name) * (i + 1)
    return total

print(solve())