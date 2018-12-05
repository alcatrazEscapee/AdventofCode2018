# Day 2: Inventory Management System
from golf.day2 import f as checksum_golf


def checksum():
    with open('../assets/day2_input.txt') as file:
        twos = 0
        threes = 0
        for line in file:
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
    lines = []
    with open('../assets/day2_input.txt') as file:
        for line in file:
            lines.append(line)

    for i in range(len(lines)):
        for j in range(i, len(lines)):
            diffs = 0
            for k in range(len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    diffs += 1

            if diffs == 1:
                print(lines[i] + '\n' + lines[j])


checksum()
find_common()


checksum_golf(open('../assets/day2_input.txt'))
