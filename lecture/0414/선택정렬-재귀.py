def selection_sort(arr, i):
    length = len(arr)
    if i == length-1:
        return
    min_idx = i
    for j in range(i, length):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    selection_sort(arr, i + 1)


for t in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, 0)
    print('#%s' % t, *arr)
