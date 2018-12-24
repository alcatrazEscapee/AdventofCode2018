# Day 24: Immune System Simulator 20XX


class Group:
    def __init__(self, units, hp, init, atk, atk_type, immune=tuple(), weak=tuple()):
        self.units = units
        self.hp = hp
        self.init = init
        self.atk = atk
        self.atk_type = atk_type
        self.immune = immune
        self.weak = weak

        self.target = -1

    def eff_power(self):
        return self.atk * self.units

    # Simulates the amount of damage this would take from an enemy
    def dmg_simulate(self, enemy):
        if enemy.atk_type in self.immune:
            return 0
        elif enemy.atk_type in self.weak:
            return enemy.eff_power() * 2
        else:
            return enemy.eff_power()

    # Takes damage from an enemy
    def dmg(self, enemy):
        lost = self.dmg_simulate(enemy) // self.hp
        if lost > self.units:
            lost = self.units
        self.units -= lost
        if self.units <= 0:
            self.units = 0

    def dead(self):
        return self.units <= 0


def simulate(immune: list, infect: list):
    stale_counter = 0
    while True:

        # Sort by effective power, then units
        immune.sort(key=lambda g: (g.eff_power(), g.init), reverse=True)
        infect.sort(key=lambda g: (g.eff_power(), g.init), reverse=True)

        # Choose Targets. Immune first, then infect
        choose_targets(immune, infect)
        choose_targets(infect, immune)

        init_order = immune + infect
        init_order.sort(key=lambda g: g.init, reverse=True)
        total_units = sum(g.units for g in init_order)
        for unit in init_order:
            if unit.dead() or unit.target == -1:
                continue
            if unit in immune:
                infect[unit.target].dmg(unit)
            elif unit in infect:
                immune[unit.target].dmg(unit)

        # Remove dead units
        infect = [i for i in infect if not i.dead()]
        immune = [i for i in immune if not i.dead()]

        # If nothing can damage each other after 10+ turns of repetition, then declare a stalemate
        total_units -= sum(g.units for g in init_order)
        if total_units == 0:
            stale_counter += 1
        else:
            stale_counter = 0

        if len(infect) == 0:
            print('Immune won with %d left' % sum(i.units for i in immune))
            return True
        elif len(immune) == 0:
            print('Infect won with %d left' % sum(i.units for i in infect))
            return False

        if stale_counter == 10:
            print('Stalemate!')
            return False


def choose_targets(players, enemies):
    targets = set(range(len(enemies)))
    for player in players:
        player.target = -1
        if targets:
            sel_target = max(targets, key=lambda t: (enemies[t].dmg_simulate(player), enemies[t].eff_power(), enemies[t].init))
            if enemies[sel_target].dmg_simulate(player) > 0:
                targets.remove(sel_target)
                player.target = sel_target


def make_armies(boost=0):
    with open('../assets/day24_input.txt') as file:
        top, bottom = file.read().split('Infection:')

    immune_groups = parse_lines(top.split('\n')[1:-2])
    for g in immune_groups:
        g.atk += boost
    return immune_groups, parse_lines(bottom.split('\n')[1:])


def parse_lines(lines):
    groups = []
    for line in lines:
        words = ''.join(c for c in line if c not in '(),;').split()
        units, hp, init, atk = map(int, (words[x] for x in (0, 4, -1, -6)))
        atk_type = words[-5]
        immune = []
        weak = []
        words = words[7:-6]
        state = ''
        # Simple Finite State Machine to parse the words
        for word in words:
            if state == 'W-' or state == 'I-':
                state = state[0]
            elif word == 'weak':
                state = 'W-'
            elif word == 'immune':
                state = 'I-'
            elif word == 'with':
                break
            elif state == 'W':
                weak.append(word)
            elif state == 'I':
                immune.append(word)

        groups.append(Group(units, hp, init, atk, atk_type, tuple(immune), tuple(weak)))
    return groups


TEST_IMMUNE = [
    Group(17, 5390, 2, 4507, 'fire', weak=('radiation', 'bludgeoning')),
    Group(989, 1274, 3, 25, 'slashing', immune=('fire',), weak=('bludgeoning', 'slashing'))
]
TEST_INFECT = [
    Group(801, 4706, 1, 116, 'bludgeoning', weak=('radiation',)),
    Group(4485, 2961, 4, 12, 'slashing', immune=('radiation',), weak=('fire', 'cold'))
]

if __name__ == '__main__':
    simulate(TEST_IMMUNE, TEST_INFECT)
    simulate(*make_armies())

    atk_boost = 1
    while not simulate(*make_armies(atk_boost)):
        atk_boost += 1
