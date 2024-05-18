# 9663. N-Queen (골드5)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def is_possible(now_row):
    for past_row in range(now_row):
        if (now_row-past_row) == abs(check[now_row]-check[past_row]):
            return False
    return True

count = 0 # vscode 빨간줄 없애기 위한 선언(지울 필요있음)
def set_queen(row):
    if row == n:
        global count
        count += 1
        return
    for col in range(n):
        check[row] = col
        if not visited[col] and is_possible(row):
            visited[col] = True
            set_queen(row+1)
            visited[col] = False

n = int(input())
check = [0] * n
visited = [False] * n
count = 0
set_queen(0)
print(count)