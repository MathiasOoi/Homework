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
        for value, multiplier in d.items():
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
            index = random.randint(1, len(len(d[path[-1]])))
            next_key = list(d[path[-1]].keys())[index]
            multiplier *= list(d[path[-1]].values())[index]
        path.append(next_key)
    return path, multiplier


dict_reciprocal(d)
print(d)
path = ["dm"]
multiplier = 1
next_key = list(d[path[-1]].keys())[0]
print(next_key)
multiplier *= list(d[path[-1]].values())[0]
print(multiplier)
"""
dm - ft
dm - cm - meters - yards
"""
"""
ft dm
ft - yard
yard - meter
meter - cm
cm - dm
"""
#for i in r:
    #print(solve(int(i[0]), i[1], i[2]))

