# 1963. 소수 경로 (골드4)

import sys
from collections import deque
input = sys.stdin.readline

# 에라토스테네스의 체를 이용해 10000이하의 소수를 미리 구함
def get_primes(number):
    arr = [i for i in range(number+1)]
    for i in range(2, number+1):
        if arr[i] == 0:
            continue
        for j in range(i+i, number+1, i):
            arr[j] = 0
    result = set()
    for i in range(2, number+1):
        if arr[i] != 0:
            result.add(arr[i])
    return result

# 숫자, 위치, 바꿀 수 를 넣어서 해당 숫자의 어떤 위치를 digit으로 교체하는 함수
def change_digits(number, location, digit):
    number = list(map(int, str(number)))
    number[location] = digit
    return int(''.join(map(str, number)))

def bfs(number):
    primes = get_primes(10000) # 10000 이하의 소수 먼저 받아오고
    queue = deque([number])
    visited[number] = 1
    while queue:
        now = queue.popleft()
        for i in range(4): # 자리수 4개
            for j in range(10): # 0~9까지 모두 바꿔봄
                next_num = change_digits(now, i, j)
                if (next_num >= 1000) and (next_num in primes) and (not visited[next_num]): # 네 자리수이고, 소수이며, 방문하지 않은 경우
                    queue.append(next_num) # 큐에 삽입
                    visited[next_num] = visited[now]+1 # depth를 표현
                if next_num == end: # end숫자와 같으면 return True
                    return True
    return False # Impossible
   
for _ in range(int(input())):
    start, end = map(int, input().split())
    visited = [0] * 10000
    if bfs(start):
        print(visited[end]-1) # 처음 visited 시작이 1이므로, 결과적으로는 1을 빼야 한다.
    else:
        print('IMPOSSIBLE')
