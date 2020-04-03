import random

def rand5():
    return random.randint(1,5)

def rand7():
    x = rand5() + rand5() * 5 - 5
    if x >= 22:
        return rand7()
    else:
        return x % 7 + 1

for i in range(1,100):
    print(rand7())