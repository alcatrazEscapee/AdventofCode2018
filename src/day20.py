# Day 20: A Regular Map
import networkx


def build_graph(txt):
    graph = networkx.Graph()
    stack = []
    start = pos = 0

    for t in txt:
        if t in 'NEWS':
            step = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}[t]
            graph.add_edge(pos, pos + step)
            pos += step
        elif t == '(':
            stack.append(start)
            start = pos
        elif t == '|':
            pos = start
        elif t == ')':
            start = stack.pop()

    return networkx.algorithms.shortest_path_length(graph, 0)


def part1(p):
    return max(p.values())


def part2(p):
    return sum(s >= 1000 for s in p.values())


TESTS = {
    '^WNE$': 3,
    '^ENWWW(NEEE|SSE(EE|N))$': 10,
    '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$': 18,
    '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$': 23,
    '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$': 31
}

if __name__ == '__main__':
    for test, exp in TESTS.items():
        assert part1(build_graph(test)) == exp

    print('Test Cases Complete')

    with(open('../assets/day20_input.txt')) as file:
        actual = build_graph(file.read())
        print('Part 1:', part1(actual))
        print('Part 2:', part2(actual))
