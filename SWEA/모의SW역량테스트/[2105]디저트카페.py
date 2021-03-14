# 2105. 디저트 카페

def move(x, y, dx, dy, case):
    if dx == [-1] and dy == [-1]:
        number = 1
    else:
        number = 2
    for k in range(number):
        nx, ny = x+dx[k], y+dy[k]
        if nx == i and ny == j:
            global max_count
            max_count = max(max_count, case.count(1))
            return
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not case[dessert[nx][ny]]:
            visited[nx][ny] = 1
            temp = list(case)
            temp[dessert[nx][ny]] = 1
            dfs(nx, ny, dx[k], dy[k], temp)
            visited[nx][ny] = 0

def dfs(x, y, pdx, pdy, case):
    if pdx == 1 and pdy == -1: # 좌하
        move(x, y, [1, 1], [-1, 1], case)
    elif pdx == 1 and pdy == 1: # 우하
        move(x, y, [1, -1], [1, 1], case)
    elif pdx == -1 and pdy == 1: # 우상
        move(x, y, [-1, -1], [-1, 1], case)
    elif pdx == -1 and pdy == -1: # 좌상
        move(x, y, [-1], [-1], case)

for t in range(1, int(input())+1):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]
    max_count = -1
    for i in range(n):
        for j in range(n):
            gcase = [0] * 101
            visited = [[0]*n for _ in range(n)]
            visited[i][j] = 1
            gcase[dessert[i][j]] = 1
            dfs(i, j, 1, -1, gcase)
    print('#%s %s' % (t, max_count))