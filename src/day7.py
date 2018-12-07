# Day 7: The Sum of its Parts
from heapq import *


class Worker:
    def __init__(self):
        self.step = ''
        self.time = 0


def find_correct_order():
    graph = build_graph()
    available = []
    complete = []

    def add_avail():
        rem = set()
        for k, v in graph.items():
            if len(v - set(complete)) == 0:
                heappush(available, k)
                rem.add(k)
        for k in rem:
            del graph[k]

    add_avail()
    while available:
        step = heappop(available)
        complete.append(step)
        add_avail()

    print('Order:', ''.join(complete))


def find_parallel_time():
    graph = build_graph()
    available = []
    complete = set()
    workers = (Worker(), Worker(), Worker(), Worker(), Worker())

    def add_avail():
        rem = set()
        for k, v in graph.items():
            if len(v - complete) == 0:
                heappush(available, k)
                rem.add(k)
        for k in rem:
            del graph[k]

    time = 0
    while True:
        for i in range(5):
            if workers[i].step != '' and workers[i].time == 0:
                complete.add(workers[i].step)
                workers[i].step = ''

        add_avail()

        for i in range(5):
            if workers[i].step == '' and len(available) > 0:
                step = heappop(available)
                workers[i].step = step
                workers[i].time = ord(step) - 4

        flag = True
        for i in range(5):
            if workers[i].step != '':
                workers[i].time -= 1
                flag = False

        if flag:
            break
        time += 1

    print('Time:', time)


def build_graph():
    f = open('../assets/day7_input.txt')
    graph = {}
    for line in f:
        if line[36] not in graph:
            graph[line[36]] = set()
        if line[5] not in graph:
            graph[line[5]] = set()
        graph[line[36]].add(line[5])
    return graph


if __name__ == '__main__':
    find_correct_order()
    find_parallel_time()
