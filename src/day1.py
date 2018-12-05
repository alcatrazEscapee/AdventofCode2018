# Day 1: Coronal Calibration


def calibrate():
    with open('../assets/day1_input.txt') as file:
        total = 0
        for line in file:
            total += int(line)
    print('The total frequency change is %d' % total)


def calibrate_2():
    with open('../assets/day1_input.txt') as file:
        deltas = []
        for line in file:
            deltas.append(int(line))

    frequency = 0
    values = set()
    index = 0
    length = len(deltas)
    while frequency not in values:
        values.add(frequency)
        frequency += deltas[index]
        index = (index + 1) % length

    print('The first repeated frequency is %d!' % frequency)


calibrate_2()
