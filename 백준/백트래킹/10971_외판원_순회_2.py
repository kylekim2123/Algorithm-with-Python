# 실버 2

import sys

input = sys.stdin.readline


def permutations(city, depth, cost):
    global min_cost

    if cost >= min_cost:  # 백트래킹(가지치기) -> 현재까지의 비용이 최소 이상이면 유망성이 없다고 판단
        return

    if depth == n - 1 and w[city][0] > 0:  # 출발 노드로 돌아오기 직전이고, 출발 노드로 갈 수 있으면
        min_cost = min(cost + w[city][0], min_cost)  # 최소 비용 갱신하고 종료
        return

    for next_city in range(n):
        if not visited[next_city] and w[city][next_city] > 0:  # 아직 방문 안했고, 갈 수 있으면
            visited[next_city] = True  # 일단 방문
            permutations(next_city, depth + 1, cost + w[city][next_city])
            visited[next_city] = False  # 방문 취소


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_cost = 9999999

visited[0] = True  # 어차피 모든 정점을 순회해야 하므로, 0번에서 출발한다고 가정
permutations(0, 0, 0)

print(min_cost)
