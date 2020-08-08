total = 0
for i in range(2, 1000000):
    if sum(int(digit)**5 for digit in str(i)) == i:
        total += i

print(total)