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
        rank[y_root] += 1

    return True


while True:
    m, n = map(int, input().split())

    if m == n == 0:
        break  # 0 0 이 입력되면 종료

    edges = []
    parent = list(range(m))
    rank = [0] * m
    total_cost, counts, minimum_cost = 0, 0, 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total_cost += z  # z를 모두 더하면 총 비용을 알 수 있음

    edges.sort()

    for z, x, y in edges:
        if union(x, y):
            minimum_cost += z
            counts += 1

            if counts >= m - 1:
                break  # 정점이 n개면 간선이 n-1개임을 이용하여 크루스칼의 효율성 확보

    print(total_cost - minimum_cost)  # 총 비용에서 최소 비용을 빼면 절약 비용을 알 수 있음
