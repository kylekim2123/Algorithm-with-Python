# 2027. 대각선 출력하기
# 주어진 텍스트를 그대로 출력하세요.

index = 0
for i in range(5):
    for j in range(5):
        if j == index:
            print('#', end='')
        else:
            print('+', end='')
    index += 1
    print()