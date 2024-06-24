# 골드 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    x_root, y_root = find(x), find(y)

    if x_root == y_root:
        return False

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

    return True


n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)
edges = []
total, counts = 0, 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for c, a, b in edges:
    if union(a, b):
        total += c
        counts += 1

        if counts == n - 1:
            break

print(total)
