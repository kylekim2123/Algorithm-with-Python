# 골드 5

import sys

input = sys.stdin.readline

n = int(input())
student_likes = {}
board = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
total_score = 0

for _ in range(n * n):
    student, *likes = map(int, input().split())
    student_likes[student] = set(likes)
    queue = []

    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                continue

            like_counts = 0
            empty_counts = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in student_likes[student]:
                        like_counts += 1
                    elif board[nx][ny] == 0:
                        empty_counts += 1

            queue.append((like_counts, empty_counts, x, y))

    queue.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    _, _, x, y = queue[0]
    board[x][y] = student

for x in range(n):
    for y in range(n):
        like_counts = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in student_likes[board[x][y]]:
                like_counts += 1

        if like_counts == 2:
            like_counts = 10
        elif like_counts == 3:
            like_counts = 100
        elif like_counts == 4:
            like_counts = 1000

        total_score += like_counts

print(total_score)
