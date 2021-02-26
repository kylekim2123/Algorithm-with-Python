# 3750. Digit sum
result = []
for t in range(1, int(input())+1):
    n = int(input())
    while n % 10 != n:
        n = sum(map(int, list(str(n))))
    result.append(f'#{t} {n}')
print(*result, sep='\n')