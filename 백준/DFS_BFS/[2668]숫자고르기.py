# 2668. 숫자 고르기 (골드5)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(start):
    next_idx = numbers[start]
    if i == next_idx:
        confirmed.update(visited)
        return
    if not visited[next_idx] and next_idx not in confirmed:
        visited[next_idx] = next_idx
        dfs(next_idx)

n = int(input())
numbers = [0] + [int(input()) for _ in range(n)]
confirmed = set()
for i in range(1, n+1):
    if i not in confirmed:
        visited = [0] * (n+1)
        visited[i] = i
        dfs(i)

print(len(confirmed)-1, *sorted(list(confirmed)[1:]), sep='\n')