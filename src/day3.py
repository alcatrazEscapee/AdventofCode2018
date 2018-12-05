# Day 3: No Matter How you Slice It
from golf.day3 import f as find_overlap_golf


def find_overlap():
    points = set()
    collisions = set()
    lines = []

    with open('../assets/day3_input.txt') as file:
        for line in file:
            # String parsing on easy mode
            lines.append(list(map(int, ''.join([c if c.isnumeric() else ' ' for c in line]).split())))

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


find_overlap()
find_overlap_golf(open('../assets/day3_input.txt'))