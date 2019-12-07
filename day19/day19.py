# Day 19: Go With The Flow

from utils import *


def slow():
    runner = ElfCode(get_input_lines())
    runner.run()
    print('Slow Part 1:', runner.reg[0])


def fast(r2: int):
    r0 = 0
    for i in range(1, r2 + 1):
        if r2 % i == 0:
            r0 += i
    print('Fast Part 2:', r0)


if __name__ == '__main__':
    slow()
    fast(986)
    fast(10551386)
