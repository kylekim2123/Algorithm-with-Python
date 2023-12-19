def make_towers(n, r):
    if r <= 0:
        global min_height
        height = sum(tower)
        if B <= height < min_height:
            min_height = height
        return
    if n < r:
        return
    tower[r-1] = H[n-1]
    make_towers(n-1, r-1)
    make_towers(n-1, r)
 
 
for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_height = 20 * 10000
    for i in range(1, N+1):
        tower = [0] * i
        make_towers(N, i)
        if B == min_height:
            break
    print('#%s %s' % (t, min_height-B))