# 1182. 부분수열의 합 (실버2)


def combinations(depth, total):
    if depth > 0 and total == s:
        global case
        case += 1

    for i in range(depth, n):
        combinations(i + 1, total + numbers[i])


n, s = map(int, input().split())
numbers = list(map(int, input().split()))
case = 0

combinations(0, 0)

print(case)
