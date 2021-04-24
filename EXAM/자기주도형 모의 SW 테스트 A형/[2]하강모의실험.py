def get_block_R(row, col):
    block_R = 0
    while row < n and grid[row][col]:
        block_R += 1
        row += 1
    return block_R

def go_down():
    for c in range(n):
        if not grid[0][c] or grid[1][c]:
            continue
        r = count = power = 1
        while r < n:
            if not grid[r][c]:
                grid[r-count][c], grid[r][c] = 0, 1
                power *= 1.9
                r += 1
                continue
            block_R = get_block_R(r, c)
            if power <= block_R:
                break
            count += block_R
            power += block_R
            r += block_R

def swap():
    for i in range(n):
        for j in range(i):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

for t in range(1, 11):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    go_down()
    swap()
    go_down()
    result1 = 0
    for i in range(n):
        result1 += grid[i][-1]
    result2 = sum(grid[-1])
    print('#%s %s %s' % (t, result1, result2))