from copy import deepcopy
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def find_chickens():
    chickens = []
    for i in range(n):
        for j in range(m):
            if area[i][j] == '2':
                chickens.append((i, j))
    return chickens


def get_thin_count(area):
    thin_count = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == '0':
                thin_count += 1
    return thin_count


def bfs(chickens):
    temp = deepcopy(area)
    queue = deque(chickens)
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == '0':
                temp[nx][ny] = '2'
                queue.append((nx, ny))
    return get_thin_count(temp)


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    area = [input().split() for _ in range(n)]
    chickens = find_chickens()
    max_counts = 0
    
    for a in range(n):
        for b in range(m):
            if area[a][b] == '0':
                area[a][b] = '1'
                for c in range(a, n):
                    d_start = b+1 if c == a else 0
                    for d in range(d_start, m):
                        if area[c][d] == '0':
                            area[c][d] = '1'
                            for e in range(c, n):
                                f_start = d+1 if e == c else 0
                                for f in range(f_start, m):
                                    if area[e][f] == '0':
                                        area[e][f] = '1'
                                        max_counts = max(max_counts, bfs(chickens))
                                        area[e][f] = '0'
                            area[c][d] = '0'
                area[a][b] = '0'

    print('#%s %s' % (t, max_counts) )
    