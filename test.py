dictionary = {1:{2:3, 4:5}}
d_copy = dictionary.copy()
for key, d in d_copy.items():
    temp_dict = {}
    print(list(d.items()))
    x = list(d.items())
    for i in range(0, len(x)):
        print(x[i][0])
        print(x[i][1])


