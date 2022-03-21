# 24463. 미로 (실버1)

import sys

sys.setrecursionlimit(10 ** 9)  # 파이썬의 최대 재귀 깊이를 늘리기 위함
input = sys.stdin.readline  # 백준에서 입력을 빠르게 받는 편법
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우


# 경로 찾기
def dfs(x, y):
    # 도착점에 도달하면 종료
    if x == end_x and y == end_y:
        return True

    # 상하좌우로 움직이며, 이동할 수 있는 곳으로 경로 이동
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == "@":  # 이동 가능한가?
            maze[nx][ny] = "."  # 이동가능하면 일단 . 으로 바꿈
            if dfs(nx, ny):
                return True
            maze[nx][ny] = "@"  # 하나의 경로로 DFS를 끝내면, 다시 @로 바꾸면서 경로 초기화

    return False


n, m = map(int, input().split())
maze, holes = [], []  # 미로, 구멍(출발, 도착)

for i in range(n):
    line = list(input().rstrip())  # 한 줄 입력
    for j in range(m):
        if line[j] == ".":
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:  # 출발점 혹은 도착점이라면
                holes.append((i, j))
            line[j] = "@"  # 여기가 포인트! 일단 .에서 @로 모두 바꿔주고 시작한다.
    maze.append(line)

start_x, start_y = holes[0]
end_x, end_y = holes[1]

dfs(start_x, start_y)
maze[start_x][start_y] = "."  # 출발점은 @로 남아있기 때문에, .으로 바꿔줌

print(*["".join(line) for line in maze], sep="\n")  # 미로 상태 출력
