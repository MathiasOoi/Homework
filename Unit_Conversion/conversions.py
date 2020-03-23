from collections import defaultdict

with open("conversions.txt", "r") as fin:
    conversions = fin.readlines()
    d = defaultdict(dict)
    # Creates dict of dicts
    for i in conversions:
        # Iterate over every conversion and maps unit to dict of another unit to conversion factor
        line = i.split()
        d[line[0]] = {line[1]: float(line[2])}

with open("requests.txt", "r") as requests:
    r = [line.split() for line in requests]


def dict_reciprocal(dictionary):
    # Adds reciprocal of a given dict of dicts
    d_copy = dictionary.copy()
    for key, d in d_copy.items():
        for value, multiplier in d.items():
            if value in dictionary.keys():
                dictionary[value].update({key: 1/multiplier})
            else:
                dictionary[value] = {key: 1/multiplier}


def find_path(start, end, dictionary):
    # Uses BFS to find a path
    q = [(start, [start])]
    # Tuple of last vertex visited and path
    while len(q) != 0:
        (v, path) = q.pop(0)
        for next in dictionary[v].keys() - set(path):
            if next == end:
                # Once correct path is discovered return it
                return path + [next]
            else:
                # If the path isn't discovered append visited vertex and path plus vertex
                q.append((next, path + [next]))


def find_multiplier(path, dictionary):
    # Gets path from find_path() and calculates the conversion factor
    multiplier = 1.0
    for i in range(len(path)-1):
        multiplier /= dictionary[path[i]][path[i+1]]
    return multiplier


def convert(n, start, end, dictionary):
    path = find_path(start, end, dictionary)
    multiplier = find_multiplier(path, dictionary) * float(n)
    return "{} {}".format(round(multiplier, 2), end)


if __name__ == "__main__":
    dict_reciprocal(d)
    for n, start, end in r:
        print(convert(n, start, end, d))



