from itertools import product
def DistinctPowers(a, b):
    """
    Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
    If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:
    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
    :param a: Start
    :param b: Stop
    :return: Length of distinct terms
    """
    result = set()
    for i, k in product(range(a, b+1), range(a, b+1)):
        print(i, k)
        result.add(i**k)
    return len(result)

print(DistinctPowers(2, 5))