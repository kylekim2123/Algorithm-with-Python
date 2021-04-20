# 6057. 그래프의 삼각형

from itertools import combinations

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y], graph[y][x] = 1, 1
    
    count = 0
    for i, j, k in combinations(range(1, n+1), 3):
        if graph[i][j] and graph[i][k] and graph[j][k]:
            count += 1
    print(f'#{t} {count}')