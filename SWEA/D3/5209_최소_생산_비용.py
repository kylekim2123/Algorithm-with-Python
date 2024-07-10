def permutations(depth, total):
    global min_total

    if total >= min_total:  # 백트래킹(가지치기) -> 이미 합이 최소 이상이면 유망성이 없다고 판단
        return

    if depth == n:
        min_total = min(total, min_total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            permutations(depth + 1, total + board[depth][i])
            visited[i] = False


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_total = 1485  # N이 15까지 가능하고, 각 줄의 자연수는 99 이하이므로 최대 1485까지만 가능
    permutations(0, 0)

    print(f"#{test_case} {min_total}")
