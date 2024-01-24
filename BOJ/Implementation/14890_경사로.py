import sys

input = sys.stdin.readline


def check(road):
    prev = road[0]
    i, equals = 1, 1
    visited = [False] * n

    while i < n:
        now = road[i]

        if abs(prev - now) > 1:
            return

        if prev == now:
            equals += 1
            i += 1
            prev = now
            continue

        if prev < now:
            if equals < l:
                return

            for k in range(i - equals, i):
                if visited[k]:
                    return

            prev = now
            i += 1
            equals = 1
        else:
            temp = 1
            for j in range(i + 1, n):
                if temp == l or road[j] != now:
                    break
                temp += 1

            if temp < l:
                return

            for k in range(i, i + min(temp, l)):
                visited[k] = True

            prev = now
            i += min(temp, l)

            if i >= n:
                break

            equals = 0 if prev == road[i] else 1

    global answer
    answer += 1
    print(road)


n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    check(board[i])  # 가로길
    check([board[j][i] for j in range(n)])  # 세로길

print(answer)
