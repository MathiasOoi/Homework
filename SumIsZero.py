def SumIsZero(lst):
    x = [[]]
    for i in lst:
        x.extend([k + [i] for k in x])
    x = x[1:]
    print(x)
    for i in x:
        if sum(i) == 0:
            return True
    return False


print(SumIsZero([-1,1,2,3,3,4,4,5]))