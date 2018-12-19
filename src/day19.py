# Day 19: Go With The Flow

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


def slow():
    reg = [0]*6
    ip = 4
    pos = reg[ip]

    with open('../assets/day19_input.txt') as file:
        inst = []
        for s in file.read().split('\n'):
            inst.append((s[0:4], *list(map(int, s[5:].split()))))

    while 0 <= pos < len(inst):
        reg[ip] = pos
        reg[inst[pos][3]] = OPCODES[inst[pos][0]](reg, *inst[pos][1:3])
        pos = reg[ip]
        pos += 1

    print('Slow Part 1:', reg[0])


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
