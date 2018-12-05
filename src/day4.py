# Day 4: Repose Record


def sleep_pattern():
    with open('../assets/day4_input.txt') as file:
        guard = -1
        guards = {}
        start = 0
        for line in file:
            if line[19:24] == 'Guard':
                guard = int(line[26:].split()[0])
            elif line[19:24] == 'falls':
                start = int(line[15:17])
            elif line[19:24] == 'wakes':
                end = int(line[15:17])
                if guard not in guards:
                    guards[guard] = [0]*60
                for i in range(start, end):
                    guards[guard][i] += 1

        max_guard = 0
        max_sleep = 0
        max_pattern = []
        for g, s in guards.items():
            if sum(s) > max_sleep:
                max_sleep = sum(s)
                max_guard = g
                max_pattern = s
        print('Max Time Asleep: %d' % (max_guard * max_pattern.index(max(max_pattern))))

        max_guard = 0
        max_sleep = 0
        max_minute = 0
        for g, s in guards.items():
            for i in range(60):
                if s[i] > max_sleep:
                    max_guard = g
                    max_sleep = s[i]
                    max_minute = i

        print('Most Frequent Minute: %d' % (max_guard * max_minute))


sleep_pattern()
