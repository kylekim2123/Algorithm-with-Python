# 2019. 더블더블
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오. 주어질 숫자는 30을 넘지 않는다.

number = int(input())
result = []
box = 1
for i in range(number + 1):
    result.append(box)
    box *= 2
print(*result)