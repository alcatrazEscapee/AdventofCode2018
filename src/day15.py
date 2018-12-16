# Day 15: Beverage Battles
from collections import namedtuple, defaultdict

Path = namedtuple('Path', 'pos dist start')


class Point(namedtuple('Point', 'x y')):
    def order(self):
        return self.x + self.y * 9999

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Entity:
    def __init__(self, x: int, y: int, key: str, atk: int = 3, hp: int = 200):
        self.pos = Point(x, y)
        self.key = key
        self.atk = atk
        self.hp = hp

    def __repr__(self):
        return '{%s: x: %d, y: %d, hp: %d}' % (self.key, self.pos.x, self.pos.y, self.hp)

    def move(self, p: Point):
        self.pos = self.pos + p

    def dead(self) -> bool:
        return self.hp <= 0


class CombatMap:
    def __init__(self, txt, elf_atk: int = 3):
        lines = txt.split('\n')
        self.sy = len(lines)
        self.sx = len(lines[0])
        self.walls = set()
        self.entities = []

        for y in range(self.sy):
            for x in range(self.sx):
                if lines[y][x] == '#':
                    self.walls.add(Point(x, y))
                elif lines[y][x] == 'G':
                    self.entities.append(Entity(x, y, 'G'))
                elif lines[y][x] == 'E':
                    self.entities.append(Entity(x, y, 'E', elf_atk))

    def wall(self, p: Point):
        return p in self.walls

    def empty(self, p: Point, ignore: Entity = None):
        return p not in self.walls and p not in [e.pos for e in self.entities if e != ignore and not e.dead()]

    def ent(self, p: Point):
        for e in self.entities:
            if e.pos == p and not e.dead():
                return e
        else:
            return None

    def sort_ent(self):
        self.entities.sort(key=lambda e: e.pos.order())

    def enemies(self, ent: Entity) -> set:
        return set(e for e in self.entities if e.key != ent.key and not e.dead())


def best_path(p: Path, q: Path):
    if p.dist < q.dist:
        return p
    elif p.dist > q.dist:
        return q
    else:
        if p.pos.order() < q.pos.order():
            return p
        else:
            return q


def find_path(cmap: CombatMap, ent: Entity) -> Point:
    # Is there an enemy in range - ignore moving
    for card in CARDINALS:
        pos: Point = ent.pos + card
        enemy = cmap.ent(pos)
        if enemy and enemy.key != ent.key:
            return ZERO

    # Calculate all enemy positions
    enemy_pos = set()
    for enemy in cmap.enemies(ent):
        for card in CARDINALS:
            pos = enemy.pos + card
            if cmap.empty(pos, ignore=ent):
                enemy_pos.add(pos)

    # Dijkstra's Algorithm
    path_map = defaultdict(lambda: Path(ZERO, 0, ZERO))
    visited = set(ent.pos)
    queue = []
    # First four points determine the starting position
    for card in CARDINALS:
        pos: Point = ent.pos + card
        if cmap.empty(pos, ignore=ent):
            new_path = Path(pos, 1, card)
            queue.append(new_path)
            path_map[pos] = new_path

    # Continue with visiting queue
    while queue:
        path = queue.pop(0)
        if path.pos in visited:
            continue
        visited.add(path.pos)

        for card in CARDINALS:
            new = path.pos + card

            if cmap.empty(new):
                new_path = Path(new, path.dist + 1, path.start)
                queue.append(new_path)
                # Operator here means 'the shortest path, then by starting position'
                if new not in path_map:
                    path_map[new] = new_path
                else:
                    path_map[new] = best_path(new_path, path_map[new])

    # Remove positions that have no valid path (including the starting position)
    enemy_pos = [p for p in enemy_pos if path_map[p].dist != 0]
    if not enemy_pos:
        return ZERO

    min_dist = min(path_map[p].dist for p in enemy_pos)
    min_path = min((path_map[p] for p in enemy_pos if path_map[p].dist == min_dist), key=lambda p: p.pos.order())
    return min_path.start


def attack(cmap: CombatMap, ent: Entity):
    enemies = [e for e in cmap.enemies(ent) if e.pos - ent.pos in CARDINALS]
    if enemies:
        min_hp = min(e.hp for e in enemies)
        min_enemy = min((e for e in enemies if e.hp == min_hp), key=lambda e: e.pos.order())

        min_enemy.hp -= ent.atk


def outcome(txt: str, elf_atk: int = 3, no_deaths: bool = False, output: bool = False) -> int:
    combat_map = CombatMap(txt, elf_atk)

    rounds = 0
    while True:
        # Entity Actions in Reading Order
        combat_map.sort_ent()
        for entity in combat_map.entities:
            if entity.dead():
                continue
            # End condition for combat
            if not combat_map.enemies(entity):
                total_hp = sum(e.hp for e in combat_map.entities if not e.dead())
                combat_result = rounds * total_hp
                if output:
                    print('Combat Ended: %d x %d = %d' % (rounds, total_hp, combat_result))
                return combat_result

            path = find_path(combat_map, entity)
            entity.move(path)

            attack(combat_map, entity)

        if no_deaths and [e for e in combat_map.entities if e.key == 'E' and e.dead()]:
            print('Atk = %d Failed!' % elf_atk)
            return -1

        rounds += 1


CARDINALS = (Point(0, -1), Point(-1, 0), Point(1, 0), Point(0, 1))
ZERO = Point(0, 0)

if __name__ == '__main__':
    # Test Cases
    assert outcome('####\n##E#\n#GG#\n####') == 13400
    assert outcome('#######\n#G..#E#\n#E#E.E#\n#G.##.#\n#...#E#\n#...E.#\n#######') == 36334
    assert outcome('#######\n#E..EG#\n#.#G.E#\n#E.##E#\n#G..#.#\n#..E#.#\n#######') == 39514
    assert outcome('#######\n#E.G#.#\n#.#G..#\n#G.#.G#\n#G..#.#\n#...E.#\n#######') == 27755
    assert outcome('#######\n#.E...#\n#.#..G#\n#.###.#\n#E#G#G#\n#...#G#\n#######') == 28944
    assert outcome('#######\n#.G...#\n#...EG#\n#.#.#G#\n#..G#E#\n#.....#\n#######') == 27730
    assert outcome(
        '#########\n#G......#\n#.E.#...#\n#..##..G#\n#...##..#\n#...#...#\n#.G...G.#\n#.....G.#\n#########') == 18740

    # Part 1 - result = 82 x 2459 = 201638
    input_map = open('../assets/day15_input.txt').read()
    outcome(input_map, output=True)

    # Part 2 - result = 10 Attack = 95764
    result, elf_attack = -1, 4
    while result == -1:
        result = outcome(input_map, elf_atk=elf_attack, no_deaths=True, output=True)
        elf_attack += 1
