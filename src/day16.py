# Day 16: Chronal Classification
from collections import defaultdict
from copy import deepcopy

OPCODES = {
    'addr': lambda r, a, b: r[a] + r[b],
    'addi': lambda r, a, b: r[a] + b,
    'mulr': lambda r, a, b: r[a] * r[b],
    'muli': lambda r, a, b: r[a] * b,
    'banr': lambda r, a, b: r[a] & r[b],
    'bani': lambda r, a, b: r[a] & b,
    'borr': lambda r, a, b: r[a] | r[b],
    'bori': lambda r, a, b: r[a] | b,
    'setr': lambda r, a, b: r[a],
    'seti': lambda r, a, b: a,
    'gtir': lambda r, a, b: a > r[b],
    'gtri': lambda r, a, b: r[a] > b,
    'gtrr': lambda r, a, b: r[a] > r[b],
    'eqir': lambda r, a, b: a == r[b],
    'eqri': lambda r, a, b: r[a] == b,
    'eqrr': lambda r, a, b: r[a] == r[b]
}


class RTest:
    def __init__(self, reg, args, exp):
        self.reg = reg
        self.opc = args[0]
        self.args = args[1:]
        self.exp = exp


def main():
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

    match_three = 0
    functions = {}
    for test in tests:
        matches = set()
        valid = 0
        for name, opc in OPCODES.items():
            reg = deepcopy(test.reg)
            reg[test.args[2]] = opc(reg, *test.args[0:2])
            if reg == test.exp:
                valid += 1
                if opc not in functions.values():
                    matches.add(name)

        if len(matches) == 1:
            name = matches.pop()
            functions[test.opc] = OPCODES[name]
            print('%s = %d' % (name, test.opc))

        if valid >= 3:
            match_three += 1

    print('3+ Test Matches = %d' % match_three)

    # Test Program (Part 2)
    reg = defaultdict(int)
    for line in open('../assets/day16_input2.txt').read().split('\n'):
        args = list(map(int, line.split()))
        reg[args[3]] = functions[args[0]](reg, *args[1:3])
    print('Test Program Result = %d' % reg[0])


if __name__ == '__main__':
    main()
