# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4): # 4방향에 대하여
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == '0': # 미로의 범위를 벗어나지 않고, 통로라면
            maze[nx][ny] = '1' # 방문 표시
            dfs(nx, ny) # 이동

for t in range(1, int(input())+1):
    n = int(input())
    maze = []
    for i in range(n):
        line = list(input()) # 미로의 한 줄 입력 받기
        maze.append(line)
        for j in range(n):
            if line[j] == '2': # 시작점
                start_x, start_y = i, j
                break
            if line[j] == '3': # 도착점
                end_x, end_y = i, j
                maze[i][j] = '0' # 도착할 수 없다면 '0'으로 유지되고 / 도착하면 '1'로 바뀐다. -> 그 결과를 그대로 출력
                break
    dfs(start_x, start_y)
    print('#%s %s' % (t, maze[end_x][end_y]))
