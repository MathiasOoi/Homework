with open("race.in", "r") as fin:
    k, n = [int(i) for i in fin.readline().split()]
    x = [int(i) for i in fin.readlines()]


def race(k, cap):
    travel = 0
    deceleration_travel = 0
    seconds = 0
    speed = 0
    while True:
        speed += 1
        travel += speed
        seconds += 1
        if travel + deceleration_travel >= k:
            return seconds
        if speed >= cap:
            deceleration_travel += speed
            seconds += 1
        if travel + deceleration_travel >= k:
            return seconds


if __name__ == '__main__':
    with open("race.out", "w") as fout:
        for i in x:
            fout.write(str(race(k, i)) + '\n')



