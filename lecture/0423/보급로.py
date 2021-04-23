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
            if 0 <= nx < n and 0 <= ny < n: # 지도의 범위에서 벗어나지 않고
                next_d = D[cx][cy] + area[nx][ny] # 이동 했을 때 드는 복구 시간
                if next_d < D[nx][ny]: # 더 적은 복구 시간으로만 이동(일종의 가지치기 및 방문처리)
                    D[nx][ny] = next_d
                    queue.append((nx, ny))
    return D[n-1][n-1]

for t in range(1, int(input())+1):
    n = int(input())
    area = [list(map(int, input())) for _ in range(n)]
    print('#%s %s' % (t, bfs(0, 0)))