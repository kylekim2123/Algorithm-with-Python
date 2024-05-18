# 1976. 여행 가자 (골드4)

import sys
input = sys.stdin.readline

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

n, m = int(input()), int(input())
parent = list(range(n+1))
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            i_root, j_root = find_set(i+1), find_set(j+1)
            if i_root != j_root:
                parent[j_root] = i_root

plans = list(map(int, input().split()))
result = 'YES'
first_set = find_set(plans[0])
for plan in plans[1:]:
    if first_set != find_set(plan):
        result = 'NO'
        break
print(result)