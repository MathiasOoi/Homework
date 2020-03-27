with open("race.in", "r") as fin:
    k, n = fin.readline().split()
    x = []
    for finishSpeed in fin.readlines():
        x.append(int(finishSpeed))

def race(k, cap):
    travel = 0
    deceleration_travel = 0
    seconds = 0
    speed = 0
    while True:
        print(travel)
        print(deceleration_travel)
        speed += 1
        travel += speed
        seconds += 1
        if travel + deceleration_travel >= int(k):
            return seconds
        if speed >= cap:
            deceleration_travel += speed
            seconds += 1
        if travel + deceleration_travel >= int(k):
            return seconds


if __name__ == '__main__':
    with open("race.out", "w") as fout:
        for i in x:
            fout.write(str(race(k, i)) + '\n')



