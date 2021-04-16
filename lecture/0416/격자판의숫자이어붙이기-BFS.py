# 1. BFS
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y, 0, grid[x][y])]
    while queue:
        x, y, count, number = queue.pop(0)
        if count >= 6:
            result.add(number)
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                queue.append((nx, ny, count+1, number+grid[nx][ny]))

for t in range(1, int(input())+1):
    grid = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j)
    print('#%s %s' % (t, len(result)))