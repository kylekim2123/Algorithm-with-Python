# 골드 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])  # path compression

    return parent[x]


n, m = map(int, input().split())
parent = list(range(n))
rank = [0] * n
result = 0

for t in range(1, m + 1):
    x, y = map(int, input().split())
    x_root, y_root = find(x), find(y)

    if x_root == y_root:
        result = t
        break

    # union by rank
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1  # 랭크가 같은 것끼리 합한 후에는 랭크 + 1을 해준다.

print(result)
