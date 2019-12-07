# Day 12: Subterranean Sustainability

from utils import *


def main(start: str):
    rules = load_rules()
    plants = set()
    for i in range(len(start)):
        if start[i] == '#':
            plants.add(i)
    for i in range(20):
        plants = iterate(plants, rules)

    print('Part 1:', sum(plants))

    # By inspection, the difference stabilizes to 53 each generation
    # At 500 generations, the value is 26966
    print('Part 2:', 26966 + (50000000000 - 500) * 53)


def iterate(plants, rules):
    min_p = min(plants) - 3
    max_p = max(plants) + 3
    plants2 = set()
    for i in range(min_p, max_p + 1):
        mp = ''
        for off in range(-2, 3):
            mp += '#' if i + off in plants else '.'
        if mp in rules:
            plants2.add(i)
    return plants2


def load_rules():
    rules = set()
    for line in get_input_lines():
        args = line.split(' => ')
        if args[1][0] == '#':
            rules.add(args[0])
    return rules


if __name__ == '__main__':
    main('##.#############........##.##.####..#.#..#.##...###.##......#.#..#####....##..#####..#.#.##.#.##')
