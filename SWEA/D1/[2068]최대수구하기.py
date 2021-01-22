# 2068. 최대 수 구하기

result = []
for i in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    result.append(f'#{i} {max(numbers)}')

for i in result:
    print(i)