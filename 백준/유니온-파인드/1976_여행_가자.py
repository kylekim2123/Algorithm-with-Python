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
        return

    # union by rank
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1  # 랭크가 같은 것끼리 합한 후에는 랭크 + 1을 해준다.


n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))
parent = list(range(n + 1))
rank = [0] * (n + 1)

# 인접 행렬로 표현된 그래프 상에서 연결된 도시끼리 union
for i in range(n):
    for j in range(i + 1, n):  # A-B이면 B-A와 같으므로, i + 1 번째부터 탐색해도 무방함
        if graph[i][j] == 1:
            union(i + 1, j + 1)

group = find(plans[0])  # 출발 도시의 집합이 기준이 됨
result = "YES"

for plan in plans[1:]:
    if group != find(plan):
        result = "NO"  # 하나의 도시라도 다른 집합에 속하면 여행할 수 없음
        break

print(result)
