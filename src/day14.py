# Day 14: Chocolate Charts


def part1(offset: int = 598701):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    while len(recipes) < 10 + offset:
        recipes += [int(c) for c in str(recipes[elf1] + recipes[elf2])]
        elf1, elf2 = (elf1 + 1 + recipes[elf1]) % len(recipes), (elf2 + 1 + recipes[elf2]) % len(recipes)
    print('Recipes: ', recipes[-10:])


def part2(search: int = 598701):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    search = [int(c) for c in str(search)]
    size = len(search)
    while True:
        recipes += [int(c) for c in str(recipes[elf1] + recipes[elf2])]
        elf1, elf2 = (elf1 + 1 + recipes[elf1]) % len(recipes), (elf2 + 1 + recipes[elf2]) % len(recipes)
        if search == recipes[-size:]:
            print('Found after:', len(recipes) - size)
            break
        elif search == recipes[-1-size:-1]:
            print('Found after:', len(recipes) - size - 1)
            break


if __name__ == '__main__':
    part1()
    part2()
