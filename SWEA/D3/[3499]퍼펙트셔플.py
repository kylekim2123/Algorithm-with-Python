# 3499. 퍼펙트 셔플

for t in range(1, int(input())+1):
    n = int(input())
    cards = input().split()
    half = (n//2) + 1 if n % 2 else n // 2
    one = cards[:half]
    two = cards[half:]
    print(f'#{t}', end=' ')
    for i in range(n//2):
        print(f'{one[i]} {two[i]}', end=' ')
    if n % 2:
        print(f'{one[-1]}')
    else:
        print()