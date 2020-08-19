import random
from collections import defaultdict
import time

random.seed(0)
rand7_calls_to_rand5 = 0
rand7x_calls_to_rand5 = 0
outcomes = [
        [1, 1, 1, 2, 2],
        [2, 3, 3, 3, 4],
        [4, 4, 4, 5, 5],
        [5, 6, 6, 6, 7],
        [7, 7, 0, 0, 0]
    ]

def rand5():
    return random.randint(0, 4)

def rand7():
    global rand7_calls_to_rand5
    rand7_calls_to_rand5 += 2
    i, k = rand5(), rand5()
    return outcomes[i][k] if outcomes[i][k] else rand7()

def rand7x(times):
    # times: Int amount of times rand7 will be called
    global rand7x_calls_to_rand5
    distribution = defaultdict(int)
    temp = rand5()
    rand7x_calls_to_rand5 += 1
    for _ in range(times):
        i, k = rand5(), rand5()
        rand7x_calls_to_rand5 += 2
        while not outcomes[i][k]:
            if temp == i == k == 4:
                while temp == 4:
                    temp = rand5()
                    rand7x_calls_to_rand5 += 1
            temp, i, k = k, temp, i  # cycle the values
        distribution[outcomes[i][k]] += 1
    return distribution

def getPercentages(dis, total):
    s = ""
    for i, k in sorted(dis.items()):
        s += str(i) + ": " + str(k/total) + "% "
    return s

if __name__ == "__main__":
    for i in [100, 1000, 10000, 100000]:
        print(i)
        print("rand7")
        d = defaultdict(int)
        for _ in range(i):
            d[rand7()] += 1
        print("Calls: %s"%(rand7_calls_to_rand5))
        print(getPercentages(d, i))
        print("rand7x")
        d = rand7x(i)
        print(getPercentages(d, i))
        print("Calls: %s\n"%(rand7x_calls_to_rand5))
        rand7_calls_to_rand5 = 0
        rand7x_calls_to_rand5 = 0






