# 2072. 홀수만 더하기

result = []
for i in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    total = 0
    for j in numbers:
        if j % 2 == 1:
            total += j
    result.append(f'#{i} {total}')

for i in result:
    print(i)