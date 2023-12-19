# 비트연산자를 이용한 부분집합 출력

arr = [1, 2, 3, 4, 5]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=', ')
    print()
print()