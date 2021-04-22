# 1249. 보급로

INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    D = [[INF]*n for _ in range(n)]
    D[x][y] = 0
    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_d = D[cx][cy] + area[nx][ny]
                if next_d < D[nx][ny]:
                    D[nx][ny] = next_d
                    queue.append((nx, ny))
    return D[n-1][n-1]

for t in range(1, int(input())+1):
    n = int(input())
    area = [list(map(int, input())) for _ in range(n)]
    print('#%s %s' % (t, bfs(0, 0)))
