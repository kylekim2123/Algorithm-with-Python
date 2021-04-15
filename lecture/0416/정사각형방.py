dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
 
def dfs(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and rooms[nx][ny] == rooms[x][y] + 1:
            if memo[nx][ny] > 1:
                memo[x][y] = memo[nx][ny] + 1
                break
            memo[x][y] = dfs(nx, ny) + 1
            break
    return memo[x][y]
 
 
for t in range(1, int(input())+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    memo = [[1]*n for _ in range(n)]
    result = [0, 0]
    for i in range(n):
        for j in range(n):
            if memo[i][j] > 1:
                continue
            total = dfs(i, j)
            if total == result[1]:
                result[0] = min(result[0], rooms[i][j])
            elif total > result[1]:
                result[0] = rooms[i][j]
                result[1] = total
    print('#%s' % t, *result)
