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
def path_correct(path, start, end):
    if path[0] == start and path[-1] == end:
        return True
    return False



def find_path(start, end):
    path = [start]
    while not path_correct(path, start, end):
        nextKey = list(d[start].keys())[0]
        path.append(nextKey)
    path.append(end)
    return path


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

