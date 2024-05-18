# 15651. N과 M (3) (실버3)


def permutations(nums):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(1, n + 1):
        permutations(nums + [i])


n, m = map(int, input().split())
permutations([])
