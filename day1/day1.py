# Day 1: Coronal Calibration

from utils import *


def calibrate():
    deltas = ints(get_input())

    frequency = 0
    values = set()
    index = 0
    length = len(deltas)
    while frequency not in values:
        values.add(frequency)
        frequency += deltas[index]
        index = (index + 1) % length

    return frequency


if __name__ == '__main__':
    print('Part 1:', sum(ints(get_input())))
    print('Part 2', calibrate())
