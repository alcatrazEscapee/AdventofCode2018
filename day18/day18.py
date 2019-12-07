# Day 18: Settlers of the North Pole

from collections import namedtuple, defaultdict
from utils import *


class Point(namedtuple('Point', 'x y')):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def main():
    txt = get_input_lines()

    yard = defaultdict(lambda: 'X')
    for y in range(len(txt)):
        for x in range(len(txt[0])):
            yard[Point(x, y)] = txt[y][x]

    i = 0
    prev = set()
    while i < 600:
        next_state = defaultdict(lambda: '.')
        for x in range(SIZE):
            for y in range(SIZE):
                p = Point(x, y)
                if yard[p] == '.':
                    trees = 0
                    for off in ADJ:
                        if yard[p + off] == '|':
                            trees += 1
                    if trees >= 3:
                        next_state[p] = '|'
                    else:
                        next_state[p] = '.'
                elif yard[p] == '|':
                    yards = 0
                    for off in ADJ:
                        if yard[p + off] == '#':
                            yards += 1
                    if yards >= 3:
                        next_state[p] = '#'
                    else:
                        next_state[p] = '|'
                elif yard[p] == '#':
                    lumber, tree = False, False
                    for off in ADJ:
                        if yard[p + off] == '|':
                            tree = True
                        elif yard[p + off] == '#':
                            lumber = True
                    if lumber and tree:
                        next_state[p] = '#'
                    else:
                        next_state[p] = '.'
        yard = next_state
        i += 1
        value = sum(v == '#' for v in yard.values()) * sum(v == '|' for v in yard.values())
        if value in prev:
            print('Repeat Found')
        prev.add(value)
        print(i, value)


SIZE = 50
ADJ = {Point(-1, -1), Point(-1, 0), Point(-1, 1), Point(0, -1), Point(0, 1), Point(1, -1), Point(1, 0), Point(1, 1)}

if __name__ == '__main__':
    main()
