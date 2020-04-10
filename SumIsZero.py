def SumIsZero(lst):
    x = [[]]
    # Create a list of lists of all possible sub-sets
    # For every integer in lst (i)
    # Create a list that adds i to every list in x
    # Add the new list to x
    for i in lst:
        x += [k + [i] for k in x]
    # Remove the empty list
    x = x[1:]
    # Check the sums of all lists
    for i in x:
        if sum(i) == 0:
            return True
    return False


print(SumIsZero([-1,1,2,3,3,4,4,5]))