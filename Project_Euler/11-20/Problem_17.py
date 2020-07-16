def cycle(numer, denom):
    digit = None
    decimals=[]
    while digit not in decimals:
        decimals += [digit]
        digit = numer * 10 // denom
        remainder = numer * 10 - digit * denom
        numer = remainder

    return len(decimals) - decimals.index(digit)
print(cycle(1, 7))