# 에라토스테네스의 체 (소수 빠르게 판별)

number = int(input())
arr = [i for i in range(number+1)]
for i in range(2, number+1):
    if arr[i] == 0: # 이미 지워졌으면 소수가 아님
        continue
    for j in range(i+i, number+1, i): # 작은 수부터 자신의 배수를 모두 지워나간다.(자신은 제외)
        arr[j] = 0

for i in range(2, number+1):
    if arr[i] != 0:
        print(arr[i], end=' ')