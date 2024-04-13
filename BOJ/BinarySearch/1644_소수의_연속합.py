# 골드 3

import sys

input = sys.stdin.readline


def check_prime(end_number):
    is_prime = [True] * (end_number + 1)

    for i in range(2, int(end_number ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end_number + 1, i):
                is_prime[j] = False

    return is_prime


n = int(input())

if n <= 3:
    print(0 if n == 1 else 1)
else:
    is_prime = check_prime(n)
    prime_numbers = [i for i in range(2, n + 1) if is_prime[i]]
    start, end, total = 0, 0, 0
    result = 1 if is_prime[n] else 0

    while end < len(prime_numbers):
        if total >= n:
            total -= prime_numbers[start]
            start += 1
        else:
            total += prime_numbers[end]
            end += 1

        result += 1 if total == n else 0

    print(result)
