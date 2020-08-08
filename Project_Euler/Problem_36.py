print(sum(i for i in range(1000000) if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1]))
