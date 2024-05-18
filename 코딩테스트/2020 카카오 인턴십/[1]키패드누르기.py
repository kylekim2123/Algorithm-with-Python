from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
l, r = {1, 4, 7}, {3, 6, 9}

def is_possible(phone, nx, ny, h):
    if h == 'left':
        if phone[nx][ny] in r:
            return False
    else:
        if phone[nx][ny] in l:
            return False
    return True

def bfs(phone, start, end, h):
    x, y = start
    visited = [[0]*3 for _ in range(4)]
    visited[x][y] = visited[3][0] = visited[3][2] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 4 and 0 <= ny < 3 and not visited[nx][ny] and is_possible(phone, nx, ny, h):
                visited[nx][ny] = visited[x][y] + 1
                if phone[nx][ny] == end:
                    return (nx, ny), visited[nx][ny]
                queue.append((nx, ny))

def solution(numbers, hand):
    phone = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [-1, 0, -2]
    ]

    lh, rh = (3, 0), (3, 2)
    result = []
    for number in numbers:
        if number in l:
            location, _ = bfs(phone, lh, number, 'left')
            lh = location
            result.append('L')
        elif number in r:
            location, _ = bfs(phone, rh, number, 'right')
            rh = location
            result.append('R')
        else:
            left_location, left_count = bfs(phone, lh, number, 'left')
            right_location, right_count = bfs(phone, rh, number, 'right')
            if left_count < right_count:
                lh = left_location
                result.append('L')
            elif left_count > right_count:
                rh = right_location
                result.append('R')
            else:
                if hand == 'left':
                    lh = left_location
                    result.append('L')
                else:
                   rh = right_location
                   result.append('R')
    return ''.join(result)

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
