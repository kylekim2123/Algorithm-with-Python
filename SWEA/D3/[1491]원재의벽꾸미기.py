# 1491. 원재의 벽 꾸미기

for t in range(1, int(input())+1):
    n, a, b = map(int, input().split())
    min_value = b * (n-1)
    r = 1
    while r <= int(n**(0.5)):
        c = r
        while r*c <= n:
            min_value = min(min_value, a*abs(r-c) + b*(n-(r*c)))
            c += 1
        r += 1
    print(f'#{t} {min_value}')