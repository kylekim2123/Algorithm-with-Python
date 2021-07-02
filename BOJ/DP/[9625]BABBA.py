# 9625. BABBA (브론즈1)

k = int(input())
A, B = 1, 0
for _ in range(k):
    A, B = B, A
    B += A
print(A, B)