# 5986. 새샘이와 세 소수

from itertools import combinations_with_replacement

primes = [0, 0] + list(range(2, 1000))
for i in range(2, 1000):
    if primes[i]:
        for j in range(i+i, 1000, i):
            primes[j] = 0

result = []
for t in range(1, int(input())+1):
    n = int(input())
    temp, count = [], 0
    for prime in primes:
        if prime and prime < n:
            temp.append(prime)
    for case in combinations_with_replacement(temp, 3):
        if sum(case) == n:
            count += 1
    result.append(f'#{t} {count}')
print('\n'.join(result))