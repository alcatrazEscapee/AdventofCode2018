from re import findall
from typing import Iterable


def get_input(path: str = None) -> str:
    if path is None:
        path = './input.txt'
    with open(path) as f:
        return f.read()


def get_input_lines(path: str = None) -> list:
    return get_input(path).split('\n')


def ints(text: str) -> tuple:
    return tuple(map(int, findall('([+\-0-9]+)', text)))


class ElfCode:
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

    def __init__(self, input_lines: Iterable[str], ip: int = 4):
        self.reg = [0] * 6
        self.ip = ip
        self.pos = self.reg[self.ip]
        self.inst = [(s[0:4], *list(map(int, s[5:].split()))) for s in input_lines]

    def run(self):
        while 0 <= self.pos < len(self.inst):
            self.reg[self.ip] = self.pos
            self.reg[self.inst[self.pos][3]] = ElfCode.OPCODES[self.inst[self.pos][0]](self.reg, *self.inst[self.pos][1:3])
            self.pos = self.reg[self.ip]
            self.pos += 1
