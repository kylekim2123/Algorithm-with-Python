# 1026. 보물 (실버4)

n = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
print(sum(A[i] * B[i] for i in range(n)))
