# 10200. 구독자 전쟁

result = []
for t in range(1, int(input())+1):
    n, a, b = map(int, input().split())
    result.append(f'#{t} {min(a, b)} {max(a+b-n, 0)}')
print('\n'.join(result))