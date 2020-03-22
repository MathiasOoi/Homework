import random
from collections import defaultdict

with open("conversions.txt", "r") as fin:
    conversions = fin.readlines()
    d = defaultdict(dict)
    # Creates dict of dicts
    for i in conversions:
        # Iterate over every conversion and maps unit to dict of another unit to conversion factor
        line = i.split()
        d[line[0]] = {line[1]: float(line[2])}
    print(d)

with open("requests.txt", "r") as requests:
    r = []
    for line in requests:
        r.append(line.split())


def dict_reciprocal(dictionary):
    # Adds reciprocal of a given dict of dicts
    d_copy = dictionary.copy()
    for key, d in d_copy.items():
        for value, multiplier in d.items():
            if value in dictionary.keys():
                dictionary[value].update({key: 1/multiplier})
            else:
                dictionary[value] = {key: 1/multiplier}


def path_correct(path, end):
    if path[-1] == end:
        return True
    return False


def find_path(start, end):
    path = [start]
    multiplier = 1
    while not path_correct(path, end):
        index = random.randint(0, len(d[path[-1]]) - 1)
        next_key = list(d[path[-1]].keys())[index]
        multiplier *= d[path[-1]][next_key]
        path.append(next_key)
    return multiplier


def convert(n, start, end):
    multiplier = find_path(start, end)
    x = float(n) / multiplier
    return "{} {}".format(round(x, 2), end)


if __name__ == "__main__":
    dict_reciprocal(d)
    for i in r:
        print(convert(i[0], i[1], i[2]))



