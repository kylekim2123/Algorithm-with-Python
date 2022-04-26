# 15650. N과 M (2) (실버3)


def permutations(start, nums):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = True
            permutations(i + 1, nums + [i])
            visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n + 1)
permutations(1, [])
