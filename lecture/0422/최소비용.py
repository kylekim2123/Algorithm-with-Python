INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dijkstra(x, y):
    costs = [[INF]*n for _ in range(n)]
    costs[x][y] = 0
    queue = [(0, x, y)]
    while queue:
        cost, cx, cy = queue.pop(0)
        if costs[cx][cy] < cost:
            continue
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + 1
                if H[nx][ny] > H[cx][cy]:
                    next_cost += H[nx][ny] - H[cx][cy]
                if next_cost < costs[nx][ny]:
                    costs[nx][ny] = next_cost
                    queue.append((next_cost, nx, ny))
    return costs[n-1][n-1]


for t in range(1, int(input())+1):
    n = int(input())
    H = [list(map(int, input().split())) for _ in range(n)]
    print('#%s %s' % (t, dijkstra(0, 0)))
