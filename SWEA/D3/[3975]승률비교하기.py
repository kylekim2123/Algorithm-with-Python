# 3975. 승률 비교하기

result = []
for t in range(1, int(input())+1):
    a, b, c, d = map(int, input().split())
    alice, bob = a/b, c/d
    if alice > bob:
        result.append(f'#{t} ALICE')
    elif bob > alice:
        result.append(f'#{t} BOB')
    else:
        result.append(f'#{t} DRAW')
print(*result, sep='\n')