# 1717. 집합의 표현 (골드4)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union_set(x, y):
    x_root, y_root = find_set(x), find_set(y)
    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root

n, m = map(int, input().split())
parent = list(range(n+1))
for _ in range(m):
    e, a, b = map(int, input().split())
    if e:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    else:
        union_set(a, b)
