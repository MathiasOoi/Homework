def SumIsZero(lst):
    x = [[]]
    # Create a list of lists of all possible sub-sets
    for i in lst:
        x.extend([k + [i] for k in x])
    # Remove the empty list
    x = x[1:]
    print(x)
    # Check the sums of all lists
    for i in x:
        if sum(i) == 0:
            return True
    return False


print(SumIsZero([-1,1,2,3,3,4,4,5]))