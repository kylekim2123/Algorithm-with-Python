# 4386. 별자리 만들기 (골드4)

import sys
input = sys.stdin.readline

def find_set(point):
    if point != parent[point]:
        parent[point] = find_set(parent[point])
    return parent[point]

n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        if i != j:
            dist = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**(0.5)
            edges.append((dist, i, j))
edges.sort()

parent = list(range(n))
total, count = 0, 0
for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root
        total += dist
        count += 1
        if count >= n-1:
            break
print('{:.2f}'.format(total))
    