def quick_sort(left, right):
    if left >= right:
        return
    i = left
    for j in range(left, right):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    quick_sort(left, i-1)
    quick_sort(i+1, right)

for t in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, n-1)
    print('#%s %s' % (t, arr[n//2]))
