def selection_sort(arr, arr_len):
    for i in range(arr_len-1):
        min_index = i
        for j in range(i+1, arr_len):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    selection_sort(numbers, n)
    print('#%s' % t, end=' ')
    i, j = 0, n-1
    while i <= j and i < 5:
        print('%s %s' % (numbers[j], numbers[i]), end=' ')
        i += 1
        j -= 1
    print()
