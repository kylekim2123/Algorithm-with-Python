# 4796. 캠핑(실버5)

index = 1
while True:
    L, P, V = map(int, input().split())

    if L == P == V == 0:
        break
    
    result = L * (V//P)
    if V % P < L:
        result += V % P
    else:
        result += L
    print(f'Case {index}: {result}')
    index += 1