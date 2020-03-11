conversions = {
    "in": {"in": 1, "ft": 12, "cm": 1 / 2.54, "m": 39.37, "yards": 36},
    "ft": {"ft": 1, "in": 1 / 12, "cm": 1/(12*2.54), "m": 3.281, "yards": 3},
    "cm": {"cm": 1, "in": 2.54, "ft": 2.54*12, "m": 100, "yards": 2.54*36},
    "m": {"m": 1, "in": 1/39.37, "ft": 1/3.281, "cm": 1/100, "yard": 1/1.094},
    "yards": {"yards": 1, "in": 1/36, "ft": 1/3, "cm": 1/2.54*36, "m": 1.094}
}

def convert(value, start, end):
    return '' + str(value*conversions[start][end]) + " " + end


with open("conversions.in", "r") as fin:
    l = fin.read().split()
    fin.close()
    value = []
    start = []
    end = []
    x = 0
    for i in range(len(l)//3):
        value.append(int(l[x]))
        start.append(l[x+1])
        end.append(l[x+2])
        x += 3


for i in range(len(value)):
    print(convert(value[i], start[i], end[i]))
