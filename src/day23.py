# Day 23:
from collections import namedtuple


class Bot(namedtuple('Bot', 'x y z r')):
    def __repr__(self):
        return '{%d %d %d %d}' % (self.x, self.y, self.z, self.r)

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, f):
        return Point(self.x * f, self.y * f, self.z * f)

    def __repr__(self):
        return '%d %d %d' % (self.x, self.y, self.z)


def main():
    with open('../assets/day23_input.txt') as file:
        bots = set()
        max_bot = None
        for line in file.read().split('\n'):
            args = list(map(int, ''.join(c if c.isnumeric() or c == '-' else ' ' for c in line).split()))
            bot = Bot(*args)
            bots.add(bot)
            if not max_bot or bot.r > max_bot.r:
                max_bot = bot

    print('In Range:', sum(max_bot.dist(other) <= max_bot.r for other in bots))

    pos = Point(0, 0, 0)
    found = in_range(bots, pos)
    dir_i = 1
    i = 0
    scale = 1
    swaps = 0
    while i < 10000:
        p_next = pos + DIRS[dir_i].scale(scale)
        f_next = in_range(bots, p_next)
        if f_next < found:
            if scale == 1:
                dir_i = (dir_i + 1) % 6
                swaps += 1
                if swaps > 10:
                    print('Arrived at an optimal point!')
                    break
            else:
                scale //= 2
                swaps = 0
        else:
            pos = p_next
            found = f_next
            scale *= 2
            swaps = 0
        i += 1
    print('Bots:', found, 'Distance:', abs(pos.x) + abs(pos.y) + abs(pos.z))


def in_range(bots, pos):
    return sum(b.dist(pos) <= b.r for b in bots)


DIRS = (Point(0, 0, 1), Point(0, 1, 0), Point(1, 0, 0), Point(0, 0, -1), Point(0, -1, 0), Point(-1, 0, 0))


if __name__ == '__main__':
    main()
