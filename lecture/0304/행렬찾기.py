# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
    queue = [(s, e)]
    warehouse[s][e] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and warehouse[nx][ny]:
                queue.append((nx, ny))
                warehouse[nx][ny] = 0
    return x-s+1, y-e+1

for t in range(1, int(input())+1):
    n = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(n)]
    matrix = []
    for i in range(n):
        for j in range(n):
            if warehouse[i][j]:
                matrix.append(bfs(i, j))

    matrix.sort(key=lambda x: (x[0]*x[1], x[0]))
    result = [t, len(matrix)]
    for unit in matrix:
        result.append(unit[0])
        result.append(unit[1])
    print('#%s' % ' '.join(map(str, result)))
