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
total, counts = 0, 0

for _ in range(m):
    a, b, c = map(int, input().split())  # 정점a, 정점b, 가중치c
    edges.append((c, a, b))  # 가중치를 먼저 넣어서, 가중치 기준 정렬 되도록 함

edges.sort()  # 크루스칼 알고리즘을 위한 가중치 기준 정렬

for c, a, b in edges:
    if union(a, b):  # 간선을 이으면(같은 집합에 넣으면)
        total += c  # 가중치 더하기
        counts += 1

        if counts == n - 1:
            break  # 트리의 특성 상, 간선의 개수는 (정점 - 1) 이므로 이에 도달하면 종료

print(total)
