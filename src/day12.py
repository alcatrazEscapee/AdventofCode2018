# Day 12: Subterranean Sustainability


def part1(start: str):
    rules = load_rules()
    plants = set()
    for i in range(len(start)):
        if start[i] == '#':
            plants.add(i)
    prev = 0
    for i in range(500):
        plants = iterate(plants, rules)
        print(i, sum(plants), prev - sum(plants))
        prev = sum(plants)


def iterate(plants, rules):
    minP = min(plants) - 3
    maxP = max(plants) + 3
    plants2 = set()
    for i in range(minP, maxP + 1):
        mp = ''
        for off in range(-2, 3):
            mp += '#' if i + off in plants else '.'
        if mp in rules:
            plants2.add(i)
    return plants2


def load_rules():
    rules = set()
    with open('../assets/day12_input.txt') as file:
        for line in file:
            args = line.split(' => ')
            if args[1][0] == '#':
                rules.add(args[0])
    return rules


if __name__ == '__main__':
    part1('##.#############........##.##.####..#.#..#.##...###.##......#.#..#####....##..#####..#.#.##.#.##')

