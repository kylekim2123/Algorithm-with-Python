# 1949. 등산로 조성

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, is_cut, route):
    max_route = route
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = 1
            if not is_cut and 0 <= land[nx][ny]-land[x][y] < k:
                temp = land[nx][ny]
                land[nx][ny] = land[x][y] - 1
                max_route = max(max_route, dfs(nx, ny, True, route+1))
                land[nx][ny] = temp
            elif land[x][y] > land[nx][ny]:
                max_route = max(max_route, dfs(nx, ny, is_cut, route+1))
            visited[nx][ny] = 0
    return max_route

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    land = []
    max_number = 0
    for i in range(n):
        line = list(map(int, input().split()))
        max_number = max(max_number, max(line))
        land.append(line)

    max_route = 0
    for i in range(n):
        for j in range(n):
            if land[i][j] == max_number:
                visited = [[0]*n for _ in range(n)]
                visited[i][j] = 1
                max_route = max(max_route, dfs(i, j, False, 1))
    print(f'#{t} {max_route}')