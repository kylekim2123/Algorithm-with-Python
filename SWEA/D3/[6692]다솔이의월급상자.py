# 6692. 다솔이의 월급 상자

results = []
for t in range(1, int(input())+1):
    n = int(input())
    result = 0
    for _ in range(n):
        p, x = map(float, input().split())
        result += p*x
    results.append(f'#{t} {result:.6f}')
print('\n'.join(results))