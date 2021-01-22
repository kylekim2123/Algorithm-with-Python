# 2029. 몫과 나머지 출력하기
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

result = []
for i in range(1, int(input()) + 1):
    numbers = list(map(int, input().split(' ')))
    result.append(f'#{i} {numbers[0] // numbers[1]} {numbers[0] % numbers[1]}')

for i in result:
    print(i)