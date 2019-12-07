# Day 3: No Matter How you Slice It

from utils import *


def find_overlap():
    points = set()
    collisions = set()
    lines = list(map(ints, get_input_lines()))

    for p in lines:
        for x in range(p[1], p[1] + p[3]):
            for y in range(p[2], p[2] + p[4]):
                if (x, y) not in points:
                    points.add((x, y))
                else:
                    collisions.add((x, y))

    print('There are %d collisions' % len(collisions))

    for p in lines:
        collides = False
        for x in range(p[1], p[1] + p[3]):
            for y in range(p[2], p[2] + p[4]):
                if (x, y) in collisions:
                    collides = True

        if not collides:
            print('Claim %d does not collide!' % p[0])


if __name__ == '__main__':
    find_overlap()
