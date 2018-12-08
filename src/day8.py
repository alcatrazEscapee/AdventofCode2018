# Day 8: Memory Maneuver


class Node:
    def __init__(self, child_size, meta_size):
        self.meta_size = meta_size
        self.child_size = child_size
        self.children = []
        self.meta = []

    def add_child(self, node):
        self.children.append(node)

    def add_meta(self, meta):
        self.meta.append(meta)

    def value(self):
        v = 0
        if len(self.children) == 0:
            return sum(self.meta)
        for i in self.meta:
            if 0 < i <= len(self.children):
                v += self.children[i - 1].value()
        return v

    def __repr__(self):
        return '{M: (%s), C:(%s)}' % (self.meta, self.children)


def check1():
    with open('../assets/day8_input.txt') as file:
        lines = list(map(int, file.read().split()))

    nodes = [lines.pop(0)]
    meta = [lines.pop(0)]
    meta_sum = 0

    while nodes:
        if nodes[0] == 0:
            nodes.pop(0)
            for i in range(meta.pop(0)):
                meta_sum += lines.pop(0)
        else:
            nodes[0] -= 1
            nodes.insert(0, lines.pop(0))
            meta.insert(0, lines.pop(0))
    print('Metadata sum: ', meta_sum)


def check2():
    tree = build_tree()
    print('Node value: ', tree.value())


def build_tree():
    with open('../assets/day8_input.txt') as file:
        lines = list(map(int, file.read().split()))

    root = Node(lines.pop(0), lines.pop(0))
    nodes = [root]
    while nodes:
        if nodes[0].child_size == 0:
            for i in range(nodes[0].meta_size):
                nodes[0].add_meta(lines.pop(0))
            nodes.pop(0)
        else:
            nodes[0].child_size -= 1
            child = Node(lines.pop(0), lines.pop(0))
            nodes[0].add_child(child)
            nodes.insert(0, child)
    return root


if __name__ == '__main__':
    check1()
    check2()