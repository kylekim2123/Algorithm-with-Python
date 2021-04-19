def quick_sort(left, right):
    if left >= right: # 남은 원소가 1개 이하여서, 왼쪽과 오른쪽이 겹치는 경우 정렬 종료
        return
    i = left
    for j in range(left, right):
        if arr[j] <= arr[right]: # j번째 값이 피봇값보다 작거나 같으면
            arr[i], arr[j] = arr[j], arr[i] # i와 j번째 값을 swap
            i += 1 # 그리고 i++
    arr[i], arr[right] = arr[right], arr[i] # 피봇값을 i번째로 swap하여 리스트를 두 구간으로 나눈다
    quick_sort(left, i-1) # 피봇값의 왼쪽 퀵 정렬
    quick_sort(i+1, right) # 피봇값의 오른쪽 퀵 정렬

for t in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, n-1)
    print('#%s %s' % (t, arr[n//2]))
