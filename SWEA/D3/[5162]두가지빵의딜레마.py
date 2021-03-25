# 5162. 두 가지 빵의 딜레마

for t in range(1, int(input())+1):
    a, b, c = map(int, input().split())
    print(f'#{t} {c//min(a, b)}')