from collections import deque


def move():
    global seconds
    queue = deque([(0, 0)])

    for _ in range(k):
        d, p = input().split()
        p = int(p)
        dx, dy = dxy[d]

        for _ in range(p):
            seconds += 1
            sx, sy = queue[-1]
            nsx, nsy = sx + dx, sy + dy

            if nsx < 0 or nsx >= n or nsy < 0 or nsy >= n:
                return

            ex, ey = queue[0]

            if nsx == ex and nsy == ey:
                queue.append(queue.popleft())
                continue

            if board[nsx][nsy] == 2:
                return

            if board[nsx][nsy] == 0:
                ex, ey = queue.popleft()
                board[ex][ey] = 0

            board[nsx][nsy] = 2
            queue.append((nsx, nsy))


n, m, k = map(int, input().split())
board = [[0] * n for _ in range(n)]
dxy = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
board[0][0] = 2  # 뱀
seconds = 0

for _ in range(m):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1  # 사과

move()

print(seconds)
