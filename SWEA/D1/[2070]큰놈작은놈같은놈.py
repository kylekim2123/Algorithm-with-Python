# 2070. 큰 놈, 작은 놈, 같은 놈

result = []
for i in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    if numbers[0] > numbers[1]:
        result.append(f'#{i} >')
    elif numbers[0] < numbers[1]:
        result.append(f'#{i} <')
    else:
        result.append(f'#{i} =')

for i in result:
    print(i)