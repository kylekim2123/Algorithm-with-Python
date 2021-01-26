# 1984. 중간 평균 값 구하기

for t in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    remains = numbers[1:-1]
    print(f'#{t} {round(sum(remains) / len(remains))}')