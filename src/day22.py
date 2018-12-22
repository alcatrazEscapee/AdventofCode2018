# Day 22: Mode Maze
from heapq import heappush, heappop


class Path:
    def __init__(self, time=0, x=0, y=0, tool='T'):
        self.time = time
        self.x = x
        self.y = y
        self.tool = tool

    def __lt__(self, other):
        return self.time < other.time


def build_map(tx: int, ty: int, extra: int = 0):
    # Size and target positions
    sx, sy = tx + 1 + extra, ty + 1 + extra
    geo = [[0 for x in range(sx)] for y in range(sy)]
    # Geological factor for edge cases
    for x in range(sx):
        geo[0][x] = 16807 * x
    for y in range(sy):
        geo[y][0] = 48271 * y

    # Geological factor from erosion of previous factors
    for x in range(1, sx):
        for y in range(1, sy):
            if x != tx or y != ty:
                geo[y][x] = erosion(geo[y - 1][x]) * erosion(geo[y][x - 1])
    return list(list(map(terrain, geo[y])) for y in range(sy))


def erosion(p):
    return (p + DEPTH) % 20183


def terrain(p):
    return erosion(p) % 3


def find_risk(tx: int, ty: int):
    geo = build_map(tx, ty)
    print('Risk =', sum(sum(geo[y]) for y in range(MAX_Y)))


def find_path(tx: int, ty: int, extra: int = 100):
    ero = build_map(tx, ty, extra)
    queue = []
    visited = set()
    heappush(queue, Path())
    shortest_to_target = -1
    # Dijkstra's Algorithm - Modified to use three ending conditions for a 'visited' node
    while queue and (tx, ty, 'T') not in visited:
        path = heappop(queue)
        if (path.x, path.y, path.tool) in visited:
            continue

        visited.add((path.x, path.y, path.tool))
        curr_area = ero[path.y][path.x]

        for card in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_path = (path.x + card[0], path.y + card[1])
            if next_path[0] < 0 or next_path[1] < 0 or next_path[0] >= tx + extra or next_path[1] >= ty + extra:
                continue

            next_area = ero[next_path[1]][next_path[0]]
            if path.tool != 'NTC'[next_area]:
                # Tool valid - proceed with current tool
                heappush(queue, Path(path.time + 1, *next_path, path.tool))
            else:
                # Tool invalid - switch tool based on next and current area
                next_tool = {0: 'TCT', 1: 'CNN', 2: 'TNN'}[next_area][curr_area]
                heappush(queue, Path(path.time + 8, *next_path, next_tool))

        if path.x == tx and path.y == ty:
            if path.tool != 'T':
                path.time += 7
            if shortest_to_target == -1 or path.time < shortest_to_target:
                shortest_to_target = path.time
    print('Shortest Path =', shortest_to_target)


DEPTH = 6084
MAX_X, MAX_Y = 15, 710
TARGET = (14, 709)

if __name__ == '__main__':
    find_risk(*TARGET)
    find_path(*TARGET)
