import sys

input = sys.stdin.readline


def travel(now_point, total):
    if all(visited):
        if costs[now_point][0] == 0:
            return

        global min_total
        min_total = min(total + costs[now_point][0], min_total)

        return

    for next_point in range(1, n):
        if next_point == 0 or costs[now_point][next_point] == 0 or visited[next_point]:
            continue

        visited[next_point] = True
        travel(next_point, total + costs[now_point][next_point])
        visited[next_point] = False


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_total = 99999999

visited[0] = True
travel(0, 0)

print(min_total)
