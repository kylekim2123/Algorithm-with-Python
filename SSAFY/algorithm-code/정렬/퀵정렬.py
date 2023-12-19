def partition(arr, start, end):
    pivot = (start+end) // 2
    L, R = start, end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
    arr[pivot], arr[R] = arr[R], arr[pivot]
    return R


def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


a = [1, 5, 0, 2, 96, 4, -1, 5, 11, 102]
quick_sort(a, 0, len(a)-1)
print(a)
