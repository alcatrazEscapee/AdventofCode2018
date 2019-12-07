# Day 2: Inventory Management System

from utils import *


def checksum():
    twos = 0
    threes = 0
    for line in get_input_lines():
        is_two = False
        is_three = False
        for c in set(line):
            num = line.count(c)
            if num == 2:
                is_two = True
            elif num == 3:
                is_three = True

        if is_two:
            twos += 1
        if is_three:
            threes += 1

    print('Twos: %d, Threes: %d, Product: %d' % (twos, threes, twos * threes))


def find_common():
    lines = get_input_lines()

    for i in range(len(lines)):
        for j in range(i, len(lines)):
            diffs = 0
            for k in range(len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    diffs += 1

            if diffs == 1:
                print(lines[i] + '\n' + lines[j])


if __name__ == '__main__':
    checksum()
    find_common()
