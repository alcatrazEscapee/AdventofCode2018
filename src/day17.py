# Day 17: Reservoir Research
from collections import namedtuple


class Point(namedtuple('Point', 'x y')):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def print_map(clay, flowing, still, x1=300, x2=700, y1=0, y2=1000):
    def char(p):
        if p == SPRING:
            return '+'
        elif p in clay:
            return '#'
        elif p in both:
            return '$' # For water that is tagged as both flowing and still
        elif p in still:
            return '~'
        elif p in flowing:
            return '|'
        else:
            return '.'

    both = flowing & still
    print('\n'.join(''.join(char(Point(x, y)) for x in range(x1, 1 + x2)) for y in range(y1, 1 + y2)))


def simulate():
    clay = set()
    with open('../assets/day17_input.txt') as file:
        for line in file:
            nums = list(map(int, ''.join(c if c.isnumeric() else ' ' for c in line).split()))
            if line[0] == 'x':
                for y in range(nums[1], 1 + nums[2]):
                    clay.add(Point(nums[0], y))
            elif line[0] == 'y':
                for x in range(nums[1], 1 + nums[2]):
                    clay.add(Point(x, nums[0]))

    lowest_y, highest_y = max(p.y for p in clay), min(p.y for p in clay)
    flowing, still, to_fall, to_spread = set(), set(), set(), set()

    # Because python sucks at recursion - need to do it manually
    to_fall.add(SPRING)
    while to_fall or to_spread:
        while to_fall:
            tf = to_fall.pop()
            res = fall(tf, lowest_y, clay, flowing)
            if res:
                to_spread.add(res)

        while to_spread:
            ts = to_spread.pop()
            rl, rr = spread(ts, clay, flowing, still)
            if not rr and not rl:
                to_spread.add(ts + UP)
            else:
                if rl:
                    to_fall.add(rl)
                if rr:
                    to_fall.add(rr)

    # Output
    print_map(clay, flowing, still, y2=lowest_y)
    print('Total Water = %d' % len([p for p in (flowing | still) if p.y >= highest_y]))
    print('Still Water = %d' % len([p for p in still if p.y >= highest_y]))


def fall(pos, ly, clay, flowing):
    while pos.y < ly:
        posd = pos + DOWN
        if posd not in clay:
            flowing.add(posd)
            pos = posd
        elif posd in clay:
            return pos
    return None


def spread(pos, clay, flowing, still):
    temp = set()
    pl = spread_r(pos, LEFT, clay, still, temp)
    pr = spread_r(pos, RIGHT, clay, still, temp)
    if not pl and not pr:
        still.update(temp)
    else:
        flowing.update(temp)
    return pl, pr


def spread_r(pos, off, clay, still, temp):
    pos1 = pos
    while pos1 not in clay:
        temp.add(pos1)
        pos2 = pos1 + DOWN
        if pos2 not in clay and pos2 not in still:
            return pos1
        pos1 = pos1 + off
    return None


SPRING = Point(500, 0)
UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

if __name__ == '__main__':
    simulate()
