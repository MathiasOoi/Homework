odd = [i for i in range(1001**2 + 1) if i % 2]
i = 0
distance_between_numbers = 1
total = 1
while odd[i] != 1001**2:
    for k in range(4):
        i += distance_between_numbers
        total += odd[i]
    distance_between_numbers += 1
print(total)
