# 1933. 간단한 N의 약수
# 입력으로 1개의 정수 N 이 주어진다. 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

N = int(input())
result = []
for i in range(1, N // 2 + 1):
    if N % i == 0:
        result.append(i)
result.append(N)
print(*result)