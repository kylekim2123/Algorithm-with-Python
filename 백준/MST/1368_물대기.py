# 골드 2

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
edges = [(int(input()), 0, i) for i in range(1, n + 1)]  # 가상의 0번 정점을 이용하여 직접 논에 우물을 파는 것을 표현
costs = [list(map(int, input().split())) for _ in range(n)]  # 인접행렬
parent = list(range(n + 1))
rank = [0] * (n + 1)
total, counts = 0, 0

# 다른 논으로부터 물을 끌어오는 비용 정보를 edges에 삽입
for i in range(n):
    for j in range(i + 1, n):
        edges.append((costs[i][j], i + 1, j + 1))

edges.sort()

for w, x, y in edges:
    if union(x, y):
        total += w
        counts += 1

        if counts == n:  # 0번 정점을 넣었으므로 간선이 n-1개가 아닌 n개이면 종료
            break

print(total)
