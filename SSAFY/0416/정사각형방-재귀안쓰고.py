di, dj = [1, -1, 0, 0], [0, 0, -1, 1]

def make_possible_list(n):
    possible = [False] * (n*n+1)
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < n and 0 <= nj < n and rooms[ni][nj] == rooms[i][j] + 1:
                    possible[rooms[i][j]] = True
                    break
    return possible

for t in range(1, int(input())+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    possible = make_possible_list(n)

    i, count, max_count = 1, 1, 1
    while i < len(possible):
        if possible[i]:
            count += 1
        else:
            if count > max_count:
                max_room, max_count = i - count + 1, count
            count = 1
        i += 1
    print('#%s %s %s' % (t, max_room, max_count))