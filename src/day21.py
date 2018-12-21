# Day 21:


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


def main():
    reg = [0] * 6
    ip = 2
    pos = reg[ip]

    reg[0] = 13443200

    with open('../assets/day21_input.txt') as file:
        inst = []
        for s in file.read().split('\n'):
            inst.append((s[0:4], *list(map(int, s[5:].split()))))

    while 0 <= pos < len(inst):
        reg[ip] = pos
        reg[inst[pos][3]] = OPCODES[inst[pos][0]](reg, *inst[pos][1:3])
        pos = reg[ip]
        pos += 1


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
