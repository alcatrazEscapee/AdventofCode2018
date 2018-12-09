# Day 9: Marble Mania
from collections import defaultdict, deque


def marble_game(max_turns: int = 25, max_players: int = 9):
    players = defaultdict(int)
    marbles: deque = deque([0])
    for turn in range(1, 1 + max_turns):
        if turn % 23 == 0:
            marbles.rotate(6)
            players[turn % max_players] += turn + marbles.pop()
        else:
            marbles.rotate(-2)
            marbles.insert(0, turn)
    return max(map(players.get, players))


if __name__ == '__main__':
    # ALL the test cases!
    assert marble_game(25, 9) == 32
    assert marble_game(1618, 10) == 8317
    assert marble_game(7999, 13) == 146373
    assert marble_game(1104, 17) == 2764
    assert marble_game(6111, 21) == 54718
    assert marble_game(5807, 30) == 37305
    print('Part 1:', marble_game(71144, 424))
    print('Part 2:', marble_game(7114400, 424))
