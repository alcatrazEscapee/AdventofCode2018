# Day 13:


class Car:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.last = -1j


def go_carts():
    with open('../assets/day13_input.txt') as file:
        track = [[c for c in line] for line in file.read().split('\n')]
    cars = []
    for y in range(len(track)):
        for x in range(len(track[y])):
            if track[y][x] == '>' or track[y][x] == '<':
                cars.append(Car(x, y, 1 if track[y][x] == '>' else -1))
                track[y][x] = '-'
            elif track[y][x] == '^' or track[y][x] == 'v':
                cars.append(Car(x, y, 1j if track[y][x] == 'v' else -1j))
                track[y][x] = '|'

    found_collision = False
    while len(cars) > 1:
        rems = set()
        cars.sort(key=lambda c: c.x * 1000 + c.y)
        for car in cars:
            car.x += car.v.real
            car.y += car.v.imag
            next_track = track[int(car.y)][int(car.x)]

            if next_track == '\\':
                car.v = car.v.imag + car.v.real * 1j
            elif next_track == '/':
                car.v = -car.v.imag - car.v.real * 1j
            elif next_track == '+':
                car.v *= car.last
                car.last *= 1j
                if car.last == -1:
                    car.last = -1j

            for other in cars:
                if car.x == other.x and car.y == other.y and car != other:
                    if not found_collision:
                        print('First Collision: %d, %d' % (car.x, car.y))
                        found_collision = True
                    rems.add(car)
                    rems.add(other)

        for car in rems:
            cars.remove(car)
        if len(cars) == 1:
            print('Last Car: %d, %d' % (cars[0].x, cars[0].y))


if __name__ == '__main__':
    go_carts()