# 17103. 골드바흐 파티션 (실버2)

arr = [i for i in range(1000001)]
for i in range(2, 1000001):
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j] = 0

for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(2, n//2+1):
        if arr[i] and arr[n-i]:
            count += 1
    print(count)