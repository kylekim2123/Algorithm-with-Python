# 2. 사은품 교환하기

result = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < 5 or n + m < 12:
        result.append(0)
        continue
    result.append(min(n//5, (n+m)//12))
print('\n'.join(map(str, result)))