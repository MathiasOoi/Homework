import random

with open("conversions.txt", "r") as fin:
    conversions = fin.readlines()
    fin.close()
    d = {}
    for i in range(len(conversions)):
        tem = {}
        line = conversions[i].split()
        if line[0] in d.keys():
            d[line[0]].update({line[1]:float(line[2])})
        else:
            tem[line[1]] = float(line[2])
            d[line[0]] = tem


with open("requests.txt", "r") as requests:
    r = []
    for line in requests:
        r.append(line.split())
    requests.close()

"""
ft yard meter cm dm
"""
def dict_reciprocal(dictionary):
    d_copy = dictionary.copy()
    for key, d in d_copy.items():
        temp_dict = {}
        l = list(d.items())
        for i in range(0, len(l)):
            value = l[i][0]
            multiplier = l[i][1]
            temp_dict[key] = 1/multiplier
            if value in dictionary.keys():
                dictionary[value].update(temp_dict)
            else:
                dictionary[value] = temp_dict


def path_correct(path, start, end):
    if path[0] == start and path[-1] == end:
        return True
    return False



def find_path(start, end):
    path = [start]
    multiplier = 1
    while not path_correct(path, start, end):
        if len(d[path[-1]]) == 1:
            next_key = list(d[path[-1]].keys())[0]
            multiplier *= list(d[path[-1]].values())[0]
        else:
            index = random.randint(0, len(d[path[-1]]) - 1)
            next_key = list(d[path[-1]].keys())[index]
            multiplier *= d[path[-1]][next_key]
        path.append(next_key)
    return multiplier

def convert(n, start, end):
    multiplier = find_path(start, end)
    x = float(n) / multiplier
    return "{} {}".format(round(x, 2), end)


dict_reciprocal(d)
print(d)
print(find_path("dm", "ft"))
"""
dm - ft
dm - cm - meters - yards
"""
for i in r:
    print(convert(i[0], i[1], i[2]))



