# 1261. 알고스팟 (골드4)

import sys, heapq
input = sys.stdin.readline


def dijkstra(x, y):
    queue = []
    visited = [[False]*m for _ in range(n)]
    cnt = [[n*m]*m for _ in range(n)]
    heapq.heappush(queue, (0, x, y))
    while queue:
        count, cx, cy = heapq.heappop(queue)
        if visited[cx][cy]:
            continue
        if cx == n-1 and cy == m-1:
            return count
        visited[cx][cy] = True
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                next_count = count + maze[nx][ny]
                if next_count < cnt[nx][ny]:
                    cnt[nx][ny] = next_count
                    heapq.heappush(queue, (next_count, nx, ny))


m, n = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
print(dijkstra(0, 0))