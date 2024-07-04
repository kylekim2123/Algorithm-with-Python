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


n, m = map(int, input().split())
truth_counts, *truth_people = map(int, input().split())
parties = [list(map(int, input().split())) for _ in range(m)]
parent = list(range(n + 1))
rank = [0] * (n + 1)

if truth_counts == 0:
    print(m)  # 진실을 아는 사람이 아무도 없다면, 모든 파티에서 거짓말 가능
else:
    # 진실을 아는 사람이 한 명이라도 있다면,
    # 1) 진실을 아는 사람들을 같은 집합으로 묶는다.
    for i in range(1, truth_counts):
        parent[truth_people[i]] = truth_people[0]

    # 2) 각 파티에 속한 사람들을 각각의 집합으로 묶는다.
    # 이때 진실을 아는 사람이 섞여 있다면, 해당 파티의 인원들은 모두 진실을 아는 사람들이 된다.
    for counts, *people in parties:
        for i in range(1, counts):
            union(people[0], people[i])

    # 3) 각 파티 중 거짓말이 가능한 파티만 센다.
    truth_group = find(truth_people[0])
    result = 0

    for _, *people in parties:
        if truth_group != find(people[0]):  # 해당 파티에 진실을 아는 사람이 없다면,
            result += 1  # 거짓말 가능한 파티 + 1

    print(result)
