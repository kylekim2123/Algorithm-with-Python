# D3

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


t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    groups = list(map(int, input().split()))
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total = 0

    for i in range(0, len(groups), 2):
        union(groups[i], groups[i + 1])

    for i in range(1, n + 1):
        if i == parent[i]:
            total += 1  # 집합의 대표 원소(=루트)의 개수가 곧 집합의 개수

    print(f"#{test_case} {total}")
