import sys

input = sys.stdin.readline


# 사다리 타기를 했을 때의 결과 구하기
def play(ladders):
    numbers = list(range(1, n + 1))

    for a, b in ladders:
        numbers[a - 1], numbers[a] = numbers[a], numbers[a - 1]

    return numbers


def recursion(depth, picks):
    if depth == m:
        picks.sort(key=lambda x: x[1])
        temp = play(picks)

        if origin == temp:
            global min_counts
            min_counts = min(min_counts, len(picks))

        return

    recursion(depth + 1, picks)
    recursion(depth + 1, picks + [ladders[depth]])


n, m = map(int, input().split())
ladders = [list(map(int, input().split())) for _ in range(m)]
ladders.sort(key=lambda x: x[1])

origin = play(ladders)
min_counts = m

recursion(0, [])

print(min_counts)
