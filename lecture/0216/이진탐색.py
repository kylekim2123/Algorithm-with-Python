def count_binary_search(start, end, target):
    count = 0
    while start <= end:
        count += 1
        center = (start+end) // 2
        if center == target:
            break
        elif center > target:
            end = center
        else:
            start = center
    return count


T = int(input())
for t in range(1, T+1):
    p, pa, pb = map(int, input().split())
    a_count = count_binary_search(1, p, pa)
    b_count = count_binary_search(1, p, pb)
    if a_count > b_count:
        result = 'B'
    elif a_count < b_count:
        result = 'A'
    else:
        result = 0
    print('#%s %s' % (t, result))
