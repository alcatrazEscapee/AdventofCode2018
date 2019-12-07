# Day 11: Chronal Charge


def fuel_cell(x: int, y: int):
    rack = x + 10
    power = rack * y
    power += SERIAL
    power *= rack
    power = (power // 100) % 10
    power -= 5
    return power


def fuel_cell_f(x: int, y: int):
    return FUEL_GRID[y][x]


def fuel_grid(x: int, y: int, s: int):
    total = 0
    for i in range(s):
        for j in range(s):
            total += fuel_cell(x + i, y + j)
    return total


def max_grid(xm: int = 300, ym: int = 300, s: int = 3):
    grids = [(x, y, fuel_grid(x, y, s)) for x in range(xm + 1 - s) for y in range(ym + 1 - s)]
    return max(grids, key=lambda x: x[2])


def max_any_grid():
    gm = (0, 0, 0)
    for size in range(300):
        g = max_grid(s=size + 1)
        if g[2] > gm[2]:
            gm = g
        print(size, g, gm)
    return gm


SERIAL = 4172
FUEL_GRID = [[fuel_cell(x, y) for x in range(300)] for y in range(300)]

if __name__ == '__main__':
    print(max_grid())
    print(max_any_grid())