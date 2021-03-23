# 4698. 테네스의 특별한 소수

primes = [i for i in range(1000001)]
for i in range(2, 1000001):
    if primes[i]:
        for j in range(i+i, 1000001, i):
            primes[j] = 0

for t in range(1, int(input())+1):
    d, a, b = map(int, input().split())
    d = str(d)
    if a == 1:
        a = 2
    count = 0
    for i in range(a, b+1):
        if primes[i] and d in str(i):
            count += 1
    print(f'#{t} {count}')

