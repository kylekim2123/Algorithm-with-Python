def powerset(depth, total):
    if total > m:
        return
    if total == m:
        global count
        count += 1
        return
    if depth < n:
        powerset(depth+1, total+arr[depth])
        powerset(depth+1, total)


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    powerset(0, 0)
    print('#%s %s' % (t, count))