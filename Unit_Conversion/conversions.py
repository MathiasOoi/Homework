with open("conversions.txt", "r") as fin:
    conversions = fin.readlines()
    fin.close()
    d = {}
    for i in range(len(conversions)):
        tem = {}
        line = conversions[i].split()
        tem[line[1]] = int(line[2])
        d[line[0]] = tem

with open(requests.txt)
