n, lst = 0, []
while True:
    cube = sorted((str(n**3)))
    lst.append(cube)
    if lst.count(cube) == 5:
        print(lst.index(cube)**3)
        break
    n += 1
