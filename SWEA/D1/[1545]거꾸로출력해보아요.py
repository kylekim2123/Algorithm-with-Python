# 1545. 거꾸로 출력해 보아요
# 주어진 숫자부터 0까지 순서대로 찍어보세요

number = int(input())
print(*range(number, -1, -1))