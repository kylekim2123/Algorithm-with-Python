# 1. 전원 연결

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def go(x, y, di, dj):
    count = 0
    route = []
    while True:
        nx, ny = x+di, y+dj
        if processor[nx][ny] == '2':
            return count, route
        if processor[nx][ny] == '1' or processor[nx][ny] == '3':
            return -1, route
        processor[nx][ny] = '3'
        count += 1
        route.append((nx, ny))
        x, y = nx, ny

def recursion(my_index, core_count, line_count):
    if my_index >= length:
        global max_value
        if core_count == max_value[0] and line_count < max_value[1]:
            max_value = (core_count, line_count)
        elif core_count > max_value[0]:
            max_value = (core_count, line_count)
        return
    is_all_fail = True
    for i in range(4):
        count, route = go(targets[my_index][0], targets[my_index][1], dx[i], dy[i])
        if count == -1:
            for r, c in route:
                processor[r][c] = '0'
            continue
        is_all_fail = False
        recursion(my_index+1, core_count+1, line_count+count)
        for r, c in route:
            processor[r][c] = '0'
    if is_all_fail:
        recursion(my_index + 1, core_count, line_count)

for t in range(1, int(input())+1):
    n = int(input())
    processor = [['2']*(n+2)]
    processor += [['2']+input().split()+['2'] for _ in range(n)]
    processor += [['2']*(n+2)]
    targets = []
    for i in range(2, n):
        for j in range(2, n):
            if processor[i][j] == '1':
                targets.append((i, j))
    length = len(targets)
    max_value = (0, 0) # core, line
    recursion(0, 0, 0)
    print('#%s %s' % (t, max_value[1]))
