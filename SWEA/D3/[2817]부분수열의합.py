# 2817. 부분 수열의 합

# 비트연산 이용
for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    count = 0
    for i in range(1, 1<<n):
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += numbers[j]
        if total == k:
            count += 1
    print(f'#{t} {count}')


# combination 모듈 이용
from itertools import combinations

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    count = 0
    for i in range(1, n+1):
        n_perm = combinations(numbers, i)
        for case in n_perm:
            total = sum(case)
            count += 1 if total == k else 0
    print(f'#{t} {count}')