# 상 하 좌 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 시작 지점 찾기
def find_start_point():
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                return i, j

def bfs(x, y):
    queue = [(x, y)]
    maze[x][y] = '1'
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if maze[nx][ny] != '1':
                if maze[nx][ny] == '3':
                    return 1 # 도착점에 도착하면 1 반환
                queue.append((nx, ny))
                maze[nx][ny] = '1'
    return 0 # 도착점에 도착하지 못하면 0 반환

for _ in range(1, 11):
    t = input()
    maze = [list(input()) for _ in range(100)]
    start_x, start_y = find_start_point() # 시작 지점
    print('#%s %s' % (t, bfs(start_x, start_y)))
