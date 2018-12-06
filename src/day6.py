# Day 6: Chronal Coordinates


EXAMPLE = {
    'a': (1, 1),
    'b': (1, 6),
    'c': (8, 3),
    'd': (3, 4),
    'e': (5, 5),
    'f': (8, 9)
}
COORDS = {
    'a': (192, 212),
    'b': (294, 73),
    'c': (153, 248),
    'd': (238, 54),
    'e': (354, 207),
    'f': (269, 256),
    'g': (155, 329),
    'h': (132, 308),
    'i': (211, 173),
    'j': (261, 241),
    'k': (300, 218),
    'l': (143, 43),
    'm': (226, 348),
    'n': (148, 349),
    'o': (114, 78),
    'p': (77, 327),
    'q': (140, 327),
    'r': (202, 346),
    's': (174, 115),
    't': (86, 198),
    'u': (132, 152),
    'v': (167, 184),
    'w': (146, 259),
    'x': (277, 288),
    'y': (330, 199),
    'z': (98, 332),
    'A': (290, 186),
    'B': (322, 120),
    'C': (295, 355),
    'D': (346, 260),
    'E': (305, 190),
    'F': (294, 82),
    'G': (156, 159),
    'H': (114, 263),
    'I': (340, 220),
    'J': (353, 207),
    'K': (220, 219),
    'L': (152, 122),
    'M': (223, 319),
    'N': (236, 243),
    'O': (358, 348),
    'P': (174, 116),
    'Q': (306, 74),
    'R': (70, 264),
    'S': (352, 351),
    'T': (194, 214),
    'U': (153, 322),
    'V': (225, 99),
    'W':(237, 331),
    'X': (279, 208)
}


def dist(p, x, y):
    return abs(p[0] - x) + abs(p[1] - y)


def closest(x, y):
    return min(COORDS, key=lambda i: dist(COORDS.get(i), x, y))


def totaldist(x, y):
    return sum(map(lambda i: dist(i[1], x, y), COORDS.items()))


def find_largest_region(size=400):
    size_map = {}
    voronoi = [['' for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            voronoi[i][j] = closest(i, j)

    for i in COORDS.keys():
        size_map[i] = sum(map(lambda x: x.count(i), voronoi))

    for j in set(voronoi[0] + voronoi[size-1] + [v[0] for v in voronoi] + [v[size - 1] for v in voronoi]):
        del size_map[j]

    max_key = max(size_map, key=size_map.get)
    print('Max Region = %d' % size_map[max_key])


def find_clustered_region(size=400):
    voronoi = [['.' for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if totaldist(i, j) < 10000:
                voronoi[i][j] = 'X'

    print('Size of Cluster: %d' % sum(map(lambda i: i.count('X'), voronoi)))


if __name__ == '__main__':
    #find_largest_region()
    find_clustered_region()
