import random

random.seed(0)


def rand5():
    return random.randint(1, 5)


def rand7():
    outcomes = [
        [1, 1, 1, 2, 2],
        [2, 3, 3, 3, 4],
        [4, 4, 4, 5, 5],
        [5, 6, 6, 6, 7],
        [7, 7, 0, 0, 0]
    ]
    i, k = rand5() - 1, rand5() - 1
    return outcomes[i][k] if outcomes[i][k] else rand7()


for _ in range(1, 100):
    print(rand7())
