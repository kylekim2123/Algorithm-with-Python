import sys

input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
answer = [1_000_000_000, 1_000_000_000]
i, j = 0, n - 1

while i < j:
    total = values[i] + values[j]

    if abs(total) < abs(sum(answer)):
        answer = [values[i], values[j]]

    if total == 0:
        break

    if total > 0:
        j -= 1
    else:
        i += 1

print(*answer)
