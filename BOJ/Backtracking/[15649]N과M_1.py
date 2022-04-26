# 15649. N과 M (1) (실버3)


def permutations(nums):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            permutations(nums + [i])
            visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n + 1)
permutations([])
