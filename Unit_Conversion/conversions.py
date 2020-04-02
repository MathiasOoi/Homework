from collections import defaultdict
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


def find_path(start, end, dictionary):
    # Uses BFS to find a path
    # Initialize queue with start inside
    q = [[start]]
    while q:
        # Get and remove oldest path in queue
        path = q.pop(0)
        # If the path is correct return it
        if path[-1] == end:
            return path
        for next in list(dictionary[path[-1]].keys()):
            if next not in path:
                q.append(path+[next])



def find_multiplier(path, dictionary):
    # Calculate conversion factor given path and dict
    multiplier = 1.0
    for i in range(len(path)-1):
            multiplier /= dictionary[path[i]][path[i+1]]
    return multiplier


def convert(n, start, end, dictionary, source):
    # Convert from start to end using conversion dictionary from create_conversions()
    # 3 possible ways
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
    other_keys = list(dictionary.keys())[1:]
    # Create the dict and the reciprocals
    for end in other_keys:
        conversions[source][end] = 1/find_multiplier(find_path(source, end, dictionary), dictionary)
        conversions[end][source] = find_multiplier(find_path(source, end, dictionary), dictionary)
    # Return tuple of created dict and source
    return conversions, source


if __name__ == "__main__":
    dict_reciprocal(d)
    conversions, source = create_conversions(d)
    for n, start, end in r:
        print(convert(n, start, end, conversions, source))



