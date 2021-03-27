# 13706. 제곱근 (브론즈1)

n = int(input())
i, j = 1, n
while i <= j:
    center = (i + j) // 2
    temp = center * center
    if temp == n:
        print(center)
        break
    if temp > n:
        j = center
        continue
    i = center