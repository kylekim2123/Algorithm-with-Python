# 3. 대여 시간을 추천해드립니다.

from datetime import time

n = int(input())
times = []
for _ in range(n):
    temp = input().split('~')
    times.append((temp[0].rstrip(), temp[1].lstrip()))
times = list(zip(*times))

result = []
for i in range(2):
    temp_arr = []
    for j in range(n):
        numbers = times[i][j].split(':')
        temp_arr.append(time(int(numbers[0]), int(numbers[1])))
    if i == 0:
        front = max(temp_arr)
        result.append(times[i][temp_arr.index(front)])
    else:
        rear = min(temp_arr)
        result.append(times[i][temp_arr.index(rear)])
if front > rear:
    print(-1)
else:
    print(f'{result[0]} ~ {result[1]}')

	