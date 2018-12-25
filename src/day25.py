# Day 25: Four Dimensional Adventure
from networkx import Graph, number_connected_components
from golf.day25 import f as find_constellations_golf


def find_constellations():
    with open('../assets/day25_input.txt') as file:
        nodes = [tuple(map(int, line.split(','))) for line in file]

    graph = Graph()
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            if sum(abs(nodes[i][k] - nodes[j][k]) for k in range(4)) <= 3:
                graph.add_edge(nodes[i], nodes[j])

    print('Number of Constellations: %d' % number_connected_components(graph))


if __name__ == '__main__':
    find_constellations()
    find_constellations_golf(open('../assets/day25_input.txt'))
