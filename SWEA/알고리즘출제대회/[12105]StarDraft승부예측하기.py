from itertools import combinations

def get_winner(i, j):
    p1, p2 = players[i], players[j]
    if p1 == 1 and p2 == 3:
        return j
    if p1 == 3 and p2 == 1:
        return i
    return i if p1 <= p2 else j


def play_league(players):
    first, second = [], []
    for k in range(0, len(players), 4):
        points = {number: 0 for number in range(k, k+4)}
        for i, j in combinations(points, 2):
            p1, p2 = min(i, j), max(i, j)
            points[get_winner(p1, p2)] += 1
        result = sorted(points.items(), key=lambda x: (-x[1], x[0]))
        first.append(result[0][0])
        second.append(result[1][0])
    return first, second[::-1]


def play_tournament(players):
    while True:
        first, second = [], []
        for round, player in enumerate(players):
            p1, p2 = min(player), max(player)
            if round % 2:
                second.append(get_winner(p1, p2))
            else:
                first.append(get_winner(p1, p2))
        players = list(zip(first, second))
        if len(players) <= 1:
            p1, p2 = min(players[0]), max(players[0])
            return get_winner(p1, p2)


for t in range(1, int(input())+1):
    players = list(map(int, input().split()))
    tournament_players = list(zip(*play_league(players)))
    winner = play_tournament(tournament_players)
    print(f'#{t} {winner}')