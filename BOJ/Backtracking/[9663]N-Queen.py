# 9663. N-Queen (골드5)


# 대각선 검사
def is_possible(x, y):
    for i, j in queens:
        if abs(i - x) == abs(j - y):
            return False
    return True


def set_queen(x):
    if x == n:
        global total
        total += 1
        return

    for i in range(n):
        # 열, 대각선 검사
        if not visited[i] and is_possible(x, i):
            visited[i] = True
            queens.append((x, i))
            set_queen(x + 1)  # 행은 겹칠 일 없음
            visited[i] = False
            queens.pop()


n = int(input())
queens = []  # 대각선 검사용
visited = [False] * n  # 열 검사용
total = 0

set_queen(0)

print(total)
