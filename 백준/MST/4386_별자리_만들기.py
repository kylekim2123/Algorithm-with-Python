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


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
parent = list(range(n))
rank = [0] * n
edges = []
total, counts = 0, 0

for i in range(n):
    x1, y1 = stars[i]

    for j in range(i + 1, n):
        x2, y2 = stars[j]
        distance = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2  # 피타고라스 정리를 이용한 거리 계산
        edges.append((distance, i, j))

edges.sort()

for distance, x, y in edges:
    if union(x, y):
        total += distance ** 0.5  # c^2의 상태이므로 루트 연산을 해야함
        counts += 1

        if counts == n - 1:
            break

print(f"{total:.2f}")
