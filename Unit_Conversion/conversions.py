from collections import defaultdict

with open("conversions.txt", "r") as fin:
    d = defaultdict(dict)
    # Creates dict of dicts
    for i in fin.readlines():
        # Iterate over every conversion and maps unit to dict of another unit to conversion factor
        line = i.split()
        d[line[0]][line[1]] = float(line[2])

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


def convert(n, start, end, dictionary, source):
    if source == start:
        multiplier = 1/dictionary[source][end] * float(n)
    elif source == end:
        multiplier = dictionary[source][start]*float(n)
    else:
        multiplier = (1/(dictionary[start][source]*dictionary[source][end]))*float(n)
    return "{} {}".format(round(multiplier, 2), end)


def create_conversions(dictionary):
    # Creates a dict that maps one unit to all other units and the reciprocal
    # Takes the first key in dict as source
    source = list(dictionary.keys())[0]
    conversions = defaultdict(dict)
    ends = set()
    # Iterate over all units
    # Adds all other units to a set
    for key in dictionary.keys():
        ends.add(key)
        for x in dictionary[key].keys():
            ends.add(x)
    # Remove source from the set
    ends.remove(source)
    # Create the dict and the reciprocals
    for end in ends:
        conversions[source][end] = 1/find_multiplier(find_path(source, end, dictionary), dictionary)
        conversions[end][source] = find_multiplier(find_path(source, end, dictionary), dictionary)
    # Return created dict and source
    return conversions , source


if __name__ == "__main__":
    dict_reciprocal(d)
    conversions, source = create_conversions(d)
    print(r)
    print(conversions)
    print(convert(1, "dm", "cm", conversions, "in"))
#    for n, start, end in r:
#        print(convert(n, start, end, conversions, source))



