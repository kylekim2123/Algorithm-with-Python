def drive(start, count, battery):
    global min_count
    if count >= min_count:
        return
    if start >= n-1:
        min_count = count
        return
    if battery >= m[start]:
        return
    for i in range(1, m[start]+1):
        drive(start+i, count+1, m[start]-i)


for t in range(1, int(input())+1):
    n, *m = map(int, input().split())
    min_count = n - 2
    drive(0, 0, 0)
    print('#%s %s' % (t, min_count-1))