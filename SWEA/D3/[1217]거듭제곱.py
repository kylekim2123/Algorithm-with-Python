# 1217. S/W 문제해결 기본 4일차 - 거듭 제곱

def pow_recursion(number, index):
    if index == 1:
        return number
    return number * pow_recursion(number, index-1)

for _ in range(1, 11):
    t = int(input())
    inputs = list(map(int,input().split()))
    print(f'#{t} {pow_recursion(inputs[0], inputs[1])}')