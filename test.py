def solve(x, y, a, domain, rang):
    output = []
    for i in domain:
        tempx = x * i
        tempa = a - tempx
        tempa /= y
        output.append(tempa)
    for k in rang:
        tempy = y * k
        tempa = a - tempy
        tempa /= x
        output.append(tempa)
    return output

print(solve(0.5, -2, 1, [1, 6], [0]))

