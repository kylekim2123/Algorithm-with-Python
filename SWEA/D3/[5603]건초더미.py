# 5603. 건초더미

for t in range(1, int(input())+1):
    n = int(input())
    dummy = sorted(int(input()) for _ in range(n))
    each = sum(dummy) // n
    i, result = n-1, 0
    while i >= 0 and dummy[i] > each:
        result += (dummy[i] - each)
        i -= 1
    print(f'#{t} {result}')
    