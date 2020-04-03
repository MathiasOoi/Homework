from collections import defaultdict
import time
#time_start = time.time()
with open("conversions.txt") as fin:
    d = defaultdict(dict)
    # Creates dict of dicts
    for i in fin.readlines():
        # Iterate over every conversion and maps unit to dict of another unit to conversion factor
        line = i.split()
        d[line[0]][line[1]] = float(line[2])

with open("requests.txt") as requests:
    r = [line.split() for line in requests]


def dict_reciprocal(dictionary):
    # Adds reciprocal of a given dict of dicts
    for key, d in dictionary.copy().items():
        for value, multiplier in d.items():
            dictionary[value][key] = 1/multiplier


def BFS(dictionary):
    # Uses BFS to find a path
    start = list(dictionary.keys())[0]
    queue = [[start]]
    visited = [start]
    paths = []
    while queue:
        path = queue.pop()
        for next in dictionary[path[-1]]:
            if next in visited:
                continue
            visited.append(next)
            queue.append(path + [next])
        paths.append(path)
    return paths[1:], start


def create_dict(paths, dictionary):
    conversions = defaultdict(dict)
    conversions[paths[0][0]][paths[0][0]] = 1.0
    for path in paths:
        multiplier = 1.0
        for i in range(len(path)-1):
            multiplier /= dictionary[path[i]][path[i+1]]
        conversions[path[0]][path[-1]] = 1/multiplier
        conversions[path[-1]][path[0]] = multiplier
    return conversions



def convert(n, start, end, dictionary, source):
    # Convert from start to end using conversion dictionary from BFS()
    # 3 possible ways
    if source == start:
        multiplier = 1/dictionary[source][end] * float(n)
    elif source == end:
        multiplier = dictionary[source][start]*float(n)
    else:
        multiplier = (1/(dictionary[start][source]*dictionary[source][end]))*float(n)
    return "{} {}".format(round(multiplier, 2), end)


if __name__ == "__main__":
    dict_reciprocal(d)
#    print(d)
    x, source = BFS(d)
#    print(x)
    conversions = create_dict(x, d)
#    print(conversions)
    for n, start, end in r:
        print(convert(n, start, end, conversions, source))
#    end = time.time()
#    print(end-time_start)


