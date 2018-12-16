# Day 16: Chronal Classification
from collections import defaultdict
from copy import deepcopy


class RTest:
    def __init__(self, reg, args, exp):
        self.reg = reg
        self.opc = args[0]
        self.args = args[1:]
        self.exp = exp


def main():
    def addr(a, b, c):
        reg[c] = reg[a] + reg[b]

    def addi(a, b, c):
        reg[c] = reg[a] + b

    def mulr(a, b, c):
        reg[c] = reg[a] * reg[b]

    def muli(a, b, c):
        reg[c] = reg[a] * b

    def banr(a, b, c):
        reg[c] = reg[a] & reg[b]

    def bani(a, b, c):
        reg[c] = reg[a] & b

    def borr(a, b, c):
        reg[c] = reg[a] | reg[b]

    def bori(a, b, c):
        reg[c] = reg[a] | b

    def setr(a, b, c):
        reg[c] = reg[a]

    def seti(a, b, c):
        reg[c] = a

    def gtir(a, b, c):
        reg[c] = 1 if a > reg[b] else 0

    def gtri(a, b, c):
        reg[c] = 1 if reg[a] > b else 0

    def gtrr(a, b, c):
        reg[c] = 1 if reg[a] > reg[b] else 0

    def eqir(a, b, c):
        reg[c] = 1 if a == reg[b] else 0

    def eqri(a, b, c):
        reg[c] = 1 if reg[a] == b else 0

    def eqrr(a, b, c):
        reg[c] = 1 if reg[a] == reg[b] else 0

    opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    with open('../assets/day16_input.txt') as file:
        lines = file.read().split('\n')

    tests = set()
    reg = defaultdict(int)
    exp = defaultdict(int)
    while lines:
        idx = 0
        # Before
        for p in map(int, lines.pop(0)[9:-1].replace(',', '').split()):
            reg[idx] = p
            idx += 1
        # Args
        args = tuple(map(int, lines.pop(0).replace(',', '').split()))
        # After
        idx = 0
        for p in map(int, lines.pop(0)[9:-1].replace(',', '').split()):
            exp[idx] = p
            idx += 1
        tests.add(RTest(deepcopy(reg), args, deepcopy(exp)))
        lines.pop(0)

    reg = defaultdict(int)
    match_three = 0
    functions = {}
    for test in tests:
        matches = set()
        valid = 0
        for opc in opcodes:
            reg = deepcopy(test.reg)
            opc(*test.args)
            if reg == test.exp:
                valid += 1
                if opc not in functions.values():
                    matches.add(opc)

        if len(matches) == 1:
            opc = matches.pop()
            functions[test.opc] = opc
            print('Opcode %d = \'%s\'' % (test.opc, opc.__name__))

        if valid >= 3:
            match_three += 1

    print('3+ Test Matches = %d' % match_three)

    # Test Program (Part 2)
    reg = defaultdict(int)
    for line in open('../assets/day16_input2.txt').read().split('\n'):
        args = list(map(int, line.split()))
        functions[args[0]](*args[1:])
    print('Test Program Result = %d' % reg[0])


if __name__ == '__main__':
    main()
