# 골드 2

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union_by_rank(x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        rank[y] += 1


n = int(input())
edges = [(int(input()), 0, i) for i in range(1, n + 1)]

for i in range(1, n + 1):
    line = list(map(int, input().split()))

    for j in range(i + 1, n + 1):
        edges.append((line[j - 1], i, j))

edges.sort()
parent = list(range(n + 1))
rank = [0] * (n + 1)
counts, total_cost = 0, 0

for cost, s, e in edges:
    s_root, e_root = find(s), find(e)

    if s_root != e_root:
        union_by_rank(s_root, e_root)
        total_cost += cost
        counts += 1

        if counts >= n:
            break

print(total_cost)
