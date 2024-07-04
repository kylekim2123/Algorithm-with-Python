# 골드 3

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])  # path compression

    return parent[x]


def union(x, y):
    x_root, y_root = find(x), find(y)

    if x_root == y_root:
        return False

    # union by rank
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1  # 랭크가 같은 것끼리 합한 후에는 랭크 + 1을 해준다.

    return True


n, m = map(int, input().split())
gods = [list(map(int, input().split())) for _ in range(n)]
parent = list(range(n + 1))
rank = [0] * (n + 1)
edges = []
total, counts = 0, 0

# 이미 연결된 우주신들은 같은 집합으로 만들기
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

# 좌표평면 상의 우주신들의 간선 정보 만들기
for i in range(n):
    x1, y1 = gods[i]

    for j in range(i + 1, n):
        x2, y2 = gods[j]
        distance = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2  # 피타고라스 정리를 이용한 거리 계산
        edges.append((distance, i + 1, j + 1))

edges.sort()

# 크루스칼 알고리즘
for distance, x, y in edges:
    if union(x, y):
        total += distance ** 0.5  # c^2의 상태이므로 루트 연산을 해야함
        counts += 1

        if counts == n - 1:
            break

print(f"{total:.2f}")
