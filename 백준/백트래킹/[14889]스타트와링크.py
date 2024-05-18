# 14889. 스타트와 링크 (실버2)

import sys

input = sys.stdin.readline


def sum_stats(team):
    return sum(stats[i][j] for i in team for j in team if i != j)


def make_team(now):
    if len(start_team) == n // 2:
        global min_diff
        link_team = set(range(n)) - start_team
        min_diff = min(min_diff, abs(sum_stats(start_team) - sum_stats(link_team)))

    for i in range(now + 1, n):
        start_team.add(i)
        make_team(i)
        start_team.remove(i)


n = int(input().rstrip())
stats = [list(map(int, input().split())) for _ in range(n)]
start_team = set()
min_diff = 99999999

make_team(0)
print(min_diff)
