def merge_sort(part):
    length = len(part)
    if length < 2:
        return part # 하나의 원소만 있는 리스트는 그대로 반환

    mid = length // 2 # 리스트를 나눌, 가운데 기준
    left = merge_sort(part[:mid]) # 왼쪽 반
    right = merge_sort(part[mid:]) # 오른쪽 반
    if left[-1] > right[-1]: # "왼쪽 마지막 원소 > 오른쪽 마지막 원소" 일때 갯수 + 1
        global count
        count += 1

    merged = [] # 왼쪽 반과 오른쪽 반을 병합하여 정렬될 리스트
    i, j = 0, 0 # 왼쪽과 오른쪽의 인덱스
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]) # 왼쪽 원소가 작거나 같으면 merged에 삽입
            i += 1
        else:
            merged.append(right[j]) # 오른쪽 원소가 작으면 merged에 삽입
            j += 1
    # merged에 삽입되지 못한 나머지 원소들 일제히 삽입
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    

for t in range(1, int(input())+1):
    n = int(input())
    count = 0
    arr = merge_sort(list(map(int, input().split())))
    print('#%s %s %s' % (t, arr[n//2], count))