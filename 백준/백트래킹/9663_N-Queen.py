# 골드 4

def is_promising(x, y):
    # 열 검사
    if visited[y]:
        return False

    # 대각선 검사
    for i, j in queens:
        if abs(i - x) == abs(j - y):
            return False

    return True


def set_queen(x):
    if x == n:  # 종료조건(Base)
        global total
        total += 1
        return

    # x행의 모든 i열에 대해
    for i in range(n):
        if is_promising(x, i):  # 가지치기(pruning) -> 여기서 유망하지 않으면 탐색 안함
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
