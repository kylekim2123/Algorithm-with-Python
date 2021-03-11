# 9009. 피보나치 (실버1)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def fibo(number):
    if number >= 2 and len(memo) < number:
        memo.append(fibo(number-1) + fibo(number-2))
    return memo[number-1]

for _ in range(int(input())):
    n = int(input())
    memo = [0, 1]
    fibo(50)
    total, result = 0, []
    for i in range(len(memo)-1, -1, -1):
        if total + memo[i] <= n:
            total += memo[i]
            result.append(memo[i])
        if total == n:
            break
    print(*result[::-1])