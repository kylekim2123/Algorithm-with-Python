# 골드 4

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
parent = list(range(n + 1))
rank = [0] * (n + 1)
edges = []
total, max_cost, counts = 0, 0, 0  # 총 비용, 최대 비용, 간선 수

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()  #

for c, a, b in edges:
    if union(a, b):
        total += c  # 총 비용 합산
        max_cost = max(max_cost, c)  # 최대 비용 갱신
        counts += 1  # 간선 수 추가

        if counts == n - 1:
            break  # (정점 - 1) 개의 간선에 도달하면 종료

print(total - max_cost)
