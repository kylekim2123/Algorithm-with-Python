# 2071. 평균값 구하기

def get_avg(numbers):
    return round(sum(numbers) / len(numbers))

result = []
for i in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    result.append(f'#{i} {get_avg(numbers)}')

for i in result:
    print(i)