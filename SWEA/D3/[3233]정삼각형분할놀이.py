# 3233. 정삼각형 분할 놀이

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    total, triangle = 0, 1
    for i in range(1, (a//b)+1):
        total += triangle
        triangle += 2
    print(f'#{t} {total}')


# 다른풀이 (제곱) -> 삼각형의 개수가 1, 4, 9, 16 ... 이런식으로 제곱수로 늘어나기 때문
for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    print('#{} {}'.format(t, (a//b)**2))