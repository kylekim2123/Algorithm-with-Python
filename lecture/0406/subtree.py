def count_subtree(node):
    global count
    count += 1
    if left[node]:
        count_subtree(left[node])
    if right[node]:
        count_subtree(right[node])

for t in range(1, int(input())+1):
    e, n = map(int, input().split())
    pairs = list(map(int, input().split()))
    left, right = [0]*(e+2), [0]*(e+2)
    for i in range(0, e*2-1, 2):
        if left[pairs[i]]:
            right[pairs[i]] = pairs[i+1]
        else:
            left[pairs[i]] = pairs[i+1]
    count = 0
    count_subtree(n)
    print('#%s %s' % (t, count))
    