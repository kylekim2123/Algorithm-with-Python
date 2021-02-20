# 2948. 문자열 교집합

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    count = len(set(input().split()) & set(input().split()))
    print(f'#{t} {count}')
