def merge_sort(part):
    length = len(part)
    if length < 2:
        return part

    mid = length // 2
    left = merge_sort(part[:mid])
    right = merge_sort(part[mid:])
    if left[-1] > right[-1]:
        global count
        count += 1

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    

for t in range(1, int(input())+1):
    n = int(input())
    count = 0
    arr = merge_sort(list(map(int, input().split())))
    print('#%s %s %s' % (t, arr[n//2], count))