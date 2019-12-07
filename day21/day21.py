# Day 21: Chronal Conversion

from utils import *


def main():
    runner = ElfCode(get_input_lines(), 2)
    runner.reg[0] = 13443200
    runner.run()


def lower():
    def calc(a, b):
        b += (a & 255)
        return ((b & 16777215) * 65899) & 16777215

    r4 = 0
    r3 = r4 | 65536
    r4 = calc(r3, 10283511)
    while r3 >= 256:
        r3 //= 256
        r4 = calc(r3, r4)
    print('Part 1:', r4)


def upper():
    def calc(a, b):
        b += (a & 255)
        return ((b & 16777215) * 65899) & 16777215

    r4 = 0
    keys = set()
    sr4 = []
    while True:
        r3 = r4 | 65536
        r4 = calc(r3, 10283511)
        while r3 >= 256:
            r3 //= 256
            r4 = calc(r3, r4)
        if (r3, r4) in keys:
            break
        else:
            keys.add((r3, r4))
            sr4.append(r4)

    # Find the last unique value
    found = set()
    unique = 0
    while sr4:
        x = sr4.pop(0)
        if x not in found:
            unique = x
        found.add(x)
    print('Part 2:', unique)


if __name__ == '__main__':
    lower()
    upper()

    # Used for visualization and testing
    # main()
