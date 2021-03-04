# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    queue = [(x, y)]
    visited[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4): # 상하좌우 네 방향을 본다
            nx, ny = x+dx[i], y+dy[i] # 한 방향으로 이동
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '1': # 미로의 범위를 넘지 않고, 방문하지 않았으며, 벽이 아닌 경우
                visited[nx][ny] = visited[x][y] + 1 # visited는 방문 체크용 뿐만 아니라, 몇 칸이 걸리는지 정보도 들어있다.
                if maze[nx][ny] == '3': # 도착점을 만나면
                    return visited[nx][ny] - 2 # 도착점까지 몇 칸 걸리는지 반환. (2를 빼는 이유는 출발점과 도착점은 "몇 칸 걸리는지"에 포함되지 않기 때문)
                queue.append((nx, ny))
    return 0

for t in range(1, int(input())+1):
    n = int(input())
    maze = []
    for i in range(n):
        line = list(input())
        maze.append(line)
        for j in range(n):
            if line[j] == '2': # 출발점을 찾으면
                start_x, start_y = i, j # 해당 좌표를 기록
                break
    print('#%s %s' % (t, bfs(start_x, start_y)))
