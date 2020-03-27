with open("buckets.in") as fin:
    rows = fin.readlines()
    rows.reverse()
    for y in range(len(rows)):
        for x in range(len(rows)):
            if rows[y][x] == "B":
                barn_cords = (x, y)
            if rows[y][x] == "L":
                lake_cords = (x, y)
            if rows[y][x] == "R":
                rock_cords = (x, y)


with open("buckets.out", "w") as fout:
    if rock_cords[1] == barn_cords[1] and rock_cords[1] == lake_cords[1]:
        if rock_cords[0] in range(min(barn_cords[0], lake_cords[0]), max(barn_cords[0], lake_cords[0])):
            fout.write(str(abs(barn_cords[0] - lake_cords[0]) + abs(barn_cords[1] - lake_cords[1]) + 1))
        else:
            fout.write(str(abs(barn_cords[0] - lake_cords[0]) + abs(barn_cords[1] - lake_cords[1]) - 1))
    elif rock_cords[0] == barn_cords[0] and rock_cords[0] == lake_cords[0]:
        if rock_cords[1] in range(min(barn_cords[1], lake_cords[1]), max(barn_cords[1], lake_cords[1])):
            fout.write(str(abs(barn_cords[0] - lake_cords[0]) + abs(barn_cords[1] - lake_cords[1]) + 1))
        else:
            fout.write(str(abs(barn_cords[0] - lake_cords[0]) + abs(barn_cords[1] - lake_cords[1]) - 1))
    else:
        fout.write(str(abs(barn_cords[0] - lake_cords[0]) + abs(barn_cords[1] - lake_cords[1]) - 1))
