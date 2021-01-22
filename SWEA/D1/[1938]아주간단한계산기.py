# 1938. 아주 간단한 계산기
# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

numbers = list(map(int, input().split(' ')))
print(numbers[0] + numbers[1])
print(numbers[0] - numbers[1])
print(numbers[0] * numbers[1])
print(numbers[0] // numbers[1])