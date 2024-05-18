# 15652. N과 M (4) (실버3)


def permutations(start, nums):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(start, n + 1):
        permutations(i, nums + [i])


n, m = map(int, input().split())
permutations(1, [])
