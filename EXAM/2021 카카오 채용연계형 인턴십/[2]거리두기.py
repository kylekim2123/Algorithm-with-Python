# 2. 죠르디의 거리두기 검사

from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y, place):
    visited = [[0]*5 for _ in range(5)]
    visited[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if visited[x][y] >= 3:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != 'X':
                if place[nx][ny] == 'P':
                    return False
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return True

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not bfs(i, j, place):
                    return 0
    return 1

def solution(places):
    return [check(place) for place in places]

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]
print(solution(places))
