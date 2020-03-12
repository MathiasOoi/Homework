with open("conversions.txt", "r") as fin:
    conversions = fin.readlines()
    fin.close()
    d = {}
    for i in range(len(conversions)):
        tem = {}
        line = conversions[i].split()
        tem[line[1]] = int(line[2])
        d[line[0]] = tem


with open("requests.txt", "r") as requests:
    r = []
    for line in requests:
        r.append(line.split())
    requests.close()


def solve(value, start, end):
    if start in d.keys() and end in d.keys():
        if start in d[end].keys():
            return str(value*d[end][start]) + " " + end
        elif end in d[start].keys():
            return str(value/d[start][end]) + " " + end
    elif start in d.keys():
        if end in d[list(d[start].keys())[0]].keys():
            return str(value/d[list(d[start].keys())[0]][end]/d[start][list(d[start].keys())[0]]) + " " + end
    elif start in d[list(d[end].keys())[0]].keys():
        return str(value*d[list(d[end].keys())[0]][start]*d[end][list(d[end].keys())[0]]) + " " + end


for i in r:
    print(solve(int(i[0]), i[1], i[2]))

